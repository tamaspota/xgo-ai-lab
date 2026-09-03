# HARDWARE

Updated: 2026-09-03

## XGO-Mini — original Kickstarter/K210 generation

Status: physically available and connected to the Windows PC for bring-up.

### Period hardware specification

Period XGO-Mini K210 documentation identifies this generation as:

- processor architecture: **Kendryte K210 + STM32**;
- K210 role: AI/high-level module;
- STM32 role: motion/core drive controller;
- display: 240 x 240 color LCD;
- camera: OV2640, 0.3 MP;
- storage: 16 GB SD card;
- battery: 7.4 V 2500 mAh;
- 12 DOF quadruped with serial bus servos.

This is materially different from current XGO-Mini generations whose driver-board documentation uses ESP32.

### 2026-09-03 Windows discovery

Baseline with XGO disconnected:

- `COM1` — `Communications Port (COM1)`;
- HWID: `ACPI\\PNP0501\\0`.

Connected USB interface after Silicon Labs VCP driver installation:

- port: **COM3**;
- description: `Silicon Labs CP210x USB to UART Bridge (COM3)`;
- manufacturer: `Silicon Labs`;
- HWID: `USB VID:PID=10C4:EA60 SER=0001 LOCATION=1-2`;
- VID:PID: **10C4:EA60**;
- serial: `0001`;
- USB location: `1-2`.

### COM3 protocol test

The repository's raw XGO firmware-version read was sent to COM3 at 115200 baud:

```text
55 00 09 02 07 0A E3 00 AA
```

Result: **no response**.

This result does not prove the motion controller or firmware is bad.

### Historical direct motion-controller interface

The original XGO-Mini Communication Protocol V1.0 (2021-08-05) specifies:

- standard TTL serial;
- XH2.54 4-pin connection;
- 115200 baud, 8 data bits, 1 stop bit, no parity;
- two UART connectors on the core board, with 5 V and 3.3 V external supply options that must not be used simultaneously;
- the **3.3 V UART is occupied by the AI module by default**;
- to use another external controller, the AI-module terminal must be unplugged and the external controller connected to the core board.

Interpretation: the external CP2102/COM3 path is likely associated with the K210 AI-module programming/console interface rather than a transparent bridge to the STM32 motion-controller UART. Physical routing still needs verification.

### Firmware compatibility warning

Tamás approved firmware/software replacement if useful. However:

- original robot: K210 + STM32;
- current published XGO-Mini lower-board firmware documentation: ESP32-based generations.

Do **not** flash current ESP32 `M`-series firmware onto the original STM32 board. Only hardware-generation-specific images are acceptable.

### Still to record

- clear exterior and underside photos;
- powered LCD/menu photo;
- K210 serial/REPL behavior on COM3;
- controller/AI board markings;
- internal 3.3 V TTL connector location/pinout photo;
- STM32 part marking if accessible;
- installed SD-card contents;
- battery condition.

## Legacy robot arm

Status: physically available according to project context, technical details not yet recorded.

Still needed:

- photos;
- motor/servo types;
- controller board;
- power supply;
- communication interface;
- original university code/project files if available.

## Verified current upstream software facts

Reviewed 2026-09-03 from `LuwuDynamics/xgo_doglib` commit `cf72514273dc703284d3c47e46c67ce238caae11`:

- public `XGO()` entry point accepts serial port and baud arguments;
- default baud is 115200;
- `xgomini` remains an explicitly supported logical device version;
- firmware version is read from address `0x07`, length 10, using protocol read mode `0x02`;
- current dog implementation performs a reset during initialization.

These current library facts do not establish direct compatibility with the original 2021 K210 + STM32 hardware path.
