# DECISIONS

## 2026-09-03 — repository scope

**Decision:** Use one repository, `xgo-ai-lab`, as the shared implementation memory for XGO bring-up, later AI integration, and eventual coordination with the legacy robot arm.

**Reason:** Avoid fragmented chat-only knowledge and allow multiple coding agents/tools to work from the same current state.

## 2026-09-03 — firmware rewrite is allowed, but only for verified hardware

**Decision:** Tamás explicitly approved replacing old firmware/software if useful. This removes the requirement to preserve the installed software as a valuable baseline. However, firmware may only be flashed after the target MCU/board is identified and a firmware image is verified for that hardware generation.

**Reason:** The original 2021 XGO-Mini is documented as **K210 + STM32**, while current XGO-Mini generations use a different driver-board architecture (ESP32). A current `M`-series ESP32 firmware package must not be assumed compatible with the original STM32 board.

**Practical consequence:**

- K210 AI-module software may be replaced once its flashing path is identified.
- Original STM32 motion-controller firmware may be replaced only with a verified original-generation image/tooling.
- Do not flash current ESP32 driver-board firmware onto this 2021 robot.

## 2026-09-03 — passive discovery before xgolib

**Decision:** Do not instantiate the current upstream `XGO_DOG`/`XGO()` library against the real robot during the first diagnostic step.

**Evidence:** The reviewed current upstream source (`LuwuDynamics/xgo_doglib`, commit `cf72514273dc703284d3c47e46c67ce238caae11`) invokes `reset()` while initializing `XGO_DOG`.

**Reason:** Initialization could move the robot. Hardware-path identification should precede motion tests.

## 2026-09-03 — COM3 is not yet proven to be the motion-controller UART

**Decision:** Treat `COM3` as the K210/AI-module USB-UART path until proven otherwise, not as a verified direct connection to the STM32 motion controller.

**Evidence:** The original 2021 communication protocol documents the motion-controller interface as a separate 4-pin TTL UART on the core board. It states that the 3.3 V UART is normally occupied by the AI module and must be unplugged when another host directly controls the motion board. The raw XGO firmware-read packet sent to COM3 produced no response.

**Reason:** This explains the failed direct protocol probe without requiring a firmware-failure hypothesis.

## 2026-09-03 — robot arm remains separate initially

**Decision:** Treat the legacy robot arm as an independent station rather than mounting it on the XGO.

**Reason:** Independent bring-up reduces mechanical, power and control complexity. Coordinated tasks can be implemented at the software layer after both devices are stable.
