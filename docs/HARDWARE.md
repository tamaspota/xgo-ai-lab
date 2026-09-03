# HARDWARE

Updated: 2026-09-03

## XGO-Mini

Status: physically available, detailed inspection pending.

Known from project context:

- original Kickstarter-era XGO-Mini;
- intended first host: Windows PC;
- later host/gateway may be PC or Raspberry Pi-class hardware;
- AI compute does not need to run on the original XGO AI board.

Still to record after physical connection:

- exterior/label photos;
- controller/AI board markings;
- connector used to attach to PC;
- Windows Device Manager name;
- USB VID/PID if available;
- COM port;
- firmware identity/version;
- battery condition;
- any installed SD card/software image.

## Legacy robot arm

Status: physically available according to project context, technical details not yet recorded.

Still needed:

- photos;
- motor/servo types;
- controller board;
- power supply;
- communication interface;
- original university code/project files if available.

## Verified upstream software facts

Reviewed 2026-09-03 from `LuwuDynamics/xgo_doglib` commit `cf72514273dc703284d3c47e46c67ce238caae11`:

- public `XGO()` entry point accepts serial port and baud arguments;
- default baud is 115200;
- `xgomini` is an explicitly supported device version;
- the current dog implementation performs a reset during initialization, therefore it is not used during passive bring-up.

These upstream facts do **not** yet prove compatibility with the installed 2021-era firmware.
