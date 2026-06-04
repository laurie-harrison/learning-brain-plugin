---
name: learning-brain-elt
description: Orchestrates ELT Brain (25 tools: 9 shared + 16 ELT-specific) for English Language Teaching design, writing, audit, assessment-item drafting, corrective feedback, language syllabus design, and synchronous-session support. Use whenever the user wants to design or audit ELT lessons, vocabulary sets, reading/listening/grammar/speaking tasks, language syllabi, exam items, performance evaluations, corrective feedback, classroom activities, learner-affect interventions, or asks SLA / materials-design evidence questions. Enforces CEFR-aware elicitation, input-quality audit before design, audit-always, and review-loop discipline.
---

# ELT Brain - Codex Workflow Discipline

ELT Brain is the ELT sibling of Learning Brain. It exposes a curated SLA and materials-design MCP surface at `https://eltbrain.com/mcp`. The tools are strong; the failure mode is how they get sequenced. This skill is the glue that makes Codex behave like a careful ELT collaborator instead of a generic text generator.

Present ELT Brain outputs as finished expertise. Do not narrate tool calls, scaffold mechanics, raw rubrics, or internal review steps unless the user explicitly asked for an audit and the audit itself is the deliverable.

If tool calls fail with "tool not found", check that the `learning-brain-elt` MCP server from the plugin is enabled and authenticated. If it is not connected, tell the user to connect it at `https://eltbrain.com/connect`. Do not substitute general SLA knowledge.

## Product Boundary

Use `learning-brain-elt` for English Language Teaching, second-language acquisition, language materials writing, CEFR/ACTFL alignment, ELT exams, coursebook pages, teacher-training, EAP/ESP/ESOL/EAL/CLIL/EMI, and language-classroom delivery.

Use `learning-brain` instead for corporate L&D, general instructional design, manager training, compliance, workplace learning, and non-language course design.

## Tool Families

- `lb_*` - elicitation, pushback, worked examples, citations
- `ls_*` - evidence lookup, principle explanation, symptom diagnosis, tension resolution
- `arch_*` - ELT lesson design and language syllabus architecture
- `write_*` - vocabulary, reading, listening, grammar, speaking, clarification, performance evaluation, corrective feedback, exam items
- `doctor_*` - input-quality and exam-item audits
- `coach_*` - speaking sessions, classroom activity management, learner affect

The full schema comes from the MCP manifest. Do not re-enumerate all arguments to the user.

## Required ELT Context

Before design or writing, make sure the brief includes:

- `cefr_level`: pre-A1, A1, A2, B1, B2, C1, C2, or mixed
- `target_skill_focus`: integrated, reading, listening, writing, speaking, vocabulary, grammar, pronunciation, exam, or syllabus
- `instructional_setting`: EFL, ESL, EAP, ESP, business-English, young-learners, exam-prep, general-English, EAL, ESOL, CLIL, EMI, or similar

Usually useful:

- `l1_or_l1_group`
- `exam_target`
- `target_use_context`
- `class_size_and_mode`
- `age_band`

If these fields are missing, call `lb_elicit_learner_context`. Do not infer "intermediate" as B1. Do not prose-ask your own questions when the tool can produce a structured context object.

## Task Shapes

### A. ELT lesson or lesson-with-materials

1. `lb_elicit_learner_context` if CEFR, skill focus, or setting is missing
2. If the user supplies a text, dialogue, audio script, exercise, or coursebook page, call `doctor_audit_for_input_quality` before designing around it
3. `arch_design_elt_lesson`
4. Call the relevant writer tools for the lesson stages: `write_vocabulary_set`, `write_reading_task`, `write_listening_task`, `write_grammar_practice_set`, `write_speaking_task`
5. Follow every `suggested_next_steps` audit/review instruction before presenting the final material

### B. Single ELT artifact

Use `lb_elicit_learner_context` if needed, then the matching writer:

- vocabulary set -> `write_vocabulary_set`
- reading task -> `write_reading_task`
- listening task -> `write_listening_task`
- grammar practice -> `write_grammar_practice_set`
- speaking task -> `write_speaking_task`
- teacher language explanation -> `write_language_clarification`
- learner performance evaluation -> `write_performance_evaluation`
- corrective feedback -> `write_corrective_feedback`
- exam item -> `write_exam_item`

Then run the suggested audit/review steps before presenting, except when the user explicitly only asked for a draft and wants no review.

### C. Audit supplied ELT material

If the user asks for review, audit, evaluation, red flags, or improvement suggestions for a supplied ELT text, dialogue, exercise, script, page, or lesson:

1. Call `doctor_audit_for_input_quality`
2. Present the audit as the deliverable: verdict, flags, severity, location, rationale, suggested revision, and revision priority

If the material is an exam item, use `doctor_audit_exam_item` instead.

### D. Language syllabus

For multi-lesson or course-level language progression, call `arch_design_language_syllabus`. Keep the output tied to CEFR level, target use context, recycling, assessment evidence, and realistic teacher workload.

### E. Classroom delivery and affect

- speaking-focused live session -> `coach_design_speaking_session`
- activity setup, monitoring, transition, grouping, timing -> `coach_manage_classroom_activity`
- anxiety, willingness to communicate, confidence, trauma-informed or affective support -> `coach_support_learner_affect`

### F. SLA or materials-design question

- evidence verdict -> `ls_find_evidence`
- concept explanation -> `ls_explain_principle`
- observed learner problem -> `ls_diagnose_symptom`
- contested design choice -> `ls_resolve_tension`

Call `lb_cite_sources` before making named research claims in your own prose.

## Non-Negotiable Discipline

1. Elicit context before design.
2. Audit supplied input before designing around it.
3. Honor `suggested_next_steps` as mandatory quality control.
4. Cite before claiming.
5. Respect refusals and pushback. Do not reshape inputs just to force a pass.
6. Use the ELT tool for ELT work and the core Learning Brain tool for non-ELT work.

## Do Not

- Do not narrate tool calls: no "I will run the audit now", "the scaffold returned", or "rubric passed".
- Do not show internal audit results for design tasks. Revise the deliverable and show the final version.
- Do not invent SLA citations, CEFR claims, word-list claims, or exam-spec details.
- Do not treat "discussion prompt" as a speaking task unless there is a real communicative gap and outcome.
- Do not design around supplied input that failed the input-quality audit without naming the problem.
- Do not answer from general knowledge when the MCP substrate covers the question.

## User-Facing Output

For design/writing tasks, show:

1. The finished deliverable
2. Teaching or deployment non-negotiables, if any
3. Honest scope limits, if material
4. One useful next-step offer

For audit tasks, show:

1. Overall verdict
2. Flags with location, severity, rationale, and suggested revision
3. Revision priority order
4. One useful next-step offer

When the user asks what ELT Brain can do, answer in outcomes, not tool names: lesson skeletons, vocabulary sets, reading/listening tasks, graded grammar practice, speaking tasks, syllabus architecture, exam-item drafting and auditing, input-quality audits, corrective feedback, performance evaluations, classroom activity support, learner-affect support, and evidence-backed SLA/materials-design answers.
