# CURRENT_STATE

Updated: 2026-09-03

## Status

Repository initialized. Passive hardware bring-up is in progress.

## Confirmed

- Target robot: original Kickstarter-era XGO-Mini owned by Tamás.
- Repository: `tamaspota/xgo-ai-lab`.
- Current upstream `LuwuDynamics/xgo_doglib` supports `xgomini` and defaults to 115200 baud.
- Current upstream `XGO_DOG` initialization calls `reset()`, so it is unsuitable for the first passive diagnostic step.
- Windows sees the robot-side USB interface as **CP2102 USB to UART Bridge Controller** under `Other devices`.
- No new COM port appears yet because the CP210x VCP driver is not installed/loaded on this Windows installation.
- Baseline serial enumeration without a working XGO driver currently shows only legacy `COM1`.

## Unverified

- Exact board/controller revision.
- Exact firmware version.
- COM port that will be assigned after CP210x VCP driver installation.
- USB VID/PID and hardware ID after proper driver enumeration.
- Battery condition.
- Compatibility of the 2021-era firmware with the current upstream library.

## Current milestone

### M1 — safe bring-up

Goal: identify the robot and establish communication without accidental motion or firmware changes.

Completed:

1. Passive serial baseline collected: only `COM1`.
2. XGO connected to Windows PC.
3. Device Manager identified the USB-UART bridge as CP2102.

Next actions:

1. Install the official Silicon Labs **CP210x USB to UART Bridge VCP driver** for Windows.
2. Reconnect the XGO if needed.
3. Run `python scripts/list_serial_ports.py` again.
4. Record the newly assigned COM port and USB details.
5. Design a read-only protocol/firmware probe that does not instantiate the current high-level XGO library.

## Blockers

Windows CP210x VCP driver is currently missing/not loaded.

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
