# CURRENT_STATE

Updated: 2026-09-04

## Status

Original 2021 XGO-Mini hardware generation is identified as **K210 + STM32**. Windows USB discovery works on `COM3`. Direct XGO motion-protocol probing on COM3 produced no reply. K210 serial probing produced a few CR/LF bytes once, but no interactive REPL. The robot reportedly displays firmware/version text approximately matching **`xgo-210722`**, which closely matches a historical 2021 K210 firmware package found in the period XgoAI source tree.

The current physical blocker is now the **battery / power path**. After approximately two hours of charging, the robot still does not start from its normal power button, while USB has been able to power at least the USB/K210-side electronics. A failed or deeply discharged battery is the leading hypothesis, but this is not yet confirmed.

## Confirmed

- Target robot: original Kickstarter-era XGO-Mini owned by Tamás.
- Repository: `tamaspota/xgo-ai-lab`.
- Local checkout: `C:\projects\xgo-ai-lab`.
- This repository is the intended shared engineering memory for implementation, experiments, documentation, ideas and multi-agent handoff.
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
- After approximately two hours on charge, normal battery-powered startup still fails.
- USB power has been sufficient for previous PC-side enumeration/communication.

## Strong historical version match

Tamás reports that the robot display shows firmware text approximately `xgo-210722`.

A historical public XGO AI demo source tree contains:

`xgo-ai-module-firmware-210722-en-2021-07-22-14-48-10.kfpkg`

The date/version match is strong evidence that the installed K210 software is from the same 2021 software family. This is not proof that the installed binary is byte-identical to that package.

The same source tree includes the expected SD application files (`main.py`, `xgo.py`, `device_test.py`, `try_demo.py`, demos/assets).

## Built-in factory/self-test path found

Historical `sd/main.py` contains a startup test mode: hold the **left/A button** during boot while the right/B button is not held. It executes `/sd/device_test.py`.

That self-test checks LCD, camera, microphone, SD card, speaker, A/B/C buttons and LEDs. The SD test mounts `/sd`, lists its files, and requires `try_demo.py` to be present.

Detailed procedure: `docs/FACTORY_SELF_TEST.md`.

## Historical recovery material found

Historical parent repository: `geluu/XgoAI`.

Useful fork: `mynameiskristopher/k210-XgoAI`.

English branch contains the dated K210 `.kfpkg`, full SD-card style tree and Blockly XML examples. This is a strong recovery lead, but not yet verified as an official current vendor repository. Source-quality notes are in `docs/RECOVERY_SOURCES.md`.

## Important incompatibility

Current XGO-Mini product generations/documentation describe ESP32-based lower boards and publish current M-series firmware. The original 2021 robot is K210 + STM32.

**Do not flash current ESP32 M-series firmware onto this original STM32 board.**

## Current milestone

### M1 — restore stable power, then verify original K210 stack and reach STM32 motion control

Completed:

1. CP2102 driver and COM3 working.
2. Direct XGO protocol read on COM3 tested; no response.
3. Original K210 + STM32 architecture verified.
4. Historical STM32 TTL interface documented.
5. K210 serial probe run: intermittent passive CR/LF bytes, no interactive REPL.
6. Historical K210 firmware/SD recovery candidate located.
7. Reported installed firmware string strongly matches the historical `210722` K210 package.
8. Historical built-in hardware/self-test path identified.
9. Battery-powered startup failure identified as the current hardware blocker.

## Next action

Before any firmware work, diagnose the battery/power path:

1. disconnect USB;
2. visually inspect the battery for swelling, damage, heat or odor;
3. if safely accessible, measure the battery-pack voltage at its connector with a multimeter;
4. inspect the battery connector and charge-path behavior;
5. record measured voltage and physical condition.

The period battery specification is **7.4 V 2500 mAh**, i.e. a nominal 2S lithium pack. Do not attempt cell-level revival or protection bypass on an aged/deeply discharged pack.

After stable battery/power operation is restored, run the built-in factory/self-test before any flash operation.

## Decision path after power diagnosis

- **Battery clearly failed / abnormal:** replace with a verified compatible pack before further robot tests.
- **Battery voltage plausible but robot still will not start:** inspect connector, charge path, power switch and power distribution.
- **Normal startup restored:** run factory self-test, then determine SD/K210 state.

## Legacy robot arm

A university-era robot arm is available and is intended as a future second device in this repository. It is not yet technically identified. When photos, controller details, original code or documentation are supplied, add them to the hardware/source records and bring the arm up independently before coordinated XGO + arm work.

## Future upgrade direction

Candidate modernization ideas (better camera, off-board compute, Local GPU Helper, child-friendly controls, robot-arm coordination and other software/sensor upgrades) are tracked separately in `docs/IDEAS.md`. They are not current commitments and should be promoted only when a concrete limitation/use case is verified.

## Blockers

- Normal battery-powered boot fails after approximately two hours of charging.
- Battery condition and pack voltage are unknown.
- Installed SD-card state remains unknown until power/self-test/inspection.
- Exact physical routing of CP2102 inside this unit remains unverified.
- Original STM32 firmware image/tooling remains unidentified, but STM32 reflashing is not currently required.
- Legacy robot arm technical details are not yet supplied.

## Do not do yet

- do not flash current ESP32 XGO-Mini firmware;
- do not overwrite STM32 without an original-generation image;
- do not assume lack of REPL means K210 failure;
- do not flash the historical K210 `.kfpkg` while power is unstable;
- do not attempt to revive an aged lithium pack by bypassing protection or forcing charge;
- do not buy/replace the robotics platform merely because newer models exist; first identify what the existing hardware cannot do.

## Later scope

- retain or recover original K210 software;
- establish user-code upload/run workflow;
- exercise K210 -> STM32 motion commands;
- optionally replace K210 with PC/Pi as high-level compute later;
- safe Python control API;
- child-friendly controls;
- upgraded camera/sensing when justified;
- voice/vision AI via PC or Local GPU Helper;
- separate legacy robot-arm station;
- coordinated multi-robot tasks.
