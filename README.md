# Learning Brain plugin

This repo now ships both:

1. **The Learning Brain MCP server** — 32 evidence-grounded learning-design tools across curriculum architecture, instructional writing, delivery coaching, course doctoring, and learning science.
2. **The Learning Brain workflow skill** — elicit-first, audit-always, evidence-cited discipline that keeps Codex or Claude from skipping rigor.

## Codex

### Best path: install the plugin so Codex gets both the MCP and the skill

Prerequisites:

- Codex app, CLI, or IDE extension
- A Learning Brain beta signup at <https://learningbrain.ai/#connect>

From this repo:

```bash
cd /path/to/learning-brain-mcp/plugin
python3 scripts/install_codex_plugin.py
```

What that does:

- Copies this plugin into `~/.codex/plugins/learning-brain`
- Creates or updates `~/.agents/plugins/marketplace.json`
- Adds Learning Brain to your personal Codex plugin marketplace

Then:

1. Restart Codex.
2. Open `Plugins`.
3. Find `Learning Brain` in your personal marketplace and install it.
4. Authenticate when Codex prompts you for the Learning Brain MCP server.

After install, Codex has:

- the bundled `learning-brain` skill
- the bundled Learning Brain MCP server at `https://learningbrain.ai/mcp`
- OAuth-based authentication, so users do not need to hand-edit headers or store an API key manually

### Fastest path: connect the MCP only

If you only want the 32 tools and do not need the workflow skill, open Codex settings and add the remote MCP server directly:

- URL: `https://learningbrain.ai/mcp`
- Transport: `Streamable HTTP`

That is the lightest-weight setup, but the plugin path above performs better because it also loads the orchestration skill.

## Claude Code

### From this repo (local dev)

```bash
claude --plugin-dir /path/to/learning-brain-mcp/plugin
```

### From GitHub

```
/plugin marketplace add https://github.com/laurie-harrison/learning-brain-plugin.git
/plugin install learning-brain@learning-brain
```

Claude Code prompts for your Learning Brain API key at enable time and stores it securely.

## What you get

After enable, your session has:

- `mcp__learning-brain__*` — all 32 tools (lb_*, ls_*, arch_*, write_*, coach_*, doctor_*)
- `learning-brain` skill — auto-triggers when you ask about instructional design, learning objectives, MCQs, audits, live sessions, or learning-science questions

## What the skill does

The skill enforces six task-shape workflows and anti-agreeableness discipline that the tool descriptions alone do not reliably produce:

- Calls `lb_elicit_*` tools before design instead of prose-asking
- Chains `doctor_*` audits after every `arch_*` and `write_*`
- Never invents named citations or frameworks
- Pushes back on user pushback instead of capitulating

A pilot comparison on 2026-04-17 showed a `10/30 -> 29/30` lift across six task shapes when the skill was loaded vs. the bare MCP.

## Troubleshooting

**Codex plugin not showing up.** Re-run `python3 scripts/install_codex_plugin.py`, then restart Codex. Confirm `~/.agents/plugins/marketplace.json` contains a `learning-brain` entry and `~/.codex/plugins/learning-brain` exists.

**Codex shows the plugin but tools are unavailable.** Open the plugin details and authenticate the bundled Learning Brain MCP server. If you added `learning_brain` manually in `~/.codex/config.toml`, remember that the manual MCP entry and the plugin are separate setup paths.

**Codex CLI says `auth_status: unsupported`.** The CLI MCP listing does not fully reflect the desktop plugin auth flow. Check the desktop plugin first. If you are using the manual CLI MCP route, run `codex mcp login learning_brain`.

**Codex CLI cancels Learning Brain tool calls.** Verify the desktop plugin path first. The desktop app is the intended Codex experience; the raw CLI MCP path can behave differently from the plugin-managed flow.

**Codex probes `resources/list`.** Learning Brain returns a minimal compatibility resource. The product is still tool-first, so use the tools for real work rather than the resource surface.

**Claude says `tool not found`.** Open `/mcp` and confirm `learning-brain` is connected. If you need a fresh API key, visit <https://learningbrain.ai/connect> and use the key retrieval flow.

**Rate limits or access issues.** Email <info@learningbrain.ai>.

## License

MIT.
