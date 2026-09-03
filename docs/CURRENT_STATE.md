# CURRENT_STATE

Updated: 2026-09-03

## Status

Original 2021 XGO-Mini hardware generation is now identified from period documentation. Windows USB discovery works, but the first direct XGO motion-protocol read on `COM3` returned no data. The most likely next task is to identify the K210 AI-module serial/console path rather than assume the STM32 motion firmware is dead.

## Confirmed

- Target robot: original Kickstarter-era XGO-Mini owned by Tamás.
- Repository: `tamaspota/xgo-ai-lab`.
- Local checkout: `C:\projects\xgo-ai-lab`.
- Period XGO-Mini K210 documentation identifies this generation as **K210 + STM32**.
- Period hardware spec: 240x240 LCD, OV2640 camera, 16 GB SD card, 7.4 V 2500 mAh battery.
- The AI module is Kendryte K210; the motion controller is STM32.
- Windows identifies the connected USB interface as Silicon Labs CP210x/CP2102.
- CP210x VCP driver is installed and working.
- USB-UART interface is **COM3**.
- VID:PID: **10C4:EA60**; serial `0001`; USB location `1-2`.
- `scripts/xgo_read_firmware_raw.py COM3` sent the inspected XGO firmware read frame at 115200 baud and received **no response**.
- The original 2021 XGO communication protocol documents the direct motion-controller interface as a **separate XH2.54 4-pin TTL UART**.
- The protocol states that the 3.3 V motion-board UART is normally occupied by the AI module; for direct external control, that AI-module connection must be unplugged and the external host connected to the motion board.
- Therefore `COM3` is not yet proven to be a direct STM32 motion-controller UART and the no-response result does not establish bad motion firmware.
- Tamás explicitly approved replacing old firmware/software if useful, provided the image is for the verified hardware.
- `scripts/k210_serial_probe.py` now exists for K210 serial/REPL identification without flashing.

## Important incompatibility

Current XGO-Mini product generations/documentation describe an ESP32 motion board and publish current `M`-series ESP32 firmware. The original 2021 robot is documented as K210 + STM32.

**Do not flash current ESP32 `M` firmware onto this original STM32 board.** A firmware prefix/model name match is insufficient because the MCU generation differs.

## Current milestone

### M1 — identify the two-controller paths

Goal: separately identify:

1. K210 AI-module USB/programming interface;
2. STM32 motion-controller TTL interface.

Completed:

1. CP2102 driver and COM3 working.
2. Direct XGO protocol read on COM3 tested; no response.
3. Historical hardware architecture verified as K210 + STM32.
4. Historical motion protocol verified to use a separate 4-pin TTL connector normally occupied by the AI module.
5. K210 serial probe added.

## Next actions

First inspect the AI module rather than flash anything:

```powershell
cd C:\projects\xgo-ai-lab
git pull
.\.venv\Scripts\Activate.ps1
python scripts\k210_serial_probe.py COM3 --listen 5
```

If no serial output appears, run:

```powershell
python scripts\k210_serial_probe.py COM3 --listen 2 --repl
```

Also power the robot normally and photograph the LCD/menu. The original manual shows a K210 application menu and 2021-era firmware information, so the screen is another useful identification path.

If K210 recovery is straightforward, replacing its old software is acceptable. Direct PC control of the STM32 motion board will likely require access to the internal 3.3 V TTL connector documented in the 2021 protocol.

## Blockers

- Need result of K210 serial/REPL probe and/or a clear photo of the powered LCD/menu.
- Exact physical routing of the CP2102 interface inside this unit remains unverified.
- Exact original STM32 firmware image/tooling has not yet been identified.

## Do not do yet

- do not flash current ESP32 XGO-Mini firmware onto the original STM32 board;
- do not use an unverified STM32 firmware image;
- do not assume COM3 is the STM32 protocol port;
- do not instantiate current high-level `xgolib` merely to probe the hardware.

## Later scope

- restore/replace K210 software or replace K210 as high-level compute;
- direct STM32 motion control from PC/Pi;
- safe Python control API;
- child-friendly controls;
- voice/vision AI via PC or Local GPU Helper;
- separate legacy robot-arm station;
- coordinated multi-robot tasks.
