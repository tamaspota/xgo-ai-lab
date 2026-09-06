# ESP32 RETROFIT RESEARCH

Updated: 2026-09-06

Purpose: collect current, relevant XGO controller documentation and define what to verify when the vendor replacement board arrives. This file distinguishes **vendor-confirmed facts about the purchased retrofit board** from **current-generation reference material** that may or may not match the exact PCB revision shipped.

## 1. Purchased retrofit board — confirmed facts

Direct correspondence with Pengfei (Bency) Liu / Luwu Dynamics confirms:

- the replacement board is **ESP32-based**;
- it is a newer adapted replacement for the discontinued 2021 STM32 V2.5 lower board;
- it is intended to work with the **original 2021 XGO-Mini chassis**;
- it is intended to work with the **original 12 servos**;
- it uses the standardized underlying XGO serial command set;
- standard locomotion, pose and kinematics calls are compatible with `xgolib`;
- it exposes an external **3.3 V TTL UART** (`TX/RX/GND`) for Raspberry Pi / SBC / PC control;
- direct Raspberry Pi GPIO UART connection is supported without a level shifter;
- vendor will provide the exact firmware/profile and command mapping for the shipped board;
- current Lite3 / CM5 integrated head modules and current modular robotic arms are not direct plug-and-play upgrades for the 2021 chassis.

Procurement state:

- chosen option: **Option 1 — replacement ESP32 driver board only**;
- price: **USD 50, shipping included**;
- paid via PayPal on 2026-09-06;
- battery kit intentionally omitted to reduce cost;
- waiting for shipment / tracking / exact board information.

## 2. Current XGO driver-board family — official 2026 reference

The current Luwu/XGO common hardware documentation, updated 2026-08-14, describes the modern XGO quadruped driver-board family as follows:

- main controller: **ESP32-WROVER-B**;
- integrated IMU;
- servo connectors;
- power connector;
- power-switch connector;
- external serial communication supporting **5 V / 3.3 V** interfaces;
- servo-reset and ESP32-reset controls;
- high-current DC-DC subsystem capable of **5 V / 6 A continuous output**;
- status LEDs for power, IMU and servo-communication fault state.

The page explicitly shows an **XGO-mini2** driver board and links an `XGOMINI.pdf` schematic.

Official source:
- https://wiki.xgorobot.com/kb/common-resources/cmsss6atk0021mb24fnrmxahr

Important: this is a **reference family**, not proof that the purchased retrofit PCB is exactly the same XGO-mini2 board. The vendor described the purchased board as an adapted replacement revision. Exact identity must be established from the physical board and supplied firmware/profile.

## 3. Current firmware family / model prefixes

The current XGO firmware-update guide, updated 2026-08, documents ESP32 driver-board firmware prefixes:

- `M` — XGO-mini2S;
- `L` — XGO-lite3;
- `R` — XGO-Rider2;
- `W` — XGO-mini3W.

The current flashing procedure uses ESP32 Flash Download Tool, UART mode and 115200 baud. Current documentation warns that the body/driver-board USB interface is the flashing target, not the upper/head computer USB interface.

Official source:
- https://wiki.xgorobot.com/kb/common-resources/83a7395c0f00416bb26303803de5b1e5

**Do not flash any of these current firmware packages onto the incoming retrofit board until its exact model/profile is confirmed by the vendor and by the board itself.**

## 4. Current `xgolib` behavior

Current official repository:
- https://github.com/LuwuDynamics/xgo_doglib

Current package observed on 2026-09-06:
- `xgolib` version: **1.4.2**;
- default serial baud: **115200**;
- supported dog profiles include `xgomini`, `xgolite`, `xgomini3W`;
- auto-detection reads firmware and maps prefixes `M`, `L`, `W`; `R` selects Rider handling.

Caution: current `XGO()` auto-detection constructs a dog object, reads firmware and invokes reset behavior during detection. Therefore the first test of the incoming board should follow the vendor-supplied profile/mapping and be done with the robot safely placed, not by blindly running auto-detection while holding the chassis.

## 5. XGO2 architecture reference

ELECFREAKS documentation for XGO2 describes the same general architecture that the retrofit is moving toward:

- ESP32 lower/slave controller manages power, servo drive and gait;
- upper Raspberry Pi CM4/CM5 host communicates with the lower controller via serial;
- aluminum structure + serial-bus servos;
- 4-pin host-to-driver cable;
- two 18650 lithium cells in the robot;
- XGO-mini2 driver board controls bus servos and can report servo position/load/voltage/mode information;
- XGO-mini2 driver-board schematic is publicly linked from that documentation.

Reference:
- https://wiki.elecfreaks.com/en/pico/cm4-xgo-robot-kit/xgo2-overview/

This is useful for connector/schematic comparison after the board arrives, but should not override the vendor's retrofit-specific documentation.

## 6. Battery expectation

The original 2021 robot used a 7.4 V / 2S arrangement with removable 18650-format cells. XGO2 documentation also describes two 18650 cells.

Current project decision:

- do **not** buy a battery before the new board arrives;
- Tamás already owns multiple 18650 cells from an older solar project;
- for the first brief test, use two matched, healthy cells only after the incoming board's polarity, holder wiring, connector and voltage requirements are verified;
- a 1–2 minute motion test is sufficient to establish that the retrofit works;
- if voltage sags or the board resets under servo load, obtain a matched high-current pair later;
- LiPo conversion is a later option only after confirming the board's allowed voltage range, power connector, protection and charging assumptions.

## 7. Upper controller / display / camera options

No upper-module purchase is required before validating locomotion.

### Option A — legacy K210 head, temporary

The original K210 display/camera module may be tested later if its UART behavior is compatible with the standardized ESP32 motion protocol. It is not a design dependency and no further money should be spent specifically to preserve it.

### Option B — Raspberry Pi 4B or other SBC

The vendor explicitly confirms 3.3 V TTL UART for Raspberry Pi / SBC / PC. A Pi 4B already available to the project is therefore a practical upper controller for:

- Wi-Fi/network control;
- camera;
- web UI;
- optional display;
- microphone/speaker;
- offload to PC / Local GPU Helper.

No level shifter should be required for the confirmed 3.3 V UART, but TX/RX/GND pin order must still be verified from the shipped board documentation.

### Option C — ESP32-S3 compact upper HMI

Luwu Dynamics' current open-source `RIG-Omni` project demonstrates a low-cost ESP32-S3 architecture combining:

- Wi-Fi / BLE;
- 240x240 SPI LCD;
- camera (GC0308 / OV2640);
- I2S audio;
- IMU;
- XGO UART protocol;
- OTA and remote/MCP features.

Official repository:
- https://github.com/LuwuDynamics/rig_omni

This is **not** a drop-in XGO-Mini2 head and is not known to be compatible mechanically with the 2021 chassis. It is a useful design reference if a compact custom display/camera/Wi-Fi upper board is preferred over Raspberry Pi later.

## 8. Arrival inspection checklist

Before installation or flashing:

1. photograph the incoming board **front and back** at high resolution;
2. record all silk-screen markings, PCB revision and date codes;
3. identify exact ESP32 module marking (`ESP32-WROVER-B`, other ESP32, etc.);
4. identify USB connector type and USB-UART/programming circuitry;
5. record power-input connector and polarity;
6. record switch connector and any adapter harness supplied;
7. record all servo connectors and labels;
8. identify 3.3 V UART header and exact TX/RX/GND pin order;
9. note reset / servo-reset / boot controls;
10. compare physical layout against the current XGO-mini2 board/schematic reference;
11. record vendor-supplied firmware/model identifier and command mapping;
12. do **not** flash firmware before this identification is complete.

## 9. First bring-up sequence

Preferred minimal test path:

1. mount/connect the new board only to the original chassis, switch and 12 servos;
2. use a matched known-good battery pair with verified polarity and voltage;
3. place robot on a flat stable surface with clearance around legs;
4. power on and observe board LEDs / servo-error state;
5. verify normal vendor baseline startup before attaching a Pi or custom HMI;
6. connect PC/Pi UART only after the board boots normally;
7. test firmware query / model ID first;
8. then test one safe low-risk `xgolib` command at low movement amplitude;
9. verify all four legs and servo groups before running full action sequences;
10. only after motion is stable decide whether to reuse K210, use Pi 4B, or build an ESP32-S3 upper module.

## 10. Current working hypothesis

It is plausible that the shipped retrofit is physically close to a current XGO-mini2-family ESP32 driver board or a small adaptation of it, because:

- vendor says standardized XGO serial protocol;
- original 12 servos are explicitly supported;
- current XGO quadruped driver boards are ESP32-based;
- current XGO architecture separates ESP32 motion control from the upper compute layer through UART.

However, this remains a **hypothesis until the board arrives**. Connector compatibility is likely but not assumed. If connector housings differ while electrical/protocol compatibility is confirmed, adapter cables or connector replacement are acceptable project work.
