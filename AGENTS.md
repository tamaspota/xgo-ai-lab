# AGENTS.md

## Purpose

This repository is the shared implementation memory for the XGO AI Lab project and the handoff surface between ChatGPT, Codex, Grok, Copilot, Local GPU Helper and future coding agents.

The repository must remain sufficient to continue the engineering work without relying on prior chat history.

## Mandatory reading order

Before changing code or documentation, read:

1. `AGENTS.md`
2. `docs/CURRENT_STATE.md`
3. `docs/DECISIONS.md`
4. latest relevant `logs/session_YYYY-MM-DD.md`
5. `docs/IDEAS.md` when planning future features/upgrades
6. `docs/RECOVERY_SOURCES.md` when working on firmware/recovery
7. task-specific source files

## Primary objective

Bring an original Kickstarter-era XGO-Mini back into useful service safely, then expose it through a maintainable Python control layer. Extend the existing platform where practical rather than replacing it by default. Later integration may include voice/vision AI, Local GPU Helper, child-friendly controls, upgraded sensing and a separate legacy robot arm.

## Documentation model

Keep different information classes separate:

- `docs/CURRENT_STATE.md` — verified current status, blocker and next concrete action;
- `docs/DECISIONS.md` — confirmed architectural/safety choices and their reasons;
- `docs/IDEAS.md` — brainstorms, candidate upgrades and future experiments that are **not commitments**;
- `docs/HARDWARE.md` — verified hardware facts, interfaces and measurements;
- `docs/RECOVERY_SOURCES.md` — external firmware/software references with provenance and confidence;
- `docs/FACTORY_SELF_TEST.md` — repeatable stock-hardware test procedure;
- `logs/session_YYYY-MM-DD.md` — dated engineering history, commands, observations, modified files and unfinished work.

When Tamás supplies a useful service, repository, manual, firmware source or hardware detail, put it in the appropriate repository document if it materially affects the project. Do not promote casual brainstorming into a decision or active task; capture it in `docs/IDEAS.md` instead.

## Safety rules

- Fail closed when hardware identity, protocol semantics or stop behavior are uncertain.
- Tamás has approved replacing old software/firmware, but only use images verified for the actual controller generation.
- Never flash current ESP32 XGO-Mini lower-board firmware onto the original STM32 board.
- Back up readable SD content before intentionally reflashing the K210.
- Do not send motion commands during passive discovery.
- Do not assume current upstream libraries are behaviorally safe for old hardware.
- Inspect upstream source before using constructors or helpers that may command movement.
- Prefer read-only diagnostics before state-changing tests.
- Any motion test must define a stop/recovery action first.

## Engineering rules

- Prefer simple Python and pyserial-compatible tooling.
- Keep platform-specific code isolated.
- Do not add cloud dependencies for basic robot control.
- Prefer existing hardware and compute before recommending another robotics platform.
- Keep the XGO and legacy robot arm as separate devices until both are independently stable.
- Record verified hardware facts in `docs/HARDWARE.md`.
- Record architectural or safety decisions in `docs/DECISIONS.md`.
- Record uncommitted feature/upgrade concepts in `docs/IDEAS.md`.
- Record external recovery references and provenance in `docs/RECOVERY_SOURCES.md`.
- Update `docs/CURRENT_STATE.md` after material progress.
- Append a dated session log for each meaningful hardware/software session.
- Keep unfinished/blocked work explicit; do not imply tests passed unless evidence was observed.

## Hardware generation

Current verified working model for this robot:

- original 2021 XGO-Mini;
- high-level/AI board: Kendryte K210;
- motion controller: STM32;
- Windows-visible CP2102 interface: COM3, treated as K210-side until proven otherwise;
- direct STM32 motion protocol: internal 3.3 V TTL/UART path documented by the original protocol.

## Software references

Current official control library reviewed on 2026-09-03:

- `LuwuDynamics/xgo_doglib`, commit `cf72514273dc703284d3c47e46c67ce238caae11`;
- current package defaults to 115200 and supports logical `xgomini`;
- current `XGO_DOG` initialization invokes `reset()`, so do not use it merely for hardware identification.

Historical recovery candidate:

- `geluu/XgoAI` plus preserved forks;
- contains a dated 2021 K210 `.kfpkg` and SD application tree;
- useful evidence, but not yet verified as an official vendor firmware source.

## Completion criteria for first recovery milestone

Milestone 1 is complete when:

- Windows COM/device identity is recorded;
- K210 USB/programming path behavior is understood;
- installed SD state is inspected/backed up or deliberately declared unrecoverable;
- a known-good K210 execution path is established (existing software, restored SD, or verified reflash);
- STM32 motion-controller access path is identified without cross-generation flashing;
- the next motion test has an explicit stop/recovery path.
