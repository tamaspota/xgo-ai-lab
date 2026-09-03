# CURRENT_STATE

Updated: 2026-09-03

## Status

Original 2021 XGO-Mini hardware generation is identified as **K210 + STM32**. Windows USB discovery works on `COM3`. Direct XGO motion-protocol probing on COM3 produced no reply. K210 serial probing produced a few CR/LF bytes once, but no interactive REPL. The powered robot reportedly displays a firmware/version string approximately matching **`xgo-210722`**, which closely matches a historical 2021 K210 firmware package found in the period XgoAI source tree.

## Confirmed

- Target robot: original Kickstarter-era XGO-Mini owned by Tamás.
- Repository: `tamaspota/xgo-ai-lab`.
- Local checkout: `C:\projects\xgo-ai-lab`.
- RobotShop legacy product data matches this generation and specifies **K210 + STM32**, 240x240 LCD, OV2640 camera, 16 GB SD, MEMS microphone, three programmable keys and 7.4 V 2500 mAh battery.
- K210 is the AI/high-level module; STM32 is the motion/core-drive controller.
- Windows USB-UART interface: Silicon Labs CP210x/CP2102 on **COM3**.
- VID:PID: **10C4:EA60**; serial `0001`; USB location `1-2`.
- Raw XGO firmware-read frame sent to COM3 at 115200 received **no response**.
- `python scripts\k210_serial_probe.py COM3 --listen 5` received 6 bytes: `0d 0a 0d 0a 0d 0a`.
- `python scripts\k210_serial_probe.py COM3 --listen 2 --repl` received no REPL response; no `>>>` prompt was detected.
- `python scripts\k210_serial_probe.py COM3 --listen 20` later received no bytes.
- Historical K210 application source shows the board runs a custom menu/application and SD-based user/demo execution, so lack of a plain REPL does not establish a broken K210.
- Original 2021 XGO communication protocol documents the STM32 motion interface as a separate XH2.54 4-pin TTL UART at 115200 8N1, normally occupied by the AI module.
- Tamás explicitly approved replacing old firmware/software when useful, provided the image matches the verified hardware generation.

## Strong historical version match

Tamás reports that the robot display shows firmware text approximately `xgo-210722`.

A historical public XGO AI demo source tree contains:

`xgo-ai-module-firmware-210722-en-2021-07-22-14-48-10.kfpkg`

The date/version match is strong evidence that the installed K210 software is from the same 2021 software family. This is not yet treated as proof that the installed binary is byte-identical to that package.

The same source tree includes the expected SD application files (`main.py`, `xgo.py`, `device_test.py`, `try_demo.py`, demos/assets).

## Built-in factory/self-test path found

Historical `sd/main.py` contains a startup test mode: hold the **left/A button** during boot while the right/B button is not held. It executes `/sd/device_test.py`.

That self-test checks:

1. LCD
2. camera
3. microphone
4. SD card
5. speaker
6. A/B/C buttons
7. LEDs

The SD test mounts `/sd`, lists its files, and requires `try_demo.py` to be present. Therefore the next check can determine whether an SD card is installed and usable **without opening the robot first**.

Detailed procedure: `docs/FACTORY_SELF_TEST.md`.

## Historical recovery material found

Historical parent repository:

- `geluu/XgoAI`

Useful fork:

- `mynameiskristopher/k210-XgoAI`

English branch contains:

- `xgo-ai-module-firmware-210722-en-2021-07-22-14-48-10.kfpkg`;
- full SD-card style tree;
- Blockly XML examples.

This is a strong recovery lead, but not yet verified as an official current vendor repository. Source-quality notes are in `docs/RECOVERY_SOURCES.md`.

## Important incompatibility

Current XGO-Mini product generations/documentation describe ESP32-based lower boards and publish current M-series firmware. The original 2021 robot is K210 + STM32.

**Do not flash current ESP32 M-series firmware onto this original STM32 board.**

## Current milestone

### M1 — verify original K210 stack, then reach STM32 motion control

Completed:

1. CP2102 driver and COM3 working.
2. Direct XGO protocol read on COM3 tested; no response.
3. Original K210 + STM32 architecture verified.
4. Historical STM32 TTL interface documented.
5. K210 serial probe run: intermittent passive CR/LF bytes, no interactive REPL.
6. Historical K210 firmware/SD recovery candidate located.
7. Reported installed firmware string strongly matches the historical `210722` K210 package.
8. Historical built-in hardware/self-test path identified.

## Next action

Run the built-in historical factory test before any flash operation:

1. close any program holding `COM3`;
2. power robot off;
3. hold **left/A** button;
4. power robot on while holding left/A;
5. release after the test screen appears;
6. photograph/transcribe every test result.

Expected stages: LCD -> camera -> microphone -> SD -> speaker -> buttons -> LEDs.

If the SD stage says `OK`, then an SD card is installed/mounted and contains the expected `try_demo.py` application file.

## Decision path after self-test

- **All/most tests OK:** keep current K210 firmware; move to uploading/running a minimal user program and exercising the historical K210 `xgo.py` -> STM32 path.
- **SD fails, K210 peripherals work:** repair/rebuild SD contents first; do not flash K210 yet.
- **Broad K210 failure:** evaluate the matched 2021 `.kfpkg` recovery path.

## Blockers

- Need built-in self-test result and a clear LCD photo/transcription.
- Installed SD-card state is still unknown until self-test.
- Exact physical routing of CP2102 inside this unit remains unverified.
- Original STM32 firmware image/tooling remains unidentified, but STM32 reflashing is not currently required.

## Do not do yet

- do not flash current ESP32 XGO-Mini firmware;
- do not overwrite STM32 without an original-generation image;
- do not assume lack of REPL means K210 failure;
- do not flash the historical K210 `.kfpkg` before running the built-in self-test.

## Later scope

- retain or recover original K210 software;
- establish user-code upload/run workflow;
- exercise K210 -> STM32 motion commands;
- optionally replace K210 with PC/Pi as high-level compute later;
- safe Python control API;
- child-friendly controls;
- voice/vision AI via PC or Local GPU Helper;
- separate legacy robot-arm station;
- coordinated multi-robot tasks.
