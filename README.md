# Learning Brain Codex / Claude plugin

This repo ships the workflow layer for both Learning Brain products:

1. **Learning Brain** — 32 evidence-grounded learning-design tools for instructional design, course architecture, writing, delivery coaching, course doctoring, and learning science.
2. **ELT Brain** — 25 evidence-grounded English Language Teaching tools: 9 shared foundation tools plus 16 ELT-specific tools for lessons, syllabi, materials writing, exam items, classroom delivery, learner affect, and audit.
3. **Workflow skills for Codex and Claude** — elicit-first, audit-always, evidence-cited discipline that keeps agents from skipping rigor.

## Codex

### Best path: install the plugin so Codex gets MCP + skills

Prerequisites:

- Codex app, CLI, or IDE extension
- A Learning Brain signup at <https://learningbrain.ai/#connect> for the core product
- An ELT Brain signup at <https://eltbrain.com/#connect> for the ELT product

From this repo:

```bash
cd /path/to/learning-brain-mcp/plugin
python3 scripts/install_codex_plugin.py
```

What that does:

- Copies this plugin into `~/.codex/plugins/learning-brain`
- Creates or updates `~/.agents/plugins/marketplace.json`
- Adds the Learning Brain / ELT Brain bundle to your personal Codex plugin marketplace

Then:

1. Restart Codex.
2. Open `Plugins`.
3. Find `Learning Brain` in your personal marketplace and install it.
4. Authenticate whichever bundled MCP server you need when Codex prompts: `learning-brain` for the core product, `learning-brain-elt` for ELT Brain.

After install, Codex has:

- the bundled `learning-brain` skill
- the bundled `learning-brain-elt` skill
- the bundled Learning Brain MCP server at `https://learningbrain.ai/mcp`
- the bundled ELT Brain MCP server at `https://eltbrain.com/mcp`
- OAuth-based authentication, so users do not need to hand-edit headers or store an API key manually

Use `learning-brain` for corporate L&D, instructional design, and general learning-science work. Use `learning-brain-elt` for English Language Teaching, SLA, language materials, CEFR/ACTFL alignment, and ELT assessment.

### Fastest path: connect an MCP only

If you only want the tools and do not need the workflow skill, open Codex settings and add the remote MCP server directly:

- Core URL: `https://learningbrain.ai/mcp`
- ELT URL: `https://eltbrain.com/mcp`
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
- `mcp__learning-brain-elt__*` — all 25 ELT Brain tools (lb_*, ls_*, arch_*, write_*, doctor_*, coach_*)
- `learning-brain` skill — auto-triggers when you ask about instructional design, learning objectives, MCQs, audits, live sessions, or learning-science questions
- `learning-brain-elt` skill — auto-triggers when you ask about ELT lessons, language syllabi, vocabulary, reading/listening/grammar/speaking tasks, exam items, classroom activity, learner affect, input-quality audits, or SLA/materials-design evidence

## What the skill does

The skill enforces six task-shape workflows and anti-agreeableness discipline that the tool descriptions alone do not reliably produce:

- Calls `lb_elicit_*` tools before design instead of prose-asking
- Chains `doctor_*` audits after every `arch_*` and `write_*`
- Never invents named citations or frameworks
- Pushes back on user pushback instead of capitulating

A pilot comparison on 2026-04-17 showed a `10/30 -> 29/30` lift across six task shapes when the skill was loaded vs. the bare MCP.

## Troubleshooting

**Codex plugin not showing up.** Re-run `python3 scripts/install_codex_plugin.py`, then restart Codex. Confirm `~/.agents/plugins/marketplace.json` contains a `learning-brain` entry and `~/.codex/plugins/learning-brain` exists.

**Codex shows the plugin but tools are unavailable.** Open the plugin details and authenticate the bundled MCP server you need. If you added `learning_brain` or `learning-brain-elt` manually in `~/.codex/config.toml`, remember that the manual MCP entry and the plugin are separate setup paths.

**Codex CLI says `auth_status: unsupported`.** The CLI MCP listing does not fully reflect the desktop plugin auth flow. Check the desktop plugin first. If you are using the manual CLI MCP route, run `codex mcp login learning-brain` or `codex mcp login learning-brain-elt`.

**Codex CLI cancels Learning Brain tool calls.** Verify the desktop plugin path first. The desktop app is the intended Codex experience; the raw CLI MCP path can behave differently from the plugin-managed flow.

**Codex probes `resources/list`.** Learning Brain returns a minimal compatibility resource. The product is still tool-first, so use the tools for real work rather than the resource surface.

**Claude says `tool not found`.** Open `/mcp` and confirm `learning-brain` is connected. If you need a fresh API key, visit <https://learningbrain.ai/connect> and use the key retrieval flow.

**Rate limits or access issues.** Email <info@learningbrain.ai>.

## License

MIT.
