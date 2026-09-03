# CURRENT_STATE

Updated: 2026-09-03

## Status

Original 2021 XGO-Mini hardware generation is identified as **K210 + STM32**. Windows USB discovery works on `COM3`. Direct XGO motion-protocol probing on COM3 produced no reply, but K210 serial probing produced a small amount of passive data, so the USB-UART path is alive and is most likely the K210 programming/console path rather than a transparent STM32 link.

## Confirmed

- Target robot: original Kickstarter-era XGO-Mini owned by Tamás.
- Repository: `tamaspota/xgo-ai-lab`.
- Local checkout: `C:\projects\xgo-ai-lab`.
- RobotShop legacy product page matches this generation and specifies **K210 + STM32**, 240x240 LCD, OV2640 camera, 16 GB SD, MEMS microphone, three programmable keys and 7.4 V 2500 mAh battery.
- K210 is the AI/high-level module; STM32 is the motion/core-drive controller.
- Windows USB-UART interface: Silicon Labs CP210x/CP2102 on **COM3**.
- VID:PID: **10C4:EA60**; serial `0001`; USB location `1-2`.
- Raw XGO firmware-read frame sent to COM3 at 115200 received **no response**.
- `python scripts\k210_serial_probe.py COM3 --listen 5` received 6 bytes: `0d 0a 0d 0a 0d 0a` (three CR/LF pairs).
- `python scripts\k210_serial_probe.py COM3 --listen 2 --repl` received no REPL response after Ctrl-C; no `>>>` prompt was detected.
- Historical K210 application source shows the board runs a custom menu/application and SD-based user/demo execution, so lack of a plain REPL does not establish a broken K210.
- Original 2021 XGO communication protocol documents the STM32 motion interface as a separate XH2.54 4-pin TTL UART at 115200 8N1, normally occupied by the AI module.
- Tamás explicitly approved replacing old firmware/software when useful, provided the image matches the verified hardware generation.

## Historical recovery material found

A historical public XGO AI demo source tree was found at:

- `geluu/XgoAI` (parent repository)
- fork: `mynameiskristopher/k210-XgoAI`

The English branch contains:

- `xgo-ai-module-firmware-210722-en-2021-07-22-14-48-10.kfpkg`;
- full SD-card style tree including `main.py`, `xgo.py`, demos, language and preset folders;
- Blockly XML examples.

This is a strong recovery lead, but it is **not yet verified as an official vendor repository**, so do not flash it blindly. Details and source-quality notes are in `docs/RECOVERY_SOURCES.md`.

## Important incompatibility

Current XGO-Mini product generations/documentation describe ESP32-based lower boards and publish current M-series firmware. The original 2021 robot is K210 + STM32.

**Do not flash current ESP32 M-series firmware onto this original STM32 board.**

## Current milestone

### M1 — recover the K210 side and identify STM32 access

Completed:

1. CP2102 driver and COM3 working.
2. Direct XGO protocol read on COM3 tested; no response.
3. Original K210 + STM32 architecture verified.
4. Historical STM32 TTL interface documented.
5. K210 serial probe run: passive CR/LF bytes observed, no interactive REPL.
6. Historical K210 firmware/SD recovery candidate located.

## Next actions

### 1. Capture K210 boot serial

Start a longer passive listener, then power-cycle the robot while it is listening:

```powershell
cd C:\projects\xgo-ai-lab
git pull
.\.venv\Scripts\Activate.ps1
python scripts\k210_serial_probe.py COM3 --listen 20
```

Capture the complete output.

### 2. Photograph the powered LCD/menu

The period K210 manual shows firmware information and a menu with entries such as DOG / Dog show / vision demos. A clear photo will identify how far the current K210 software boots.

### 3. Inspect and back up the microSD card

Before reflashing K210, remove/read the SD card if practical and copy its complete contents to a backup directory. Compare it with the historical `XgoAI` SD tree. Replacing missing/corrupt SD files may recover the stock application without touching flash.

## Blockers

- Need boot-time serial capture and LCD state.
- Installed SD-card contents are still unknown.
- Exact physical routing of CP2102 inside this unit is still unverified.
- Original STM32 firmware image/tooling remains unidentified.

## Do not do yet

- do not flash current ESP32 XGO-Mini firmware;
- do not overwrite STM32 without an original-generation image;
- do not assume lack of REPL means K210 failure;
- do not mirror/flash the historical K210 `.kfpkg` until the board/recovery path is checked.

## Later scope

- restore or replace K210 software;
- direct STM32 motion control from PC/Pi;
- safe Python control API;
- child-friendly controls;
- voice/vision AI via PC or Local GPU Helper;
- separate legacy robot-arm station;
- coordinated multi-robot tasks.
