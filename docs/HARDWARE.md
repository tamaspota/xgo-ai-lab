# HARDWARE

Updated: 2026-09-06

## XGO-Mini — original Kickstarter/K210 generation

Status: original 2021 lower-board electronics are no longer the preferred repair target. A vendor-supported ESP32 replacement board has been purchased.

### Original hardware

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
- battery cell description on legacy product material: standard 18650, 2500 mAh, 3C discharge;
- 12 DOF quadruped with serial-bus servos;
- original charger: 8.4 V / 1 A.

### Original board / failure observations

- lower-board date marking: `20211027`;
- old controller generation: STM32 / V2.5-era board;
- original K210 firmware text previously appeared approximately as `xgo-210722`;
- battery-powered startup failed despite testing replacement cells;
- old board showed some USB-powered activity but no reliable battery-powered startup;
- no obvious external burn/damage was observed on the old board;
- vendor states this generation is discontinued and no longer supported with official legacy schematics/firmware/support.

Historical reverse-engineering notes remain in `docs/BOARD_DIAGNOSTICS.md`, `docs/RECOVERY_SOURCES.md` and prior session logs.

## Vendor-supported ESP32 replacement — purchased 2026-09-06

### Confirmed compatibility

Vendor explicitly confirmed:

- replacement lower board is **ESP32-based**;
- it is a newer adapted revision, not the original STM32 V2.5 board;
- it is designed to work with the **existing original XGO-Mini chassis**;
- it is designed to work with the **original 12 servos**;
- normal locomotion can therefore be restored without replacing the mechanical platform or leg servos.

This is the critical retrofit compatibility fact.

### Control interface

Vendor confirmed:

- standardized underlying XGO serial protocol;
- compatibility with the core `xgolib` command set for standard locomotion, pose adjustments and kinematics calls;
- onboard external UART intended for Raspberry Pi / SBC / PC;
- UART logic level: **3.3 V TTL**;
- interface signals stated as `TX/RX/GND`;
- direct connection to Raspberry Pi GPIO is supported without level shifting;
- exact firmware version/model identifier and command mapping will be supplied for the replacement board.

### Purchased option / price

Chosen and paid:

- **Option 1: ESP32 replacement driver board only**;
- price: **USD 50**;
- shipping to Hungary included;
- payment: PayPal, completed 2026-09-06;
- battery not included.

Current state: waiting for shipment/tracking.

## Current ESP32 XGO driver-board family — reference only

Official current XGO hardware documentation updated 2026-08 describes modern quadruped driver boards using:

- **ESP32-WROVER-B**;
- onboard IMU;
- servo connectors;
- power connector;
- switch connector;
- external serial interfaces supporting **5 V / 3.3 V**;
- servo-reset and ESP32-reset controls;
- high-current **5 V / 6 A continuous** DC-DC output capability;
- power / IMU / servo-communication status LEDs.

The official page shows an XGO-mini2 board and links an `XGOMINI.pdf` schematic.

Reference:
- https://wiki.xgorobot.com/kb/common-resources/cmsss6atk0021mb24fnrmxahr

Do not assume the purchased board is exactly this PCB revision until it arrives.

### Current firmware reference

Current official firmware documentation maps:

- `M` -> XGO-mini2S;
- `L` -> XGO-lite3;
- `R` -> XGO-Rider2;
- `W` -> XGO-mini3W.

Current driver-board flashing uses an ESP32 UART workflow at 115200 baud, but no firmware should be flashed to the retrofit board until the exact shipped profile is confirmed.

Reference:
- https://wiki.xgorobot.com/kb/common-resources/83a7395c0f00416bb26303803de5b1e5

## Battery

The original chassis uses removable 18650-format cells and historically ran a 7.4 V / 2S arrangement. Current XGO2 reference material also describes two 18650 cells, but the exact power connector/protection arrangement of the purchased retrofit board is still unknown.

Tamás has several 18650 cells available from an older solar project.

Initial plan:

- wait for the board;
- verify exact power input, connector and polarity;
- use two matched healthy cells for a short 1–2 minute functional test;
- if voltage sag or resets occur under servo load, buy a matched high-current pair later;
- do not convert to LiPo until allowed voltage range, protection and charging assumptions are known.

## Upper module / HMI implications

### Legacy K210 module

The original K210 display/camera module may be tested later over UART if convenient, but is no longer required for the target architecture.

### Raspberry Pi 4B

The vendor-confirmed 3.3 V TTL UART makes an existing Raspberry Pi 4B a practical future upper controller for Wi-Fi, web UI, camera, audio and Local GPU/PC offload.

### ESP32-S3 compact upper HMI

Luwu Dynamics' open-source `RIG-Omni` project is a useful modern reference for a compact ESP32-S3 upper layer with:

- Wi-Fi/BLE;
- 240x240 SPI display;
- camera;
- I2S audio;
- XGO UART protocol;
- OTA / remote-control features.

Reference:
- https://github.com/LuwuDynamics/rig_omni

This is not assumed to be a drop-in XGO-Mini head. It is a possible future design pattern after locomotion is validated.

## Target hardware architecture

```text
Original 2021 aluminum chassis
        |
Original 12 leg servos
        |
Purchased vendor ESP32 replacement motion board
        |
3.3 V TTL UART
        |
Optional upper controller
        |-- legacy K210 temporarily, or
        |-- existing Raspberry Pi 4B, or
        `-- compact ESP32-S3 HMI
              |-- display
              |-- camera
              |-- Wi-Fi
              `-- audio / sensors as needed
```

Detailed current-generation comparison and arrival checklist: `docs/ESP32_RETROFIT_RESEARCH.md`.

## Legacy robot arm

A separate university-era robot arm is also available. It remains an independent future device until its controller, actuators, power and interface are identified.

A current XGO arm is not assumed compatible with this old chassis.
