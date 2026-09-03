# CURRENT_STATE

Updated: 2026-09-03

## Status

Repository initialized. Safe hardware bring-up is in progress and the Windows serial path is now identified.

## Confirmed

- Target robot: original Kickstarter-era XGO-Mini owned by Tamás.
- Repository: `tamaspota/xgo-ai-lab`.
- Local checkout: `C:\projects\xgo-ai-lab`.
- Current upstream `LuwuDynamics/xgo_doglib` supports `xgomini` and defaults to 115200 baud.
- Current upstream `XGO_DOG` initialization calls `reset()`, so it remains unsuitable for initial hardware probing.
- Windows identifies the robot-side USB interface as Silicon Labs CP210x/CP2102.
- Official CP210x VCP driver is installed and working.
- XGO USB-UART interface is now **COM3**.
- VID:PID: **10C4:EA60**.
- serial: `0001`.
- USB location: `1-2`.
- Baseline legacy serial port remains `COM1`.
- A dedicated raw firmware READ probe now exists at `scripts/xgo_read_firmware_raw.py`.

## Unverified

- Exact board/controller revision.
- Exact firmware version.
- Whether the original 2021-era controller replies to the current upstream firmware-read request.
- Battery condition.
- Full compatibility of the 2021-era firmware with the current upstream library.

## Current milestone

### M1 — safe bring-up

Goal: identify the robot and establish communication without accidental motion or firmware changes.

Completed:

1. Passive serial baseline collected: only `COM1`.
2. XGO connected to Windows PC.
3. Device Manager identified the USB-UART bridge as CP2102.
4. Silicon Labs CP210x VCP driver installed.
5. XGO serial interface enumerated as `COM3` with VID:PID `10C4:EA60`.
6. Inspected upstream read protocol and created a local firmware-only raw probe without importing `xgolib`.

Next action:

```powershell
cd C:\projects\xgo-ai-lab
git pull
.\.venv\Scripts\Activate.ps1
python scripts\xgo_read_firmware_raw.py COM3
```

Record the complete output. If no reply is received, check robot/controller power and hardware details before trying any other protocol command.

## Current blocker

Need the result of the first firmware-version READ request on `COM3`.

## Do not do yet

- firmware flash/update;
- instantiate current `xgolib.XGO` or `XGO_DOG` against the real robot;
- send gait, reset, servo, posture or other motion commands;
- integrate AI/voice/vision before basic control is verified.

## Later scope

- safe Python control API;
- child-friendly manual controls;
- voice/vision AI via PC or Local GPU Helper;
- separate legacy robot-arm station;
- coordinated multi-robot tasks.
