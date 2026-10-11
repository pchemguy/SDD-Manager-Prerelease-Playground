---
url: https://chatgpt.com/c/6aafd74d-9d74-83eb-b046-dd4384744e29
---

> **Historical exploration transcript.** This document is retained for provenance and is not authoritative for current behavior or agent instructions. Use [README.md](README.md) and [CAPABILITY-MAP.md](docs/dev/CAPABILITY-MAP.md) for the current plugin and workflow entry points.

## 📗 Architectural Revision

> [!NOTE] Prompt
>  
> Let's proceed by discussing high-level concepts first. I want to 
> 
> 1. convert sdd-man into a plugin and split it into a set of capabilities/skills
> 2. abandon the option of working on non-git projects - the plugin/skills will refuse to modify non-git projects.
> 3. abandon transaction workflow with backup files. Since non-git projects are no longer supported, the checkpoints are simply git commits and the resumption process will reset dirty files in working tree when a reliable resumption of interrupted incomplete task cannot be performed.
> 4. develop additional workflows for architecture and decomposition development before creating the SPEC. I am also thinking about transforming PLAN into a higher-level artifact without the lowest-level execution units. The ROADMAP will be replaced with TASKS to make it more conventional.
> 5. make provisions for robust addition of new capabilities/skills for well-defined workflows (say, creation of GitHub issues and milestones for tasks/milestones/phases from the TASKS)

These changes fit together. The central shift is to make **Git the recovery boundary**, **PLAN the delivery strategy**, and **TASKS the executable work inventory**. The current skill puts task detail in PLAN, repeats its structure in ROADMAP, and maintains a separate transaction record. The revision can give each artifact a clearer job.

| Stage           | Proposed output                                                  | Responsibility                                                                                                                                  |
| --------------- | ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Exploration     | Accepted decisions and open questions                            | Establish the problem, constraints, and intended outcomes.                                                                                      |
| Architecture    | `ARCHITECTURE`                                                   | Define system boundaries, components, interfaces, dependency direction, and important design choices.                                           |
| Decomposition   | Architecture’s component tree, or a separate artifact when large | Refine responsibilities until the system can be specified coherently.                                                                           |
| Specification   | `SPEC`                                                           | State the required behavior, contracts, and acceptance conditions. Architecture informs it; SPEC becomes authoritative for the intended system. |
| Planning        | `PLAN`                                                           | Define implementation strategy, phases, milestones, dependencies, and their exit conditions.                                                    |
| Task derivation | `TASKS`                                                          | Define ordered, verifiable execution units under those milestones, with stable IDs and completion state. This replaces ROADMAP.                 |
| Implementation  | Code, tests, documentation, Git commits                          | Execute a requested range, verify it, report implemented features, and stop for steering.                                                       |

I would keep **phases and milestones canonically defined in PLAN**, with TASKS referencing them. Tasks would exist only in TASKS. That prevents the two documents from becoming competing task lists. LAYOUT can remain the physical ownership view, developed once architecture and contracts give it something concrete to locate.

For the plugin, I suggest a **small set of independently usable skills**, rather than one skill per document or every internal step:

- **Explore and design:** exploration, architecture, and decomposition. These may be one skill initially if users typically move among them in the same conversation.
- **Specify:** create and reconcile the authoritative SPEC.
- **Plan and derive tasks:** create PLAN, then derive and maintain TASKS. These are distinct outputs and could be separate skills.
- **Implement and resume:** discover status, execute bounded tasks, verify, commit, and recover interrupted work.
- **Review and steer:** inspect a checkpoint and make a focused revision or return to design.

Testing selection, reporting, and in-code documentation governance can be shared workflow rules invoked by those skills. They need their own skills only where independent invocation proves useful. This matches the plugin format’s model of multiple skills under one package, while letting each skill retain a clear activation and output. :chatgpt-content-reference{index="0"}

**Git-only recovery needs one explicit safety rule.** Every mutating workflow should verify that the project is in a valid Git worktree. A verified task ends in a commit; its TASKS entry records completion and links to that commit. At startup, the agent compares HEAD, the working tree, TASKS, and the requested range. It continues an interrupted task only when the dirty state can be attributed reliably to it; otherwise it returns to the last trusted commit and starts the task again. The old backup manifests and recovery directories can go. A lightweight journal may still be useful for narrative audit, but it should not be required to reconstruct project state.

The difficult case is **uncommitted user work mixed with interrupted agent work**. I recommend implementing tasks in a dedicated Git worktree. Then an unrecoverable interrupted task can be reset there without discarding changes in the developer’s main worktree. If implementation must also run in a shared worktree, the agent should identify ownership before resetting files; an ambiguous dirty state should block an automatic reset.

For future capabilities, define a narrow **extension contract**: when a capability activates, what authoritative artifacts it reads, what it may write, how it identifies objects across repeated runs, and how it reports drift or partial failure. A GitHub publishing skill could then read stable TASKS IDs and reconcile issues and milestones without making GitHub the source of truth. One plausible mapping is task → issue, milestone → GitHub milestone, phase → label or other grouping; GitHub exposes these as separate issue, milestone, and label facilities. :chatgpt-content-reference{index="1"} Scripts would remain optional for deterministic operations such as validation or synchronization.

The first architectural decision I would settle is: **should a dedicated Git worktree be the default requirement for implementation, or should shared-worktree implementation remain supported with a conservative reset policy?** That choice determines how strong and automatic the new recovery promise can be. I have left the feature branch untouched during this discussion.

---
---

## 📗 Explore and Design

> [!NOTE] Prompt
>  
> Let's focus first on Exploration/Architecture/Decomposition and `Explore and design` skill  Should this skill be called `sdd-design`/`sdd-explore`/`sdd-explore-design` or what? It should produce or update (in docs/dev/) PROJECT.md, which should capture concise project overview, ARCHITECTURE.md, and DECOMPOSITION.md.
> 
> Exploration stage is OK. 
> 
> ARCHITECTURE.md and DECOMPOSITION.md are necessary for from-scratch workflows, and FEATURE_ARCHITECTURE.md (may include feature scope/definition) and FEATURE_DECOMPOSITION.md may be necessary for architectural revisions. ARCHITECTURE.md will need to capture concise project overview and high-level architectural decisions and design, such as major blocks/components (like deterministic core/engine + shell + ...), patterns, etc.. ARCHITECTURE.md should probably include only limited project-specific links. The details shall be developed in DECOMPOSTION.md.

I recommend **`sdd-design`**. It names the outcome of the skill while allowing exploration to remain conversational.

| Name                 | Assessment                                                                                                   |
| -------------------- | ------------------------------------------------------------------------------------------------------------ |
| `sdd-explore`        | Suggests the skill stops before producing design documents.                                                  |
| `sdd-explore-design` | Accurate, but cumbersome to invoke and narrow if the skill is later used to revise an existing architecture. |
| **`sdd-design`**     | Covers exploration, initial design, and architectural revision without implying that it writes code or SPEC. |

Its description should make the boundary explicit: _explore a software project, develop or revise its architecture and decomposition, and maintain the pre-specification design documents._

### Document responsibilities

| Document                    | Canonical content                                                                                                                                                               |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `docs/dev/PROJECT.md`       | Concise project brief: purpose, users, problem, desired outcomes, scope, key constraints, and terms needed to orient a reader.                                                  |
| `docs/dev/ARCHITECTURE.md`  | Concise system design: major blocks, their relationships and dependency direction, selected patterns, system-wide design principles, and the reasons for consequential choices. |
| `docs/dev/DECOMPOSITION.md` | Detailed breakdown of those blocks: responsibilities, boundaries, collaborations, interfaces needing definition, and how components subdivide.                                  |

I would keep the project overview **canonical in PROJECT.md**. ARCHITECTURE.md can open with a two- or three-sentence orientation and link to PROJECT.md, then concentrate on design. That avoids maintaining two slightly different descriptions of the project.

Your proposed boundary for ARCHITECTURE.md is sound. For example, it might establish a deterministic core, an I/O shell, and an adapter layer, explain why those boundaries exist, and show their permitted dependency direction. DECOMPOSITION.md would then identify the components within each block, what each owns, and where their interactions occur. It should be allowed to grow into focused child documents if a single file becomes unwieldy. ARCHITECTURE.md needs only a small set of navigation links to those children and other governing documents.

**DECOMPOSITION is still design, rather than an early PLAN.** It answers “what parts does this system consist of, and what does each part own?” SPEC subsequently defines their required behavior and contracts; LAYOUT assigns physical locations; PLAN determines construction order; TASKS defines execution units. Exploration can revisit architecture when decomposition exposes a weak boundary. Document production need not force a one-way sequence.

### Initial work and revisions

For a from-scratch project, `sdd-design` would produce or update all three documents before SPEC authoring. For an existing project, it would inspect the actual system first and revise only the documents supported by the requested scope.

For a material feature or architectural revision, `FEATURE_ARCHITECTURE.md` can state the feature’s scope and the **proposed changes to the system design**. `FEATURE_DECOMPOSITION.md` can detail affected components and relationships. They should describe the delta, with unchanged parts referenced rather than copied. Once the revision is accepted and implemented, the main architecture and decomposition should describe the resulting system directly; Git preserves the history.

There is one existing convention we must deliberately change: the current sdd-man reads `docs/dev/PROJECT.md` as a **project instruction file**. Under this proposal it becomes a **project overview and design input**. I recommend keeping operational instructions in `AGENTS.md` or another explicitly designated instruction file, and removing the special instruction authority currently assigned to PROJECT.md. Otherwise the new documents would have an ambiguous precedence relationship.

The question I would settle next is whether **DECOMPOSITION.md may define provisional component interfaces**, leaving precise behavioral contracts to SPEC. I recommend yes: it should capture enough interaction detail to test the architecture for coherence, while clearly marking contract details that SPEC must resolve.

---
---

## 📗 Explore and Design Refine

> [!NOTE] Prompt
>  
> Everything is accepted. Both ARCHITECTURE.md and DECOMPOSITION.md should be allowed to use focused children, when appropriate.
> 
> Before we proceed to creation of the `sdd-design` skill, I need to clarify how shared capabilities are managed within the plugin. None of the focused workflow capabilities shall integrate common/shared capabilities. Say, agent repo orientation should occur before any change to the repo occurs. At least the orchestrating agent must orient itself, for subagents workflows might vary, which is ok as orchestrating agent should include the necessary boundaries in subagent context. Orientation shall include, among other things, reading key governing repo docs, verifying availability of git, worktree status, and so on.

Agreed: both `ARCHITECTURE.md` and `DECOMPOSITION.md` may become compact parent documents with focused children. The parent owns the system-wide relationships; each child owns its detailed scope.

For shared capabilities, I recommend a **coordinator and focused skills**:

| Role                 | Responsibility                                                                                                                                                                                        |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `sdd-manage`         | Own the lifecycle, authorization boundary, requested work range, and handoffs between skills.                                                                                                         |
| `sdd-orient`         | Inspect the repository and return a concise, evidence-based context: governing instructions and documents, Git repository and branch, HEAD, worktree state, active changes, and relevant constraints. |
| `sdd-design`         | Conduct exploration and develop PROJECT, ARCHITECTURE, and DECOMPOSITION. It owns the design method and outputs, not repository orientation.                                                          |
| Later focused skills | Own specification, planning, task derivation, implementation, steering, and other distinct workflows.                                                                                                 |

For a requested repository change, the coordinator would **orient first, select the focused workflow, then verify the result and state before committing or reporting completion**. It would pass the relevant orientation findings and authority boundaries to any subagent. A subagent may inspect more within its assignment; the coordinator remains responsible for resolving conflicts and checking the final repository state.

A focused skill needs a small **entry condition**, but should not reimplement the shared capability: “Repository mutations require a current orientation result showing a valid Git worktree and identifying applicable instructions.” If that condition is missing or stale, it returns control to the coordinator for orientation. Exploration can still proceed conversationally without modifying files. On a non-Git project, orientation can report findings, but the coordinator refuses repository mutation.

One portability limit matters here: a plugin packages discoverable skills, but the format does not enforce a global _run this skill first_ hook. The ordering is therefore a rule of the `sdd-manage` workflow, backed by entry checks in focused skills. We should document direct invocation accordingly: users can invoke `sdd-design` for discussion, while its document-writing path requires orchestration and a current orientation result. This keeps shared behavior in one place without pretending the plugin format supplies automatic interception.

I would make **coordinated entry mandatory for all repository mutations**. That is the cleanest way to meet your requirement that focused workflows never absorb common capabilities.

---
---

## 📗 Repo Orientation Skill

> [!NOTE] Prompt
>
> Yes, this makes sense. When a particular skill requires a shared capability, it can reference it, establishing prereqs or something, ensuring the mandatory steps are obeyed. Plus we will have `sdd-manage`. But should probably be defined later. You probably have sufficient info to create plugin skeleton in the feature branch and the first `sdd-orient` skill. If there are some extra questions needs to be discussed first, let's do it. Otherwise proceed and also review the saved V1 snapshot to make sure that everything important for the old design is included.

Created and pushed the first plugin increment on `feature/architecture-revision` (`1a5831c`).

The package now has a plugin.json and a read-only SKILL.md. Orientation checks the project root, applicable instructions, development documents, Git worktree and dirty state, then produces a scoped handoff. It marks non-Git projects ineligible for repository mutation. It also recognizes that a V1 `PROJECT.md` may contain instructions, which must remain applicable until explicitly migrated to an instruction source.

The V1-MIGRATION.md accounts for all eleven old workflow references and the templates, distinguishing retained capabilities from the backup and non-Git workflows being retired. `sdd-manage` and `sdd-design` remain future work; the current package does not claim to orchestrate mutations.

Plugin and skill structural validation passed. Clean, dirty, and non-Git inspection examples behaved as expected. These checks validate the package and its Git inspection commands; they do not establish that a client has installed or invoked the skill.

---
---

## 📗 SDD Conventions Explore

> [!NOTE] Prompt
>
> The next is probably another shared capability, `sdd-conventions`. We could start it with something in line
> 
> ```
> - Break the system into smaller units that each have one clear purpose, communicate through well-defined interfaces, and can be understood and tested independently
> - For each unit, you should be able to answer: what does it do, how do you use it, and what does it depend on?
> - Can someone understand what a unit does without reading its internals? Can you change the internals without breaking consumers? If not, the boundaries need work.
> - Smaller, well-bounded units are also easier for you to work with - you reason better about code you can hold in context at once, and your edits are more reliable when files are focused. When a file grows large, that's often a signal that it's doing too much.
> ```
> 
> Basically, proper decomposition (in general sense) should be considered at all design stages, starting from architecture and al the way to the `TASKS.md`. The objective is to have modular decoupled design ,which can be tested and evolved in a robust fashion. Most non-architectural mutation/refactor/evolve jobs should be decomposable into well-defined tasks mutating one code module (ideally) or very few at a time with no or localized expected breaks (until the job is complete).
> 
> This capability should probably also introduce LAYOUT.md and its organization. Inspect the saved V1 snapshot and suggest other additions. At the same, we want to keep this capability from blowing it up unnecessarily with stage-specific conventions.

Yes. I would make `sdd-conventions` a **shared set of structural rules** that other skills reference, with decomposition as its central concern. The same questions should apply to a system block, component, specification section, delivery increment, or task: what does it own, how is it used, and what does it depend on?

Your four points are a strong core. From the V1 snapshot, I would add five compact rules:

1. **One clear owner per concern.** A parent explains scope and relationships; a child owns its detail. Avoid repeating authoritative content across documents or components.
2. **Make dependency direction explicit.** Identify consumers and dependencies, challenge cycles, and resolve unclear ownership before building further work on it.
3. **Keep boundaries observable.** Specify what a unit provides, what it requires, and how its contract can be verified without inspecting its internals.
4. **Split for cohesion, not size alone.** A large file is a prompt to inspect responsibilities, not an automatic reason to split. A useful split gives each resulting unit an independent purpose.
5. **Decompose changes into verifiable increments.** Prefer tasks that affect one module or a few closely related modules, including their tests and documentation. Where a contract change crosses many consumers, use ordered compatibility steps so intermediate states remain coherent.

That last point should be a **preference, not a hard one-module limit**. A public interface change may properly require coordinated edits to its implementation, consumers, tests, and documentation within one bounded task.

### LAYOUT ownership

The V1 layout rules have useful material: physical ownership of source, tests, documentation, fixtures, generated files, and packaging; dependency constraints enforced by placement; and focused children organized by physical domain. I would retain those ideas under **`docs/dev/LAYOUT.md`**, using the capitalization you propose. Its root would give a compact repository map and shared placement rules. Children such as `layout/source.md`, `layout/tests.md`, or `layout/documentation.md` would appear only when those areas have enough independent detail. It should map logical components to locations without repeating ARCHITECTURE or DECOMPOSITION.

To keep `sdd-conventions` small, I recommend that it **define the rules and the LAYOUT document contract**, while a later focused layout workflow creates and maintains the project’s actual LAYOUT files. That preserves its role as a prerequisite across stages instead of turning it into a document-authoring skill. The coordinator can invoke the layout workflow when design has enough detail to assign physical ownership and again when that ownership changes.

The resulting skill could be short: a core decomposition checklist, rules for dependency and change boundaries, and one focused reference for LAYOUT’s ownership and organization. It need not contain separate architecture, SPEC, PLAN, and TASKS procedures. The repository is unchanged; the current capability map still uses lowercase `layout.md` and would be updated when this decision is implemented.

---
---

## 📗 SDD Conventions

> [!NOTE] Prompt
> 
> Accepted. `layout.md`, perhaps, should remain lower case as a supporting shared artifact as opposed to SPEC or PLAN. Proceed to `sdd-conventions`.

Added SKILL.md to the plugin. It gives architecture, components, documents, and tasks the same cohesion, interface, dependency, and verifiability checks. A focused layout-governance.md defines `docs/dev/layout.md` as the supporting physical ownership map; authoring that project document remains a separate workflow.

The CAPABILITY-MAP.md and plugin metadata are updated. Structural validation passes for both skills. Committed and pushed as `dca5eba`.

---
---

## 📗 SDD Conventions Refine

> [!NOTE] Prompt
> 
> I was wrong - layout is completely out of place here. I expect from you critical help as well, helping catch my mistakes earlier reducing the need for revisions. Well, remove layout from `sdd-conventions`. Also, its scope must not be limited to structural/decomposition. It should be more extendable. Design decomposition is a shared major concern I have identified so far, but other aspects mat be added later. You cannot define indefinite scope, but it would be nice to clearly hint to possible future expansion.

You were right; I should have flagged the ownership mismatch earlier. I removed layout governance from SKILL.md. Its first focused module is now decomposition.md.

The skill can grow, but a new convention must apply across workflows without taking ownership of an artifact or operational workflow. `layout.md` remains separately owned in the CAPABILITY-MAP.md.

Plugin validation passes. The correction is committed and pushed as `4986a80`.

---
---

## 📗 Greenfield vs Brownfield

> [!NOTE] Prompt
> 
> Now, what do I do with greenfield vs brownfield? Does it concern skills other than `sdd-manage` and `sdd-design`? Should it be defined as part of `sdd-manage` ?

Greenfield versus brownfield should be a **project-context classification**, owned by `sdd-manage`, rather than two separate versions of every skill.

|Capability|Responsibility|
|---|---|
|`sdd-orient`|Report evidence: existing code, documents, tests, Git history, active changes, and applicable instructions. It does not decide the workflow.|
|`sdd-manage`|Classify the **requested scope** and route the work. A repository can contain both a new component and established components.|
|`sdd-design`|Use that context: design a new system from first principles, or inspect existing boundaries and define a coherent change to them.|
|SPEC, PLAN, TASKS, implementation, verification|Apply their own narrow differences where the context actually changes their work.|
|`sdd-conventions`|Apply the same decomposition criteria in either context.|

I would define three useful contexts in `sdd-manage`:

1. **New system:** no implemented baseline for the requested system. Develop its complete intended design and build path.
2. **Existing system, new capability:** establish the relevant current baseline and define the intended delta, including affected contracts and dependents.
3. **Existing system, correction or restructuring:** establish current behavior and the desired invariant, then determine whether the change requires architectural design or can proceed as bounded corrective work.

This matters beyond `sdd-design`. For example, verification of existing work needs to identify pre-existing failures; implementation needs to protect existing consumers; and recovery needs to distinguish interrupted agent work from unrelated changes. Those skills should contain only their **own context-dependent procedure**. `sdd-manage` owns the classification and handoff, so each skill does not invent a different definition of “brownfield.”

I would avoid making “greenfield” a permanent repository label. A new subsystem inside an established repository may need from-scratch design while still inheriting repository instructions, interfaces, and tests. The coordinator should classify the **work boundary**, record the evidence and assumptions behind it, and revisit the classification if inspection changes the picture.

---
---

## 📗 Explore and Design Context

> [!NOTE] Prompt
> 
> `sdd-manage` is a later concern. What else capabilities should be defined before `sdd-design`?

**No additional skill is required before `sdd-design`.** `sdd-orient` supplies repository evidence, and `sdd-conventions` supplies the decomposition criteria. Exploration, architectural decisions, and the PROJECT/ARCHITECTURE/DECOMPOSITION document workflow belong inside `sdd-design`.

One **entry contract** does need to be stated before we write it:

- Discussion and read-only design can start directly.
- Writing project documents requires an explicit document-authoring request, a current `sdd-orient` handoff confirming an eligible Git worktree, and applicable instructions.
- `sdd-design` references those prerequisites and `sdd-conventions`; it does not reimplement them.
- Until `sdd-manage` exists, the invoking agent coordinates that handoff. The later coordinator skill will formalize the same boundary.

Layout authoring, verification, reporting, and implementation recovery need not block `sdd-design`; each has a separate owner. This lets us build the design skill next without giving it provisional responsibilities we would have to remove later.

---
---

## 📗 Explore and Design

> [!NOTE] Prompt
> 
> Proceed to `sdd-design`. Exploration, architecture and, decomposition should probably be separate progressively loaded sub-workflows.

Added SKILL.md with three progressively loaded sub-workflows: exploration.md, architecture.md, and decomposition.md.

Exploration remains conversational. Project document changes require a requested authoring step and a current Git-eligible `sdd-orient` handoff. Architecture and decomposition each support focused children and scoped feature changes without taking over SPEC, PLAN, or layout ownership.

Plugin validation and reference-routing checks passed. Committed and pushed as `3096f8c`.
