# HARDWARE

Updated: 2026-09-03

## XGO-Mini — original Kickstarter/K210 generation

Status: physically available and connected to the Windows PC for bring-up.

### Verified period hardware specification

RobotShop's discontinued legacy XGO-Mini page (`RB-Xgo-01`, manufacturer `XGO-MINI`) and period documentation identify this generation as:

- processor architecture: **Kendryte K210 + STM32**;
- K210 role: AI/high-level module;
- STM32 role: motion/core-drive controller;
- display: 240 x 240 color LCD;
- camera: OV2640, 0.3 MP;
- storage: 16 GB SD card;
- microphone: MEMS digital microphone;
- keys: 3 programmable keys;
- battery: 7.4 V 2500 mAh;
- 12 DOF quadruped with serial-bus servos;
- micro-USB data cable included with the original product.

This is materially different from current XGO-Mini generations whose lower-board documentation uses ESP32.

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

### COM3 test results

Raw XGO motion-controller firmware-read query at 115200:

```text
55 00 09 02 07 0A E3 00 AA
```

Result: **no response**.

K210 serial passive probe:

```text
passive RX bytes: 6
hex: 0d 0a 0d 0a 0d 0a
```

Interpretation: three CR/LF pairs were received, so COM3 is not a completely dead serial path.

K210 Ctrl-C / MicroPython REPL probe:

- no bytes returned after Ctrl-C;
- no `>>>` prompt detected.

Historical K210 source shows a custom menu application running from flash/SD rather than requiring a plain REPL, so this result does not establish K210 failure.

### Historical direct motion-controller interface

XGO-Mini Communication Protocol V1.0 (2021-08-05) specifies:

- standard TTL serial;
- XH2.54 4-pin connection;
- 115200 baud, 8N1;
- the **3.3 V UART is occupied by the AI module by default**;
- for direct external control, disconnect the AI-module terminal and connect the external host to the core board.

Interpretation: COM3 is likely the K210 AI-module USB/programming/console path, while the STM32 motion protocol is on an internal TTL path.

### Historical K210 recovery package found

A public historical `XgoAI` source tree contains a dated English K210 firmware package:

`xgo-ai-module-firmware-210722-en-2021-07-22-14-48-10.kfpkg`

and an SD application tree including `main.py`, `xgo.py`, demo and asset directories. This closely matches the legacy RobotShop/manual architecture, but the repository is not yet verified as an official vendor source. See `docs/RECOVERY_SOURCES.md`.

### Firmware compatibility warning

Tamás approved firmware/software replacement if useful. However:

- original robot: K210 + STM32;
- current published lower-board XGO-Mini firmware may target ESP32-based hardware.

Do **not** flash current ESP32 M-series firmware onto the original STM32 board.

### Still to record

- clear exterior and underside photos;
- powered LCD/menu photo;
- boot-time K210 serial output;
- controller/AI board markings;
- internal 3.3 V TTL connector location/pinout photo;
- STM32 part marking if accessible;
- installed SD-card contents and backup;
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
