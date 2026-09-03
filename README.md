# xgo-ai-lab

Recovery and modernization workspace for an original Kickstarter-era XGO-Mini.

## Verified hardware generation

This robot is the 2021-era **K210 + STM32** XGO-Mini:

- Kendryte K210 high-level/AI module;
- STM32 motion controller;
- 240x240 LCD;
- OV2640 camera;
- 16 GB microSD;
- CP2102 USB-UART exposed to Windows as **COM3**.

This is not the same lower-board generation as current ESP32-based XGO-Mini products.

## Current state

- CP210x driver installed; COM3 works.
- Raw XGO motion-protocol firmware query on COM3 returned no reply.
- K210 passive serial probe received three CR/LF pairs.
- Ctrl-C did not expose an interactive MicroPython/MaixPy REPL.
- Historical source shows the K210 normally runs a custom LCD/menu application and loads user/demo files from SD, so lack of REPL does not imply board failure.
- A historical 2021 K210 firmware/SD recovery package has been located; provenance is useful but not yet verified as official vendor firmware.

Read `docs/CURRENT_STATE.md` and `docs/RECOVERY_SOURCES.md` for the current recovery plan.

## Immediate next step

Capture boot-time serial while power-cycling the robot:

```powershell
cd C:\projects\xgo-ai-lab
git pull
.\.venv\Scripts\Activate.ps1
python scripts\k210_serial_probe.py COM3 --listen 20
```

Also photograph the powered LCD/menu and inspect/back up the microSD card before intentionally reflashing the K210.

## Firmware policy

Tamás has approved replacing old software/firmware when useful, but firmware must match the verified controller generation.

**Never flash current ESP32 XGO-Mini M-series lower-board firmware onto this original STM32 board.**

If K210 reflashing becomes necessary, use a verified K210 recovery image/tooling path. The historical `XgoAI` package and Sipeed `kflash_gui` are documented in `docs/RECOVERY_SOURCES.md`.

## Planned phases

1. Recover/understand K210 boot and SD state.
2. Identify direct STM32 TTL motion-controller access.
3. Establish a minimal safe motion test with an explicit stop path.
4. Build a stable Python control layer.
5. Add child-friendly controls.
6. Add voice/vision AI via PC or Local GPU Helper.
7. Integrate the legacy robot arm as a separate station.

## Repository memory

AI tools working on this repository must read:

- `AGENTS.md`
- `docs/CURRENT_STATE.md`
- `docs/DECISIONS.md`
- `docs/RECOVERY_SOURCES.md` for recovery/firmware work
- latest relevant file under `logs/`

Implementation state belongs in this repository rather than in chat history.
