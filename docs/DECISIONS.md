# DECISIONS

## 2026-09-03 — repository scope

**Decision:** Use one repository, `xgo-ai-lab`, as the shared implementation memory for XGO bring-up, later AI integration, and eventual coordination with the legacy robot arm.

**Reason:** Avoid fragmented chat-only knowledge and allow multiple coding agents/tools to work from the same current state.

## 2026-09-03 — firmware rewrite is allowed, but only for verified hardware

**Decision:** Tamás explicitly approved replacing old firmware/software if useful. Firmware may be flashed only after the target MCU/board and the intended image are identified well enough to avoid cross-generation flashing.

**Reason:** The original 2021 XGO-Mini is **K210 + STM32**, while current XGO-Mini lower-board material includes ESP32-based hardware.

**Practical consequence:**

- K210 software/firmware may be replaced after its recovery path is verified.
- STM32 firmware may be replaced only with an original-generation-compatible image/tooling.
- Never flash current ESP32 M-series lower-board firmware onto this original STM32 board.

## 2026-09-03 — back up SD content before K210 flashing

**Decision:** Before intentionally reflashing the K210, inspect and copy the installed microSD contents if the card is readable.

**Reason:** The historical K210 application is heavily SD-based (`main.py`, demos, models/assets, user program files). A missing or damaged SD tree could explain broken behavior without requiring a flash rewrite, and a backup gives a cheap rollback path.

## 2026-09-03 — historical XgoAI repository is a recovery candidate, not a trusted vendor image

**Decision:** Use `geluu/XgoAI` and its forks as historical technical evidence and a recovery candidate, but do not treat the `.kfpkg` as verified official firmware until provenance and board compatibility are checked.

**Reason:** The repository contents strongly match the 2021 K210 XGO generation, including a dated 2021 K210 firmware package and SD application tree, but the repository is not currently verified as an official Luwu/XGO vendor source.

## 2026-09-03 — passive discovery before xgolib

**Decision:** Do not instantiate the current upstream `XGO_DOG`/`XGO()` library merely to identify the old hardware.

**Evidence:** The reviewed current `LuwuDynamics/xgo_doglib` constructor invokes `reset()` during initialization.

**Reason:** Initialization could command movement. Hardware-path identification should precede motion tests.

## 2026-09-03 — COM3 is treated as K210-side until proven otherwise

**Decision:** Treat `COM3` as the K210/AI-module USB-UART path, not as a verified direct STM32 motion-controller UART.

**Evidence:**

- original protocol documents the STM32 motion interface as a separate 4-pin TTL connection normally occupied by the AI module;
- raw XGO firmware-read packet on COM3 produced no response;
- K210 serial probe on COM3 observed three CR/LF pairs;
- Ctrl-C did not expose an interactive REPL, which is compatible with the historical custom K210 menu application.

## 2026-09-03 — robot arm remains separate initially

**Decision:** Treat the legacy robot arm as an independent station rather than mounting it on the XGO.

**Reason:** Independent bring-up reduces mechanical, power and control complexity. Coordinated tasks can be implemented at the software layer after both devices are stable.
