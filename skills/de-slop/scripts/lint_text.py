#!/usr/bin/env python3
"""Flag common AI-style writing habits without rewriting the source."""

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Tuple


@dataclass
class Finding:
    code: str
    severity: str
    line: int
    message: str
    excerpt: str


Rule = Tuple[str, str, re.Pattern, str]


RULES: Sequence[Rule] = (
    (
        "DS001",
        "high",
        re.compile(r"\u2014|&mdash;|&#8212;|&#x2014;", re.IGNORECASE),
        "Em dash found. Recast the sentence with ordinary punctuation.",
    ),
    (
        "DS002",
        "high",
        re.compile(
            r"\bnot\s+(?:just|only|merely|simply)\b[^.!?\n]{0,140}"
            r"\bbut(?:\s+also)?\b",
            re.IGNORECASE,
        ),
        "Formulaic negative contrast found. State the positive claim directly.",
    ),
    (
        "DS003",
        "high",
        re.compile(
            r"\b(?:it|this|that)\s+(?:is|was)(?:n't| not)\b"
            r"(?!\s+(?:just|only|merely|simply)\b)[^.!?\n]{0,100}"
            r"(?:[,;:]\s*but\b|[.;:]\s*(?:it|this|that)\s+(?:is|was)\b)",
            re.IGNORECASE,
        ),
        "Staged 'not A, B' contrast found. Keep only the useful distinction.",
    ),
    (
        "DS004",
        "high",
        re.compile(
            r"\b(?:no|not)\s+[^.!?\n]{1,45}[.,]\s*"
            r"(?:no|not)\s+[^.!?\n]{1,45}[.,]\s*just\s+[^.!?\n]{1,80}",
            re.IGNORECASE,
        ),
        "Repeated negation followed by 'just' found. State the point directly.",
    ),
    (
        "DS010",
        "medium",
        re.compile(
            r"^\s*(?:great|excellent|good|smart|insightful|fantastic)\s+"
            r"(?:question|point|idea|observation)\b",
            re.IGNORECASE | re.MULTILINE,
        ),
        "Canned praise appears before the answer.",
    ),
    (
        "DS011",
        "medium",
        re.compile(
            r"^\s*(?:you(?:'re| are)\s+)?"
            r"(?:absolutely|completely|totally)\s+(?:right|correct)\b",
            re.IGNORECASE | re.MULTILINE,
        ),
        "Automatic agreement may be sycophantic. Verify the claim first.",
    ),
    (
        "DS012",
        "medium",
        re.compile(
            r"^\s*(?:certainly|absolutely|of course)[!,.:\s]+",
            re.IGNORECASE | re.MULTILINE,
        ),
        "Canned acknowledgment delays the answer.",
    ),
    (
        "DS013",
        "medium",
        re.compile(
            r"\b(?:let(?:'s| us)\s+(?:break\s+(?:it|this)\s+down|"
            r"dive\s+(?:in|into)|delve\s+into|unpack|explore)|"
            r"here(?:'s| is)\s+(?:the\s+thing|the\s+catch|the\s+kicker|"
            r"what\s+(?:most\s+)?people\s+miss))\b",
            re.IGNORECASE,
        ),
        "Preamble or false-suspense phrase found. Deliver the point directly.",
    ),
    (
        "DS020",
        "low",
        re.compile(
            r"^\s*(?:in\s+conclusion|in\s+summary|to\s+sum\s+up|"
            r"overall|to\s+bring\s+it\s+back)\b",
            re.IGNORECASE | re.MULTILINE,
        ),
        "Signposted conclusion may repeat what the reader already knows.",
    ),
    (
        "DS021",
        "medium",
        re.compile(
            r"\b(?:if\s+you(?:'d|\s+would)\s+like,\s+i\s+can|"
            r"let\s+me\s+know\s+if\s+you\s+(?:want|need)|"
            r"feel\s+free\s+to\s+(?:ask|reach\s+out)|hope\s+this\s+helps)\b",
            re.IGNORECASE,
        ),
        "Generic closing offer found. Stop when the requested work is complete.",
    ),
    (
        "DS030",
        "low",
        re.compile(
            r"\b(?:the\s+)?(?:result|reason|problem|truth|answer|catch|"
            r"worst\s+part|best\s+part)\?\s+[A-Z]",
        ),
        "Self-asked question may be manufacturing emphasis.",
    ),
    (
        "DS040",
        "low",
        re.compile(
            r"\b(?:it\s+is\s+worth\s+noting|it\s+bears\s+mentioning|"
            r"in\s+today(?:'s|\s+modern)\s+(?:world|landscape)|"
            r"in\s+an?\s+ever[- ](?:changing|evolving)\s+(?:world|landscape))\b",
            re.IGNORECASE,
        ),
        "Filler transition or generic scene-setting found.",
    ),
    (
        "DS050",
        "medium",
        re.compile(
            r"\b(?:stands|serves|functions|operates)\s+as\s+(?:a|an|the)\b",
            re.IGNORECASE,
        ),
        "A simple verb such as 'is' may be clearer.",
    ),
    (
        "DS051",
        "medium",
        re.compile(
            r"\b(?:experts|observers|critics|analysts|industry\s+reports|"
            r"research|studies|many\s+believe)\s+(?:say|argue|suggest|"
            r"show|indicate|have\s+cited|believe)\b",
            re.IGNORECASE,
        ),
        "Vague attribution found. Name the source or narrow the claim.",
    ),
    (
        "DS052",
        "low",
        re.compile(
            r"\b(?:pivotal\s+moment|enduring\s+legacy|indelible\s+mark|"
            r"rich\s+tapestry|complex\s+landscape|transformative\s+power|"
            r"game[- ]changing|revolutionary\s+shift|reshap(?:e|es|ing)\s+"
            r"(?:everything|the\s+future))\b",
            re.IGNORECASE,
        ),
        "Inflated or promotional language found. Name the concrete effect.",
    ),
    (
        "DS060",
        "low",
        re.compile(r"^\s*[-*+]\s+\*\*[^*\n]{1,80}\*\*\s*:", re.MULTILINE),
        "Bold-first bullet pattern found. Use plain bullets unless labels aid scanning.",
    ),
    (
        "DS061",
        "low",
        re.compile(
            r"^\s{0,3}#{1,6}\s+(?:"
            r"(?:What|Why|Where|How|When)\b|"
            r"(?:[A-Z][a-z]+(?:\s+|$)){3,})",
            re.MULTILINE,
        ),
        "Template-like or title-case heading found. Check whether it is needed.",
    ),
    (
        "DS062",
        "low",
        re.compile(
            r"^\s*(?:[-*+]\s+|#{1,6}\s+)?"
            r"[\U0001F300-\U0001FAFF\u2600-\u27BF]",
            re.MULTILINE,
        ),
        "Decorative emoji marker found.",
    ),
)


WATCH_WORDS = (
    "delve",
    "tapestry",
    "landscape",
    "realm",
    "intricate",
    "intricacies",
    "interplay",
    "nuanced",
    "multifaceted",
    "robust",
    "meticulous",
    "meticulously",
    "showcase",
    "showcasing",
    "underscore",
    "underscores",
    "underscoring",
    "foster",
    "fostering",
    "leverage",
    "leveraging",
    "harness",
    "streamline",
    "seamless",
    "pivotal",
    "transformative",
    "vibrant",
)


def mask_code(text: str) -> str:
    """Blank fenced and inline code while preserving line numbers."""
    lines = text.splitlines(keepends=True)
    masked: List[str] = []
    fence: Optional[str] = None

    for line in lines:
        match = re.match(r"^\s*(```+|~~~+)", line)
        if match:
            marker = match.group(1)[0]
            if fence is None:
                fence = marker
            elif fence == marker:
                fence = None
            masked.append("\n" if line.endswith("\n") else "")
            continue
        if fence is None:
            masked.append(line)
        else:
            masked.append("\n" if line.endswith("\n") else "")

    without_fences = "".join(masked)
    return re.sub(
        r"`+[^`\n]+`+",
        lambda match: " " * len(match.group(0)),
        without_fences,
    )


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def compact_excerpt(value: str, limit: int = 140) -> str:
    value = re.sub(r"\s+", " ", value).strip()
    if len(value) <= limit:
        return value
    return value[: limit - 3].rstrip() + "..."


def add_regex_findings(text: str, findings: List[Finding]) -> None:
    for code, severity, pattern, message in RULES:
        for match in pattern.finditer(text):
            findings.append(
                Finding(
                    code=code,
                    severity=severity,
                    line=line_number(text, match.start()),
                    message=message,
                    excerpt=compact_excerpt(match.group(0)),
                )
            )


def add_watchword_density(text: str, findings: List[Finding]) -> None:
    lowered = text.lower()
    counts = {
        word: len(re.findall(r"\b" + re.escape(word) + r"\b", lowered))
        for word in WATCH_WORDS
    }
    counts = {word: count for word, count in counts.items() if count}
    word_count = max(1, len(re.findall(r"\b[\w'-]+\b", text)))
    total = sum(counts.values())
    threshold = max(3, (word_count + 249) // 250)

    if total >= threshold and len(counts) >= 2:
        summary = ", ".join(
            "{} ({})".format(word, count)
            for word, count in sorted(
                counts.items(), key=lambda item: (-item[1], item[0])
            )
        )
        findings.append(
            Finding(
                code="DS070",
                severity="low",
                line=1,
                message=(
                    "High density of generic AI-associated vocabulary. "
                    "Replace only words that are vague, inflated, or repetitive."
                ),
                excerpt=compact_excerpt(summary),
            )
        )


def sentence_chunks(text: str) -> List[Tuple[str, int]]:
    chunks: List[Tuple[str, int]] = []
    for paragraph_match in re.finditer(
        r"(?:^|\n\s*\n)([^\n].*?)(?=\n\s*\n|\Z)", text, re.S
    ):
        paragraph = paragraph_match.group(1)
        if "http://" in paragraph or "https://" in paragraph:
            continue
        if any(
            re.match(r"^\s*(?:#{1,6}\s+|[-*+]\s+|\d+[.)]\s+)", line)
            for line in paragraph.splitlines()
        ):
            continue
        for match in re.finditer(r"[^.!?\n]+[.!?]", paragraph):
            value = match.group(0).strip()
            if value:
                chunks.append(
                    (value, paragraph_match.start(1) + match.start())
                )
    return chunks


def add_fragment_cluster(text: str, findings: List[Finding]) -> None:
    chunks = sentence_chunks(text)
    run: List[Tuple[str, int]] = []

    for sentence, offset in chunks:
        words = re.findall(r"\b[\w'-]+\b", sentence)
        if 2 <= len(words) <= 5:
            run.append((sentence, offset))
            if len(run) == 3:
                excerpt = " ".join(item[0] for item in run)
                findings.append(
                    Finding(
                        code="DS071",
                        severity="low",
                        line=line_number(text, run[0][1]),
                        message=(
                            "Three short sentences appear in sequence. "
                            "Check for manufactured punch."
                        ),
                        excerpt=compact_excerpt(excerpt),
                    )
                )
        else:
            run = []


def add_repeated_openings(text: str, findings: List[Finding]) -> None:
    chunks = sentence_chunks(text)
    openings: List[Tuple[str, int, str]] = []

    for sentence, offset in chunks:
        words = re.findall(r"[A-Za-z][A-Za-z'-]*", sentence.lower())
        if len(words) >= 3:
            openings.append((" ".join(words[:2]), offset, sentence))

    for index in range(len(openings) - 2):
        group = openings[index : index + 3]
        if len({item[0] for item in group}) == 1:
            findings.append(
                Finding(
                    code="DS072",
                    severity="low",
                    line=line_number(text, group[0][1]),
                    message=(
                        "Three nearby sentences share the same opening. "
                        "Keep the repetition only if it is deliberate."
                    ),
                    excerpt=compact_excerpt(" ".join(item[2] for item in group)),
                )
            )


def add_layout_findings(text: str, findings: List[Finding]) -> None:
    lines = text.splitlines()
    word_count = max(1, len(re.findall(r"\b[\w'-]+\b", text)))
    headings = [
        (index + 1, line)
        for index, line in enumerate(lines)
        if re.match(r"^\s{0,3}#{1,6}\s+\S", line)
    ]
    if len(headings) >= 3 and len(headings) * 50 > word_count:
        findings.append(
            Finding(
                code="DS080",
                severity="medium",
                line=headings[0][0],
                message="Heading density is high for the amount of text.",
                excerpt="{} headings across {} words".format(
                    len(headings), word_count
                ),
            )
        )

    longest_bullet_run = 0
    current_bullet_run = 0
    bullet_run_start = 1
    longest_bullet_start = 1
    for index, line in enumerate(lines):
        if re.match(r"^\s*[-*+]\s+\S", line):
            if current_bullet_run == 0:
                bullet_run_start = index + 1
            current_bullet_run += 1
            if current_bullet_run > longest_bullet_run:
                longest_bullet_run = current_bullet_run
                longest_bullet_start = bullet_run_start
        elif line.strip():
            current_bullet_run = 0

    if longest_bullet_run >= 9:
        findings.append(
            Finding(
                code="DS081",
                severity="low",
                line=longest_bullet_start,
                message="Long bullet sequence may need grouping, trimming, or prose.",
                excerpt="{} consecutive bullet items".format(longest_bullet_run),
            )
        )

    for index, line in enumerate(lines):
        words = re.findall(r"\b[\w'-]+\b", line)
        if len(words) > 180:
            findings.append(
                Finding(
                    code="DS082",
                    severity="low",
                    line=index + 1,
                    message="Very long paragraph may hide multiple ideas.",
                    excerpt=compact_excerpt(line),
                )
            )


def normalize_paragraph(value: str) -> str:
    value = re.sub(r"[^\w\s]", "", value.lower())
    return re.sub(r"\s+", " ", value).strip()


def add_duplicate_paragraphs(text: str, findings: List[Finding]) -> None:
    paragraphs: List[Tuple[int, str]] = []
    for match in re.finditer(r"(?:^|\n\s*\n)([^\n].*?)(?=\n\s*\n|\Z)", text, re.S):
        paragraph = match.group(1).strip()
        normalized = normalize_paragraph(paragraph)
        if len(normalized.split()) >= 8:
            paragraphs.append((match.start(1), normalized))

    seen = {}
    for offset, normalized in paragraphs:
        if normalized in seen:
            findings.append(
                Finding(
                    code="DS090",
                    severity="high",
                    line=line_number(text, offset),
                    message="Duplicate paragraph found.",
                    excerpt=compact_excerpt(normalized),
                )
            )
        else:
            seen[normalized] = offset


def lint(text: str, include_code: bool = False) -> List[Finding]:
    checked = text if include_code else mask_code(text)
    findings: List[Finding] = []
    add_regex_findings(checked, findings)
    add_watchword_density(checked, findings)
    add_fragment_cluster(checked, findings)
    add_repeated_openings(checked, findings)
    add_layout_findings(checked, findings)
    add_duplicate_paragraphs(checked, findings)
    severity_order = {"high": 0, "medium": 1, "low": 2}
    return sorted(
        findings,
        key=lambda item: (severity_order[item.severity], item.line, item.code),
    )


def read_inputs(paths: Iterable[str]) -> List[Tuple[str, str]]:
    paths = list(paths)
    if not paths:
        return [("<stdin>", sys.stdin.read())]

    results = []
    for raw_path in paths:
        path = Path(raw_path)
        results.append((str(path), path.read_text(encoding="utf-8")))
    return results


def print_text_report(name: str, text: str, findings: Sequence[Finding]) -> None:
    word_count = len(re.findall(r"\b[\w'-]+\b", text))
    print("{}: {} words, {} finding(s)".format(name, word_count, len(findings)))
    for item in findings:
        print(
            "  {} {} line {}: {}".format(
                item.severity.upper(), item.code, item.line, item.message
            )
        )
        if item.excerpt:
            print("    {}".format(item.excerpt))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Flag common AI-style writing habits in text or Markdown."
    )
    parser.add_argument("paths", nargs="*", help="Files to lint. Reads stdin if omitted.")
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="Output format.",
    )
    parser.add_argument(
        "--include-code",
        action="store_true",
        help="Inspect fenced code blocks instead of masking them.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with status 1 when any finding is present.",
    )
    args = parser.parse_args()

    reports = []
    has_findings = False

    for name, text in read_inputs(args.paths):
        findings = lint(text, include_code=args.include_code)
        has_findings = has_findings or bool(findings)
        reports.append(
            {
                "path": name,
                "word_count": len(re.findall(r"\b[\w'-]+\b", text)),
                "findings": [asdict(item) for item in findings],
            }
        )
        if args.format == "text":
            print_text_report(name, text, findings)

    if args.format == "json":
        print(json.dumps(reports, indent=2))

    return 1 if args.strict and has_findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
