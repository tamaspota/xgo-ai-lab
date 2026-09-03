# HARDWARE

Updated: 2026-09-03

## XGO-Mini

Status: physically available and connected to the Windows PC for first passive discovery.

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

After connecting the XGO:

- no new COM port appeared yet;
- Windows Device Manager did detect a new device under `Other devices`;
- detected name: **CP2102 USB to UART Bridge Controller**;
- the device shows a warning icon, consistent with the VCP driver not being installed/loaded.

Interpretation: the physical USB connection is working far enough for Windows to enumerate the CP2102 USB-UART bridge. The current blocker is the Windows CP210x VCP driver, not an absent USB device.

Next hardware check after driver installation:

- confirm device moves from `Other devices` to `Ports (COM & LPT)`;
- record assigned COM port;
- record VID/PID and hardware ID from Device Manager or `list_serial_ports.py`;
- do not send protocol or motion commands yet.

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
- the current dog implementation performs a reset during initialization, therefore it is not used during passive bring-up.

These upstream facts do **not** yet prove compatibility with the installed 2021-era firmware.
