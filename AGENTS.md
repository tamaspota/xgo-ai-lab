# AGENTS.md

## Purpose

This repository is the shared implementation memory for the XGO AI Lab project.

## Mandatory reading order

Before changing code or documentation, read:

1. `AGENTS.md`
2. `docs/CURRENT_STATE.md`
3. `docs/DECISIONS.md`
4. latest relevant `logs/session_YYYY-MM-DD.md`
5. task-specific source files

## Primary objective

Bring an original Kickstarter-era XGO-Mini back into useful service safely, then expose it through a maintainable Python control layer. Later integration may include voice/vision AI, Local GPU Helper, and a separate legacy robot arm.

## Safety rules

- Fail closed when hardware identity, protocol semantics or stop behavior are uncertain.
- Do not flash firmware unless Tamás explicitly approves it.
- Do not send motion commands during passive discovery.
- Do not assume current upstream libraries are behaviorally safe for old hardware.
- Inspect upstream source before using constructors or helpers that may command movement.
- Prefer read-only diagnostics before state-changing tests.
- Any motion test must define a stop/recovery action first.

## Engineering rules

- Prefer simple Python and pyserial-compatible tooling.
- Keep platform-specific code isolated.
- Do not add cloud dependencies for basic robot control.
- Keep the XGO and legacy robot arm as separate devices until both are independently stable.
- Record verified hardware facts in `docs/HARDWARE.md`.
- Record architectural or safety decisions in `docs/DECISIONS.md`.
- Update `docs/CURRENT_STATE.md` after material progress.
- Append a dated session log for each meaningful hardware/software session.

## Current upstream reference

Official current control library reviewed on 2026-09-03:

- repository: `LuwuDynamics/xgo_doglib`
- reviewed commit: `cf72514273dc703284d3c47e46c67ce238caae11`
- current package factory defaults to 115200 baud and supports `xgomini`
- current `XGO_DOG` initialization invokes `reset()`, so it must not be used for the initial passive discovery step

## Completion criteria for first milestone

Milestone 1 is complete only when:

- Windows COM/device identity is recorded;
- connection method is understood;
- exact or best-supported XGO hardware/firmware identity is recorded;
- a read-only or otherwise non-motion communication path is proven;
- no firmware update was needed.
