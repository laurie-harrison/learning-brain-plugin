# Learning Brain — Claude Code plugin

One install gets you:

1. **32 evidence-grounded learning-design tools** (MCP server) — curriculum architect, instructional writer, delivery coach, course doctor, and learning scientist personas, backed by 188 curated research notes across 9 domains.
2. **A workflow skill** that orchestrates the tools — elicit-first, audit-always, evidence-cited discipline that keeps Claude from inventing citations or skipping rigor.

## Install

### Prerequisites

- Claude Code ≥ 2.0
- A Learning Brain API key — sign up at <https://learningbrain.ai/#connect>. The success screen shows your key. Lost it? Sign up again with the same email and you'll get the same active key back.

### From this repo (local dev)

```bash
claude --plugin-dir /path/to/learning-brain-mcp/plugin
```

### From Codeberg (one-line install)

```
/plugin marketplace add https://codeberg.org/learningbrain/learning-brain-plugin.git
/plugin install learning-brain@learning-brain
```

Claude Code will prompt for your API key at enable time and store it securely (macOS Keychain / encrypted credentials file). No hand-editing of config files.

## What you get

After enable, your Claude Code session has:

- `mcp__learning-brain__*` — all 32 tools (lb_*, ls_*, arch_*, write_*, coach_*, doctor_*)
- `learning-brain:mcp-workflow` skill — auto-triggers when you ask about instructional design, learning objectives, MCQs, audits, live sessions, or learning-science questions

## What the skill does

It enforces six task-shape workflows and anti-agreeableness discipline that the tool descriptions alone can't reliably produce:

- Calls `lb_elicit_*` tools before design (doesn't prose-ask)
- Chains `doctor_*` audits after every `arch_*` and `write_*` (doesn't skip)
- Never invents named citations or frameworks
- Pushes back on user pushback instead of capitulating

A pilot comparison (2026-04-17) showed a 10/30 → 29/30 lift across six task shapes when the skill is loaded vs. the bare MCP.

## Uninstall

```
/plugin disable learning-brain
/plugin uninstall learning-brain
```

Your API key is removed from the keychain on uninstall.

## Troubleshooting

**"Tool not found" errors.** The MCP connection failed. Check:
1. `/mcp` shows `learning-brain` as connected
2. Your API key is still valid: visit <https://learningbrain.ai/#connect> and use "Fetch my key"
3. If behind a corporate proxy blocking `mcp-remote`, fall back to the direct OAuth URL at <https://learningbrain.ai/connect>

**Rate limits, access issues.** Email <info@learningbrain.ai>.

## License

MIT. See plugin.json.
