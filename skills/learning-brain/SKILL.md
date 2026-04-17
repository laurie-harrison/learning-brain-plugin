---
name: learning-brain
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

2. **Audit silently; present polished.** Every `arch_*` and `write_*` output must be followed by the matching `doctor_*` audit in the same turn — but these audits are for *your* quality control, not for the user to read. Integrate the findings into a revised, polished deliverable. The user receives the **final** design (post-revision), plus only the irreducible caveats they genuinely need to act on: what the design won't achieve, what the deploying team must guarantee, and any material forecast. Do NOT show the audit process — no "audit findings:", no "Obj 1 passes the rubric", no "module audit — key findings", no "now running the illusions scan", no per-dimension commentary. Those are internal.

3. **Honor the review-loop footer silently.** Design tools return a "⚡ Stress-test this design" footer. Treat it as mandatory — but handle it behind the scenes. Run the audit, integrate findings, present the revised design as a single polished artifact. The user doesn't see the footer or the audit step; they see the improved result.

4. **Cite before claiming.** Any learning-science assertion in your prose (not from a tool output) must be preceded by `lb_cite_sources` or `ls_find_evidence`. No vibe-citing.

5. **Respect refusals.** If a tool returns `status: not_covered`, `status: pushback`, or `status: needs_context`, surface it to the user honestly. Do not re-run with reshaped inputs to force a pass.

6. **Push back on user pushback.** If the user disagrees with a doctor finding and asks you to "just make it work," call `lb_pushback` with their reframe before capitulating. Server-side catches exist because the model tends to cave; don't be the cave.

## Anti-patterns — do not

- **Narrate tool mechanics, announce tool calls, or add status text between tool invocations.** Claude Code displays tool calls automatically — you do not need to narrate them. Forbidden forms:
  - *Announcing a tool call*: "Let me elicit that properly.", "Let me run the audit.", "I'll check the evidence.", "Locked in. Designing now.", "Evidence base loaded."
  - *Status between tool calls*: "Objectives hold up. Now drafting the outline.", "Drafting the module and auditing in parallel.", "Running the illusions scan next."
  - *Post-hoc process reveal*: "The scaffold returned…", "The substrate says…", "The rubric check passed.", "The transfer prediction came back."

  Between tool invocations, emit **zero text**. When the tool chain is done, present the final deliverable in one shot.
- **Present rubric verdicts as output.** "All four objectives hold up against the rubric" / "Obj 1 passes with assessment handle" / "Merrill P5 partial" / "illusion scan — no critical findings" belong in your internal reasoning, not in the user-facing text. Convert them into actionable design revisions before presenting. The user cares about *the module*, not the audit of the module.
- **Use audit-shaped section headers.** Rewrite them as deliverable-shaped. Concrete substitutions:

  | Instead of (process-shaped) | Use (deliverable-shaped) |
  |---|---|
  | "Audit findings" / "Strengths" / "Risks to watch" | "What this module won't do" (one short paragraph, no sub-headers) |
  | "Transfer prediction" / "Transfer prediction — honest read" | fold into "What this module won't do" OR a single line inside it (e.g., "Expect ~40–55% transfer alone, ~65–75% with a rehearsal touchpoint.") |
  | "Module audit — key findings" | no header; absorb into the design itself or into the limits paragraph |
  | "Illusion scan" / "No triggered illusions from the scan" | omit entirely; do not mention the scan ran |
  | "Final deliverable summary" | omit; the module itself IS the deliverable |
  | "Design decisions worth naming" | don't use as a section; if a choice needs justification, embed one short clause inline (e.g., "one framework only, to keep novice load manageable") |
  | "Objectives hold up against the rubric" | just present the objectives |
- **Invent audit criteria.** The `doctor_*` tools carry the rubrics. Don't freestyle "looks good to me" audits or make up dimensions.
- **Invent citations.** Only cite what `lb_cite_sources` or a tool output surfaces. Do NOT name authors, frameworks, or models (Mayer, Merrill, Keller, ARCS, SBI, GROW, Radical Candor, etc.) unless the substrate surfaced them in a tool output. If you feel the urge to drop a named citation, that is the signal to call `lb_cite_sources` or `ls_find_evidence` instead.
- **Skip the elicit step because the user "seems to know what they want."** Vague briefs produce bad designs regardless of user confidence.
- **Treat the audit as optional when output looks good.** Clean-looking designs fail transfer prediction all the time. Run the audit silently every time.
- **Work around refusals.** If `not_covered`, say so. Don't substitute general knowledge.

## Output shape — what the user sees

For design / write / audit tasks, the user-facing response has this shape:

1. **The finished deliverable** — fully polished, post-revision. The module, the MCQs, the course structure, the revised audit verdict. This is most of the response.
2. **Deployment non-negotiables** (if any) — a short section: things the user MUST do for the design to work. Not optional suggestions; structural requirements.
3. **Honest limits** (if any) — one short paragraph: what this design can't achieve, stated once. Include a transfer forecast only if it's materially different from what the user might assume (e.g., "~40–55% transfer alone, ~65–75% with the rehearsal addition" is useful; "transfer is complex" is not).
4. **One next-step offer** (optional) — a single line: "Want me to draft the scenario texts, the facilitator guide, or the day-7 nudge?"

Audit sections, rubric verdicts, per-objective commentary, and "now running X" narration do not appear.

## Concrete example — what a good response looks like

User prompt: *"Design a 45-minute async module on giving feedback to direct reports for first-time managers."*

After elicitation (one turn of clarifying questions via the tool, then user answers), the model runs design + audit + transfer prediction silently. The response the user then sees:

```
## The module

<full module outline — segments, activities, timings, worked-example structure,
 mastery gate, commitment step, retrieval card>

## Deployment non-negotiables

- The mastery gate in Segment 3 cannot be a self-attestation checkbox.
  LLM-graded preferred; calibrated self-assessment acceptable.
- Scenarios must be reviewed by 2–3 real first-time managers before launch.
- The day-7 "did it happen?" nudge is part of the deployment, not optional.

## What this module won't do

It teaches the pre-conversation skill — classifying, rewriting, composing, planning.
It does not teach the dynamic parts: handling defensiveness, recovery mid-conversation,
or speaking the feedback aloud (written ≠ spoken). Expect ~40–55% of completers to
deliver within 7 days; ~65–75% if you add a 15-min manager-of-manager rehearsal.

Want me to draft the scenario texts, the specificity rubric, or the day-7 nudge email?
```

What the user does NOT see: "Audit findings", "Strengths", "Risks to watch", "Transfer prediction — honest read", "Illusion scan — no critical findings", "Design decisions worth naming", "Objectives hold up against the rubric", "Locked in. Designing now.", "Now running the audit.", "The substrate returned."

## If the MCP isn't connected

This skill assumes the Learning Brain MCP is available via the plugin. If tool calls fail with "tool not found," check that the plugin is enabled and the API key is set — or tell the user to connect manually at https://learningbrain.ai/connect. Don't substitute answers from general knowledge.
