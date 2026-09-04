# HARDWARE

Updated: 2026-09-04

## XGO-Mini — original Kickstarter/K210 generation

Status: physically available and connected to the Windows PC for bring-up. Current blocker is the battery/power path.

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
- battery: **7.4 V 2500 mAh**;
- 12 DOF quadruped with serial-bus servos;
- micro-USB data cable included with the original product.

This is materially different from current XGO-Mini generations whose lower-board documentation uses ESP32.

### Battery / power-path observation — 2026-09-04

Tamás reports:

- robot was left charging for approximately two hours;
- normal startup from the power button still does not work;
- USB has previously powered at least the USB/K210-side electronics sufficiently for Windows enumeration and serial probing.

Interpretation: a failed or deeply discharged battery is the leading hypothesis, but this is not yet confirmed. Other plausible causes are battery-protection state, loose/disconnected battery connector, charge-path fault or power-switch/power-path fault.

Next check:

- unplug USB;
- inspect pack for swelling, damage, abnormal heat or odor;
- if safely accessible, measure pack voltage at the battery connector;
- inspect connector and charge indication behavior.

Do not attempt protection bypass, forced charging or cell-level revival of an aged lithium pack.

### Installed firmware indication

Tamás reports that the powered LCD shows firmware/version text approximately matching:

`xgo-210722`

This closely matches a historical K210 recovery package named:

`xgo-ai-module-firmware-210722-en-2021-07-22-14-48-10.kfpkg`

Interpretation: strong evidence that the installed K210 software belongs to the original July 22, 2021 software family. Exact binary identity is not proven.

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

K210 serial passive probe first run:

```text
passive RX bytes: 6
hex: 0d 0a 0d 0a 0d 0a
```

Later 20-second passive run:

```text
passive RX bytes: 0
<none>
```

K210 Ctrl-C / MicroPython REPL probe:

- no bytes returned after Ctrl-C;
- no `>>>` prompt detected.

Historical K210 source shows a custom menu application, so no plain REPL is expected evidence of neither success nor failure.

### Historical built-in self-test

The period `sd/main.py` can enter test mode by holding the **left/A button during boot** while the right/B button is not held. It executes `/sd/device_test.py`.

The historical self-test checks LCD, camera, microphone, SD card, speaker, A/B/C buttons and LEDs. The SD stage lists `/sd` and requires `try_demo.py` to exist.

See `docs/FACTORY_SELF_TEST.md`.

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

and an SD application tree including `main.py`, `xgo.py`, demo and asset directories. This closely matches the legacy RobotShop/manual architecture, but the repository is not verified as a current official vendor source. See `docs/RECOVERY_SOURCES.md`.

### Firmware compatibility warning

Tamás approved firmware/software replacement if useful. However:

- original robot: K210 + STM32;
- current published lower-board XGO-Mini firmware may target ESP32-based hardware.

Do **not** flash current ESP32 M-series firmware onto the original STM32 board.

### Still to record

- battery physical condition;
- battery-pack voltage;
- connector and charge-path state;
- clear exterior and underside photos;
- exact LCD firmware text/photo;
- built-in self-test results after stable power is restored;
- whether `/sd` passes and contains `try_demo.py`;
- controller/AI board markings;
- internal 3.3 V TTL connector location/pinout photo if later needed.

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
