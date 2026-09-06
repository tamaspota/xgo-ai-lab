# CURRENT_STATE

Updated: 2026-09-06

## Status

The project has moved from repairing the unsupported 2021 STM32 V2.5 lower board to a **vendor-supported ESP32 retrofit** while preserving the original XGO-Mini chassis and 12 servos.

The selected retrofit has now been **ordered and paid**:

- **Option 1: ESP32 replacement driver board only**;
- price: **USD 50**;
- shipping to Hungary included;
- payment completed via PayPal on 2026-09-06;
- battery intentionally omitted because compatible cells can be sourced locally if the board uses the expected 2S/18650 power arrangement;
- current state: **WAITING FOR SHIPMENT / TRACKING / EXACT BOARD DETAILS**.

The old STM32/K210 electronics are now archival/fallback hardware. Component-level repair is no longer the main task.

## Vendor-confirmed retrofit facts — 2026-09-06

Pengfei (Bency) Liu / Luwu Dynamics confirmed:

- replacement board is **ESP32-based**, not the old STM32 V2.5 generation;
- it is an adapted replacement intended for the original XGO-Mini chassis;
- it works with the **existing original 12 servos**;
- it runs the standardized underlying XGO serial protocol;
- standard locomotion, pose and kinematics calls are compatible with **`xgolib`**;
- exact firmware version/model identifier and command mapping will be provided for the shipped board;
- board exposes **3.3 V TTL UART** (`TX/RX/GND`) for external Raspberry Pi / SBC / PC control;
- direct Raspberry Pi GPIO UART connection is supported without a level shifter;
- current Lite3 / CM5 AI modules and current modular robotic arms are **not direct plug-and-play** with the old chassis because of generational mechanical/electrical integration differences;
- custom upper-layer development is expected to be secondary development;
- vendor will not provide the legacy servo bus protocol, legacy board schematic or full legacy hardware documentation.

## Current-generation reference research

Current official XGO documentation, updated 2026-08, shows the present quadruped driver-board family using **ESP32-WROVER-B**, onboard IMU, servo/switch/power connectors, 5 V / 3.3 V serial interfaces, reset controls and a high-current 5 V / 6 A DC-DC subsystem.

Current firmware documentation identifies present ESP32 profiles by prefix:

- `M` — XGO-mini2S;
- `L` — XGO-lite3;
- `R` — XGO-Rider2;
- `W` — XGO-mini3W.

Current official `xgolib` observed version is **1.4.2**, using 115200 baud by default and firmware-prefix auto-detection.

These are useful comparison references only. **Do not assume the purchased retrofit PCB is exactly the current XGO-mini2 board until the physical board and vendor-supplied firmware/profile are inspected.**

Detailed notes: `docs/ESP32_RETROFIT_RESEARCH.md`.

## Intended architecture

Preferred target architecture:

```text
original 2021 aluminum XGO chassis
          +
original 12 servos
          +
new vendor ESP32 motion controller
          |
          | 3.3 V TTL UART / xgolib-compatible command set
          v
optional modern upper controller
  - existing Raspberry Pi 4B / other SBC, or
  - compact ESP32-S3 HMI, or
  - legacy K210 temporarily if useful
          |
          +-- camera
          +-- optional display
          +-- microphone / speaker
          +-- Wi-Fi / network access
          `-- PC / Local GPU Helper for heavier AI
```

The motion layer should stay vendor-compatible. The upper AI/HMI layer is intentionally replaceable and project-owned.

## HMI / camera direction

Do **not** buy a new display/camera module before validating the new motion board.

The final display may not need to be large at all if the main UI is phone/web based. A small local screen could be used only for status, face/animation, battery/Wi-Fi state and debug information.

Possible upper-layer paths after motion works:

1. test the old K210 head over UART if convenient;
2. use the existing Raspberry Pi 4B over the vendor-confirmed 3.3 V UART;
3. later build a compact ESP32-S3 display/camera/Wi-Fi upper module if a smaller embedded solution is preferable.

Luwu Dynamics' open-source `RIG-Omni` ESP32-S3 project is a useful design reference for option 3, but is not assumed to be a drop-in XGO head.

## Battery direction

Board-only was chosen because it reduces the retrofit cost from USD 75 to **USD 50**.

Tamás already has multiple 18650 cells from an older solar project. No new battery should be purchased before the incoming board's exact voltage, connector, polarity and protection expectations are checked.

First-test rule:

- use two matched, healthy cells only after power requirements are verified;
- a short 1–2 minute functional motion test is enough to prove the retrofit works;
- if cells sag/reset the board under servo load, buy a matched high-current pair later;
- LiPo conversion is possible only after the board's permitted voltage range and power/charging design are known.

Current XGO2 reference material also uses two 18650 cells, but this does not by itself prove the retrofit board's exact battery wiring.

## Current milestone

### M1 — receive and identify the purchased ESP32 retrofit

Pending:

1. vendor ships the paid board and provides tracking;
2. receive exact firmware/model identifier and command mapping;
3. photograph the board front/back before installation;
4. record PCB revision, ESP32 module, connector labels and pinouts;
5. compare physical layout with current XGO-mini2-family reference material;
6. verify power input and select a matched local battery pair;
7. install board into original chassis and connect all 12 servos + switch;
8. perform minimal vendor-baseline startup test;
9. verify UART and `xgolib` control only after normal boot;
10. then decide K210 vs Pi 4B vs ESP32-S3 upper-layer path.

## Arrival safety / identification rules

- do not flash any firmware before the incoming board is identified;
- do not assume current `M`-series firmware is correct merely because the board is ESP32-based;
- do not assume connector polarity/order from visual similarity alone;
- do not run full action sequences as the first motion test;
- place the robot on a flat surface with leg clearance before initialization;
- retain all supplied adapter cables and photograph their routing before modifying connectors.

## Procurement context

Original XGO-Mini was backed on Kickstarter in 2021 for approximately **USD 624 total** including shipping.

The objective is not to obtain a newer USD 1000+ robot cheaply. The objective is to reuse the already-owned aluminum mechanics and 12 servos while replacing the unsupported motion electronics at minimum sensible cost.

The board-only purchase at **USD 50 shipped** is now the chosen cost-effective recovery path.

## Superseded troubleshooting path

The following work remains documented but is no longer primary:

- repair/reverse-engineer original STM32 V2.5 power path;
- recover old K210 firmware stack;
- identify COM3 ownership on the legacy electronics;
- locate original board schematic / servo protocol.

Keep these notes for reference, but do not spend additional time on them unless the ESP32 retrofit fails or becomes unavailable.
