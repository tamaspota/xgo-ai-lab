# HARDWARE

Updated: 2026-09-05

## XGO-Mini — original Kickstarter/K210 generation

Status: physically opened for battery/power-path diagnosis and lower-board inspection.

### Verified period hardware specification

RobotShop legacy XGO-Mini documentation identifies this generation as:

- processor architecture: **Kendryte K210 + STM32**;
- K210 role: AI/high-level module;
- STM32 role: motion/core-drive controller;
- display: 240 x 240 color LCD;
- camera: OV2640, 0.3 MP;
- storage: 16 GB SD card;
- microphone: MEMS digital microphone;
- keys: 3 programmable keys;
- battery: **7.4 V 2500 mAh**;
- battery cell description on RobotShop legacy page: **standard 18650, 2500 mAh, 3C discharge**;
- 12 DOF quadruped with serial-bus servos;
- original charger: 8.4 V / 1 A.

### Installed firmware indication

Powered LCD previously showed firmware/version text approximately matching `xgo-210722`, closely matching historical K210 recovery package `xgo-ai-module-firmware-210722-en-2021-07-22-14-48-10.kfpkg`.

### Windows discovery

- Silicon Labs CP210x/CP2102 enumerated on **COM3**;
- VID:PID `10C4:EA60`;
- serial `0001`;
- raw XGO firmware-read on COM3 at 115200: no response;
- serial probe once received three CR/LF pairs; later probes silent; no REPL.

COM3 physical ownership is **not yet resolved**.

### Battery construction and measured state — 2026-09-05

Observed:

- two removable 18650-format Li-ion cells in a chassis holder;
- historical 7.4 V specification strongly implies 2S operation;
- holder has a visible `+` marking in the photographed upper cell bay;
- original cells measured approximately **3.74 V** and **3.70 V** open circuit;
- normal power-button startup still produces no visible response.

Interpretation:

- neither cell is obviously deeply discharged from open-circuit voltage alone;
- open-circuit voltage does not prove usable current capability;
- aged/high-resistance cells may sag heavily during startup;
- a RobotShop support case with essentially the same XGO-Mini K210 no-start symptom was fixed by replacing the batteries, making battery/current-delivery failure plausible but not proven here.

Next electrical measurement is the holder **pack-end voltage** and its sag during power-button press.

### Exposed lower/controller board — 2026-09-05

Photographed board features:

- visible board date marking **`20211027`**;
- lower-board micro-USB;
- 4-pin `SWITCH` harness connector;
- two board-mounted mode switches labelled DOWNLOAD and CALIBRATE;
- physically populated white 4-pin connector immediately adjacent to silkscreen **`G CLK DIO 3V3`**;
- multiple additional 4-pin connectors near the lower-board micro-USB, including one carrying colored wires.

#### Correction: `G CLK DIO 3V3`

This is not a free-standing test point. It is silkscreen next to a 4-pin connector.

Engineering inference only:

- `G` -> likely GND;
- `CLK` -> likely SWCLK;
- `DIO` -> likely SWDIO;
- `3V3` -> likely target-voltage reference.

This is strongly consistent with STM32 SWD naming, but it must be electrically verified before attaching an ST-Link.

#### Serial connectors

The original XGO-Mini Communication Protocol V1.0 explicitly states that **two serial communication interfaces exist on one side of the motherboard**, with external supply voltages of 5 V and 3.3 V. It also states that the **3.3 V terminal is occupied by the AI module by default**.

The photographed two 4-pin connector area near the lower-board micro-USB is therefore a strong match for the documented TTL UART interfaces. Exact pin order still needs a clear silkscreen read/continuity map.

### Power-path measurement method without schematic

With **all USB disconnected and both cells removed**:

1. use continuity mode to map accessible battery-holder solder tabs to each metal cell contact;
2. identify any direct 2S series bridge between one cell end and the opposite cell end;
3. the remaining two rails are the likely pack endpoints;
4. reinstall two matched cells with verified polarity;
5. measure across the pack endpoints — with ~3.7 V cells, expected magnitude is roughly ~7.4 V;
6. press the power switch while measuring the same points and observe voltage sag.

Do not infer polarity only from spring shape.

Detailed working notes: `docs/BOARD_DIAGNOSTICS.md`.

### Historical built-in self-test

Historical K210 `sd/main.py` can enter test mode by holding the left/A button during boot. It runs `/sd/device_test.py` and tests LCD, camera, microphone, SD card, speaker, A/B/C buttons and LEDs.

See `docs/FACTORY_SELF_TEST.md`.

### Historical motion-controller interface

XGO-Mini Communication Protocol V1.0 documents:

- standard TTL serial;
- XH2.54 4-pin;
- 115200 baud, 8N1;
- two motherboard serial connectors;
- 3.3 V connector occupied by AI module by default.

### Public schematic status

No public board-level schematic/boardview for the photographed original `XGO MINI V2.5` / 2021 lower board has yet been found. Current diagnostic basis is period documentation + photographed silkscreen + continuity/voltage mapping.

### Firmware compatibility warning

Do **not** flash current ESP32 M-series XGO-Mini firmware onto this original K210 + STM32 generation.

## Legacy robot arm

Status: physically available according to project context, technical details not yet recorded.

Still needed: photos, motor/servo types, controller board, power supply, communication interface and original university code/project files if available.
