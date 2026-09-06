# HARDWARE

Updated: 2026-09-06

## XGO-Mini — original Kickstarter/K210 generation

Status: original 2021 lower-board electronics are no longer the preferred repair target. Vendor-supported retrofit path is available.

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

## Vendor-supported ESP32 replacement — confirmed 2026-09-06

Luwu Dynamics / XGO offered a new replacement package for the original chassis.

### Confirmed compatibility

Vendor explicitly confirmed:

- replacement lower board is **ESP32-based**;
- it is a newer adapted revision, not the original STM32 V2.5 board;
- it is designed to work with the **existing original XGO-Mini chassis**;
- it is designed to work with the **original 12 servos**;
- normal locomotion can therefore be restored without replacing the mechanical platform or the 12 leg servos.

This is the most important hardware compatibility fact for the retrofit.

### Control interface

Vendor confirmed:

- standardized underlying XGO serial protocol;
- compatibility with the core `xgolib` command set for standard locomotion, pose adjustments and kinematics calls;
- onboard external UART intended for Raspberry Pi / SBC / PC;
- UART logic level: **3.3 V TTL**;
- interface signals stated as `TX/RX/GND`;
- direct connection to Raspberry Pi GPIO is supported without level shifting;
- exact firmware version/model identifier and command mapping sheet will be supplied with the replacement board.

### Package / price

Quoted package:

- ESP32 replacement driver board;
- compatible battery kit;
- shipping to Hungary included;
- total: **USD 75**.

Exact connector set / adapter cabling is still to be confirmed when the order is prepared.

### Battery

Original chassis uses removable 18650 cells, but the exact power implementation expected by the new ESP32 replacement board is not yet documented in the repository.

Do not assume the replacement can use any arbitrary 2S holder until the supplied wiring/connector/BMS arrangement is known.

If the vendor later confirms that a standard 2S 18650 arrangement is acceptable, locally sourced matched cells may be used as a cost-saving option. Until then the compatible vendor battery kit is the safe baseline.

## Upper module / HMI implications

### Legacy K210 module

The old K210 display/camera module is no longer required for the target architecture.

It may be retained for archival/testing purposes, but the preferred modern path is a separate SBC-based upper controller.

### Current Lite3 / CM5 / arm modules

Vendor confirmed that current Lite3 / CM5 AI modules and modular robotic arms are **not direct plug-and-play** with the original chassis because of newer mounting, cable routing and integration architecture.

Therefore:

- do not assume current-generation head assemblies will physically fit;
- do not assume current robotic-arm modules will electrically/mechanically attach directly;
- these may still serve as design references for custom secondary development.

## Target hardware architecture

```text
Original 2021 aluminum chassis
        |
Original 12 leg servos
        |
Vendor ESP32 replacement motion board
        |
3.3 V TTL UART
        |
Custom Raspberry Pi / CM / SBC upper controller
        |-- inexpensive display
        |-- modern camera
        |-- microphone / speaker
        |-- Wi-Fi / network
        `-- Local GPU / PC integration
```

This architecture intentionally separates the vendor-supported motion layer from the user-owned AI/HMI layer.

## Legacy robot arm

A separate university-era robot arm is also available. It remains an independent future device until its controller, actuators, power and interface are identified.

A current XGO arm is not assumed compatible with this old chassis.
