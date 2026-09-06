# DECISIONS

## 2026-09-03 — repository scope and project-memory role

**Decision:** Use one repository, `xgo-ai-lab`, as the shared implementation memory for XGO bring-up, later AI integration, future sensor/software upgrades, and eventual coordination with the legacy robot arm.

The repository is the primary handoff surface between ChatGPT, Codex, Grok, Copilot, Local GPU Helper and future coding agents. Relevant implementation state, experiments, hardware facts, sources, ideas, decisions and dated progress must be captured in the repository rather than left only in chat history.

**Reason:** Avoid fragmented chat-only knowledge and allow another tool/agent to continue from repository state alone.

## 2026-09-03 — ideas are documented separately from commitments

**Decision:** Keep speculative upgrades and brainstorms in `docs/IDEAS.md`. Do not silently promote them to current work or architectural decisions.

**Reason:** The project will accumulate camera, AI, child-interface, robot-arm and hardware-upgrade concepts. Separating ideas from current state prevents overparallelization while preserving useful thoughts.

## 2026-09-03 — firmware rewrite is allowed, but only for verified hardware

**Decision:** Tamás explicitly approved replacing old firmware/software if useful. Firmware may be flashed only after the target MCU/board and the intended image are identified well enough to avoid cross-generation flashing.

## 2026-09-03 — back up SD content before K210 flashing

**Decision:** Before intentionally reflashing the K210, inspect and copy the installed microSD contents if the card is readable.

This remains a historical fallback rule only; K210 recovery is no longer the preferred project path after the vendor-supported ESP32 retrofit became available.

## 2026-09-03 — historical XgoAI repository is a recovery candidate, not a trusted vendor image

**Decision:** Use `geluu/XgoAI` and its forks as historical technical evidence and a recovery candidate, but do not treat the `.kfpkg` as verified official firmware.

## 2026-09-03 — passive discovery before xgolib

**Decision:** Do not instantiate the current upstream `XGO_DOG`/`XGO()` library merely to identify the old hardware.

This applies to the legacy board diagnosis. Once the replacement ESP32 board is installed and its firmware/profile is known, use the vendor-provided initialization/mapping.

## 2026-09-03 — COM3 treated as K210-side (superseded 2026-09-05)

**Decision at the time:** Treat `COM3` as the K210/AI-module USB-UART path.

**Superseded:** COM3 ownership on the old electronics is unresolved and no longer worth prioritizing unless legacy-board investigation resumes.

## 2026-09-05 — power-path diagnosis precedes board/firmware replacement (superseded 2026-09-06)

**Decision at the time:** Do not replace the STM32 board while the battery/power path is still unmeasured.

**Superseded:** after vendor correspondence on 2026-09-06, a supported ESP32 replacement board became available and is now the preferred recovery strategy. Additional component-level diagnosis of the old power path is not currently worth the time unless the retrofit becomes unavailable.

## 2026-09-05 — `G CLK DIO 3V3` is a connector label, not a proven test point

**Decision:** Treat the adjacent populated 4-pin connector as a likely STM32 SWD interface only after electrical verification.

This remains true for archival/reverse-engineering work on the old board.

## 2026-09-06 — vendor-supported ESP32 retrofit is the preferred recovery path

**Decision:** Prefer the official Luwu/XGO **ESP32 replacement driver board** over further repair of the unsupported 2021 STM32 V2.5 board.

**Vendor-confirmed facts:**

- replacement board is designed for the original XGO-Mini chassis;
- original 12 servos remain compatible;
- board uses the standardized XGO serial command set;
- standard motion/pose/kinematics are compatible with `xgolib`;
- board exposes 3.3 V TTL UART for Raspberry Pi/SBC/PC control;
- vendor will provide exact firmware/profile and command mapping with the board;
- current Lite3/CM5 integrated modules and robotic arms are not plug-and-play on the original chassis.

**Reason:** This preserves the expensive/useful mechanical platform and servos while moving the motion controller to a currently supported, programmable architecture.

## 2026-09-06 — preserve mechanics and servos; modernize electronics above the motion layer

**Decision:** Target architecture is:

`original aluminum chassis + original 12 servos + vendor ESP32 motion controller + custom modern upper compute/HMI`.

**Reason:** This is the lowest-cost path to a reliable, maintainable educational/research platform without purchasing a complete newer XGO robot.

## 2026-09-06 — old K210 HMI is optional, not a design dependency

**Decision:** Do not design the revived robot around the legacy K210 display/camera module.

If it works with the replacement board, it may be used temporarily. Long-term preference is a simple modern SBC + inexpensive display + camera.

**Reason:** avoids legacy firmware constraints and gives full control over UI, vision, networking and AI integration.

## 2026-09-06 — battery kit can be optimized only after retrofit power requirements are known

**Decision:** The quoted USD 75 board + battery kit is acceptable as a baseline. Do not remove the battery from the order unless the vendor confirms the replacement board accepts a standard locally sourced 2S 18650 arrangement without a specific pack/BMS/connector requirement.

**Reason:** locally sourced 18650 cells may be cheaper, but the first objective is a known-good supported retrofit.

## 2026-09-06 — current-generation robot arm remains a future custom integration, not a retrofit assumption

**Decision:** Do not assume the current Lite3/mini2 robotic arm can be attached directly to this chassis.

**Reason:** vendor explicitly states current arm/head modules are tailored to newer chassis generations. Future manipulation work can use a custom arm/gripper or the separate legacy university robot arm after locomotion is stable.

## 2026-09-03 — robot arm remains separate initially

**Decision:** Treat the legacy university robot arm as an independent station rather than mounting it on the XGO initially.

**Reason:** independent bring-up reduces mechanical, power and control complexity. Coordinated tasks can be implemented at the software layer after both devices are stable.
