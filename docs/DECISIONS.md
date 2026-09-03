# DECISIONS

## 2026-09-03 — repository scope

**Decision:** Use one repository, `xgo-ai-lab`, as the shared implementation memory for XGO bring-up, later AI integration, and eventual coordination with the legacy robot arm.

**Reason:** Avoid fragmented chat-only knowledge and allow multiple coding agents/tools to work from the same current state.

## 2026-09-03 — no firmware update during bring-up

**Decision:** Initial recovery is diagnostic only. No firmware flashing or updating unless explicitly approved later.

**Reason:** The hardware is old and exact firmware/controller compatibility is not yet verified. Preserving a working baseline is more valuable than immediately modernizing it.

## 2026-09-03 — passive discovery before xgolib

**Decision:** Do not instantiate the current upstream `XGO_DOG`/`XGO()` library against the real robot during the first diagnostic step.

**Evidence:** The reviewed current upstream source (`LuwuDynamics/xgo_doglib`, commit `cf72514273dc703284d3c47e46c67ce238caae11`) invokes `reset()` while initializing `XGO_DOG`.

**Reason:** Initialization could move the robot. The first step must be non-motion serial/device discovery.

## 2026-09-03 — robot arm remains separate initially

**Decision:** Treat the legacy robot arm as an independent station rather than mounting it on the XGO.

**Reason:** Independent bring-up reduces mechanical, power and control complexity. Coordinated tasks can be implemented at the software layer after both devices are stable.
