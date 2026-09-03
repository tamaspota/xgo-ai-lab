# CURRENT_STATE

Updated: 2026-09-03

## Status

Repository initialized. Hardware bring-up has not started yet.

## Confirmed

- Target robot: original Kickstarter-era XGO-Mini owned by Tamás.
- Repository: `tamaspota/xgo-ai-lab`.
- Current upstream `LuwuDynamics/xgo_doglib` supports `xgomini` and defaults to 115200 baud.
- Current upstream `XGO_DOG` initialization calls `reset()`, so it is unsuitable for the first passive diagnostic step.

## Unverified

- Exact board/controller revision.
- Exact firmware version.
- Which USB/serial device appears on the Windows PC.
- Whether a USB-UART adapter is required or the robot exposes serial directly.
- Battery condition.
- Compatibility of the 2021-era firmware with the current upstream library.

## Current milestone

### M1 — safe bring-up

Goal: identify the robot and establish communication without accidental motion or firmware changes.

Next actions:

1. Run `scripts/list_serial_ports.py` with XGO disconnected.
2. Connect XGO to Windows PC.
3. Run the same script again.
4. Record newly appearing COM/device information.
5. Inspect exact hardware connection and only then design the first protocol probe.

## Blockers

Need the physical XGO connected to the PC and the serial enumeration output.

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
