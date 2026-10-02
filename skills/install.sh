#!/bin/bash
# Installs the kit's skills into Claude Code (~/.claude/skills) and, if present, Codex (~/.codex/skills).
# Safe to re-run: it overwrites only these five skill folders.
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
for dest in "$HOME/.claude/skills" "$HOME/.codex/skills"; do
  if [ "$dest" = "$HOME/.codex/skills" ] && [ ! -d "$HOME/.codex" ]; then continue; fi
  mkdir -p "$dest"
  for s in cold-email de-slop chat-voice lead-research call-prep-onepager; do
    rm -rf "$dest/$s"; cp -R "$HERE/$s" "$dest/$s"
    echo "installed $s -> $dest/$s"
  done
done
echo "Done. Restart Claude Code so it picks up the new skills."
