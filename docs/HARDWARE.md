# HARDWARE

Updated: 2026-09-03

## XGO-Mini

Status: physically available and connected to the Windows PC for safe bring-up.

Known from project context:

- original Kickstarter-era XGO-Mini;
- intended first host: Windows PC;
- later host/gateway may be PC or Raspberry Pi-class hardware;
- AI compute does not need to run on the original XGO AI board.

### 2026-09-03 Windows discovery

Baseline with XGO disconnected:

- `COM1` — `Communications Port (COM1)`;
- HWID: `ACPI\\PNP0501\\0`;
- no USB VID/PID reported.

Initial connection before driver installation:

- Windows Device Manager detected **CP2102 USB to UART Bridge Controller** under `Other devices`;
- device showed a warning icon;
- no additional COM port was available.

After installing the Silicon Labs CP210x VCP driver:

- assigned port: **COM3**;
- description: `Silicon Labs CP210x USB to UART Bridge (COM3)`;
- manufacturer: `Silicon Labs`;
- HWID: `USB VID:PID=10C4:EA60 SER=0001 LOCATION=1-2`;
- USB VID:PID: **10C4:EA60**;
- serial: `0001`;
- USB location: `1-2`.

Interpretation: the PC-to-robot USB path exposes a working Silicon Labs CP210x USB-UART bridge. No separate USB-UART adapter is currently required for the first protocol test.

Next hardware/protocol check:

- use `COM3` at the upstream default `115200` baud;
- run only the repository's explicit firmware-version READ probe;
- do not instantiate the current high-level `xgolib` class yet;
- do not flash firmware or send motion/reset/action commands.

Still to record later:

- exterior/label photos;
- controller/AI board markings;
- exact connector used to attach to PC;
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
- firmware version is read from address `0x07`, length 10, using protocol read mode `0x02`;
- the current dog implementation performs a reset during initialization, therefore it is not used during initial bring-up.

These upstream facts do **not** yet prove compatibility with the installed 2021-era firmware.
