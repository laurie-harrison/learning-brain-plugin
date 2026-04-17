---
name: mcp-workflow
description: Orchestrates the Learning Brain MCP (32 tools across 5 expert personas) for evidence-grounded instructional design. Use whenever the user wants to design, write, audit, or improve learning content — courses, modules, objectives, MCQs, question banks, worked examples, explanations, live sessions, discussions, facilitator guides — or ask evidence-backed learning-science questions (what does research say about X, is Y a myth, how do I diagnose Z). Enforces elicit-first, audit-always, and review-loop discipline that tool descriptions alone don't guarantee.
---

# Learning Brain MCP — workflow discipline

The MCP exposes 32 tools. Each returns a scaffold with curated evidence, rubrics, and pushback logic. The tools are strong; the failure mode is in *how they get strung together*. This skill is that glue.

## The five personas (one line each)

- **Cross-cutting (`lb_*`)** — elicitation, pushback, citations, worked examples
- **Learning Scientist (`ls_*`)** — evidence lookup, principle explanation, symptom diagnosis, tension resolution
- **Curriculum Architect (`arch_*`)** — courses, modules, sequencing, retrieval schedules, assessment blueprints, adaptive paths
- **Instructional Writer (`write_*`)** — objectives, MCQs, question banks, explanations, worked examples, feedback copy, diagnostics
- **Delivery Coach (`coach_*`)** — live sessions, discussions, facilitator scripts, stuck-learner interventions
- **Course Doctor (`doctor_*`)** — module audits, objectives audits, question audits, illusion scans, transfer prediction

Full tool list and schemas come from the MCP manifest — don't re-enumerate them here.

## Six task shapes → tool sequence

Match the user's request to one of these. The sequence is not optional.

### A. New course from scratch
1. `lb_elicit_course_brief` (unless brief is already complete and explicit)
2. `lb_elicit_learner_context` (unless already captured)
3. `arch_design_course`
4. For each module: `arch_design_module` → `write_objectives` → `doctor_audit_objectives` (gate)
5. `arch_sequence_content` + `arch_build_retrieval_schedule`
6. `arch_design_assessment_blueprint` → write + audit items
7. `doctor_predict_transfer` as final gate

### B. Single module
Skip the course layer. Start at step 4 of A, preceded by `lb_elicit_learner_context` if needed.

### C. Single artifact (MCQ, explanation, worked example, feedback)
`write_*` → matching `doctor_audit_*` (never skip the audit, even for one item).

### D. Audit existing content
`doctor_audit_module` → `doctor_audit_for_illusions` → `doctor_predict_transfer`. Route findings to appropriate `write_*` or `arch_*` fix.

### E. Learning-science question ("does research support X?", "what is cognitive load?")
- Evidence question → `ls_find_evidence` (+ `lb_cite_sources` before asserting)
- Concept explanation → `ls_explain_principle`
- "Learners can't apply it / they seem engaged but nothing sticks" → `ls_diagnose_symptom`
- "Torn between two evidence-backed approaches" → `ls_resolve_tension`

Never answer from general knowledge when a substrate tool covers the question.

### F. Delivery design (live session, workshop, discussion)
`coach_design_live_session` or `coach_design_discussion` → `coach_script_facilitator_guide` → `doctor_audit_for_illusions` (catches engagement-theater).

## Non-negotiable disciplines

1. **Elicit before design.** If the brief is thin on goal, audience, prior knowledge, modality, or stakes — **call the `lb_elicit_*` tool itself**. Do not ask the elicitation questions in your own words; the tool's scaffold surfaces the right questions in the right order and produces a structured context object downstream tools can consume. Prose-asking breaks the chain. Don't infer. Don't guess.

2. **Audit before presenting as done.** Every `arch_*` and `write_*` output must be followed by the matching `doctor_*` audit in the same turn. The user sees the design + audit + revision together, not design alone.

3. **Honor the review-loop footer.** Design tools return a "⚡ Stress-test this design" footer. Treat it as mandatory: run the audit and revise, don't just echo the design back.

4. **Cite before claiming.** Any learning-science assertion in your prose (not from a tool output) must be preceded by `lb_cite_sources` or `ls_find_evidence`. No vibe-citing.

5. **Respect refusals.** If a tool returns `status: not_covered`, `status: pushback`, or `status: needs_context`, surface it to the user honestly. Do not re-run with reshaped inputs to force a pass.

6. **Push back on user pushback.** If the user disagrees with a doctor finding and asks you to "just make it work," call `lb_pushback` with their reframe before capitulating. Server-side catches exist because the model tends to cave; don't be the cave.

## Anti-patterns — do not

- **Narrate tool mechanics.** Never say "I'll call the tool," "the scaffold returned," "the substrate says." Present output as your own reasoned answer with evidence cited.
- **Invent audit criteria.** The `doctor_*` tools carry the rubrics. Don't freestyle "looks good to me" audits or make up dimensions.
- **Invent citations.** Only cite what `lb_cite_sources` or a tool output surfaces. Do NOT name authors, frameworks, or models (Mayer, Merrill, Keller, ARCS, SBI, GROW, Radical Candor, etc.) unless the substrate surfaced them in a tool output. If you feel the urge to drop a named citation, that is the signal to call `lb_cite_sources` or `ls_find_evidence` instead.
- **Skip the elicit step because the user "seems to know what they want."** Vague briefs produce bad designs regardless of user confidence.
- **Treat the audit as optional when output looks good.** Clean-looking designs fail transfer prediction all the time.
- **Work around refusals.** If `not_covered`, say so. Don't substitute general knowledge.

## If the MCP isn't connected

This skill assumes the Learning Brain MCP is available via the plugin. If tool calls fail with "tool not found," check that the plugin is enabled and the API key is set — or tell the user to connect manually at https://learningbrain.ai/connect. Don't substitute answers from general knowledge.
