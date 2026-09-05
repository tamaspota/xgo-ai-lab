# HARDWARE

Updated: 2026-09-05

## XGO-Mini — original Kickstarter/K210 generation

Status: physically opened for battery/power-path diagnosis and lower-board inspection.

### Verified period hardware specification

RobotShop's discontinued legacy XGO-Mini page (`RB-Xgo-01`, manufacturer `XGO-MINI`) and period documentation identify this generation as:

- processor architecture: **Kendryte K210 + STM32**;
- K210 role: AI/high-level module;
- STM32 role: motion/core-drive controller;
- display: 240 x 240 color LCD;
- camera: OV2640, 0.3 MP;
- storage: 16 GB SD card;
- microphone: MEMS digital microphone;
- keys: 3 programmable keys;
- battery specification: **7.4 V 2500 mAh**;
- 12 DOF quadruped with serial-bus servos;
- micro-USB data cable included with the original product.

This is materially different from current XGO-Mini generations whose lower-board documentation uses ESP32.

### Installed firmware indication

Tamás reports that the powered LCD shows firmware/version text approximately matching `xgo-210722`. This closely matches historical K210 recovery package `xgo-ai-module-firmware-210722-en-2021-07-22-14-48-10.kfpkg`. This is a strong family/date match but not proof of byte-identical firmware.

### 2026-09-03 Windows discovery

- XGO USB-UART: Silicon Labs CP210x/CP2102 on **COM3**.
- VID:PID: **10C4:EA60**.
- serial: `0001`.
- location: `1-2`.
- raw XGO firmware-read on COM3 at 115200: no response.
- K210 serial probe once received `0d 0a 0d 0a 0d 0a`; later probes were silent and no REPL appeared.

Historical K210 source shows a custom menu application, so no plain REPL does not prove failure.

### 2026-09-05 battery construction and power state

The robot was opened after it failed to power on from its normal power button despite approximately two hours on its charger.

Observed:

- two removable 18650-format Li-ion cells in an internal mechanical holder;
- the holder is part of the robot chassis, not a permanently welded external battery pack;
- given the historical 7.4 V specification, a 2S electrical arrangement is expected, but holder output voltage still needs direct measurement before treating that as electrically verified;
- both removed cells were placed in an XTAR VC2 charger; at the time photographed the charger did not show meaningful accumulated charge, so cell health is unresolved.

Required measurements:

1. cell 1 open-circuit voltage;
2. cell 2 open-circuit voltage;
3. holder/output voltage with two known-good matched cells installed;
4. voltage sag during power-on attempt.

Do not force-charge or bypass protection on severely over-discharged/damaged Li-ion cells.

### 2026-09-05 exposed lower/controller board

The opened chassis exposes a central lower board. Tamás reads the silkscreen as including **`XGO MINI V2.5`** plus a 2021-era code/date marking; the exact full code is not yet treated as verified from the available photo.

Visible features:

- micro-USB connector on the lower board;
- 4-pin connector clearly labelled **`SWITCH`** for the external power-switch harness;
- 4-pin service/debug header labelled **`G CLK DIO 3V3`** (P2);
- two small board-mounted mode switches which Tamás identifies from the silkscreen as **DOWNLOAD** and **CALIBRATE**;
- several additional 4-pin connectors for internal bus/power/AI-module wiring.

Engineering interpretation:

- `G CLK DIO 3V3` is highly consistent with an STM32 **SWD** header: GND, SWCLK, SWDIO, 3.3 V reference. This is an inference from the silkscreen and standard STM32 practice; it is not yet electrically verified.
- if confirmed, the original lower board has a direct debug/recovery route using an ST-Link-class interface, so board replacement is not required merely to gain firmware access.
- the exposed micro-USB and DOWNLOAD/CALIBRATE controls make the earlier assumption that COM3 must be the K210-side USB interface uncertain. COM3 may instead be a lower-board service/programming path. Physical routing needs verification after stable power is restored.

### Historical built-in self-test

The period `sd/main.py` can enter test mode by holding the **left/A button during boot** while the right/B button is not held. It executes `/sd/device_test.py` and tests LCD, camera, microphone, SD card, speaker, A/B/C buttons and LEDs.

See `docs/FACTORY_SELF_TEST.md`.

### Historical direct motion-controller interface

XGO-Mini Communication Protocol V1.0 (2021-08-05) specifies standard TTL serial, XH2.54 4-pin, 115200 8N1. It states that the 3.3 V UART is occupied by the AI module by default and must be disconnected for another controller to directly command the core board.

The exact relationship between this documented UART, the photographed 4-pin connectors and the lower-board micro-USB/CP2102 path remains to be mapped.

### Historical K210 recovery package found

A public historical `XgoAI` source tree contains `xgo-ai-module-firmware-210722-en-2021-07-22-14-48-10.kfpkg` and an SD application tree with `main.py`, `xgo.py`, demos and assets. See `docs/RECOVERY_SOURCES.md`.

### Firmware compatibility warning

Do **not** flash current ESP32 M-series XGO-Mini firmware onto this original K210 + STM32 generation.

### Still to record

- voltage of both original 18650 cells;
- holder/output voltage with known-good matched cells;
- exact full lower-board silkscreen/model code;
- exact function/pinout of all exposed 4-pin connectors;
- confirm whether `G CLK DIO 3V3` is SWD;
- identify which physical USB interface produces COM3;
- exact LCD firmware text/photo;
- built-in self-test results after power is restored;
- whether `/sd` passes and contains `try_demo.py`.

## Legacy robot arm

Status: physically available according to project context, technical details not yet recorded.

Still needed: photos, motor/servo types, controller board, power supply, communication interface and original university code/project files if available.

## Verified current upstream software facts

Reviewed 2026-09-03 from `LuwuDynamics/xgo_doglib` commit `cf72514273dc703284d3c47e46c67ce238caae11`: current public API supports `xgomini`, defaults to 115200 baud, and current `XGO_DOG` initialization performs a reset. These facts do not establish direct compatibility with the original 2021 K210 + STM32 hardware path.
