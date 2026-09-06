# XGO BOARD FAMILY — 2026 REFERENCE

Updated: 2026-09-06

Purpose: map the current XGO product families to their known lower motion-controller and upper-compute architecture, so the incoming retrofit board can be identified quickly on arrival.

Important: this is a **reference matrix**, not proof of the exact board being shipped for the 2021 retrofit. The vendor described the purchased board as an adapted ESP32 replacement revision for the original 12-servo chassis.

## Current family matrix

| Product family | Form | Lower motion controller / driver board | Firmware/profile | Upper compute / HMI | Confidence / notes |
| --- | --- | --- | --- | --- | --- |
| **XGO-mini2S** | 12-DOF quadruped | Current XGO-MINI family driver board, ESP32-based; common hardware docs show **ESP32-WROVER-B**, integrated IMU, servo/power/switch connectors, 5V/3.3V serial interfaces and 5V/6A DC-DC | **M** prefix / `xgomini` | CM5 Lite **4 GB** on current AI module; 2.0" 320x240 IPS, 5 MP CSI camera, MEMS mic, speaker, Wi-Fi/BLE | **High**. Best current reference for the incoming retrofit because the vendor confirmed original 12-servo compatibility and standardized XGO/xgolib command set. Exact PCB revision still unknown. |
| **XGO-lite3** | smaller quadruped, arm-oriented | Current XGO-LITE family driver board, ESP32-based; common docs show separate XGOLITE board family with similar UART/power/IMU architecture | **L** prefix / `xgolite` | CM5 Lite **2 GB** current standard; same general XGO AI-module HMI architecture | **High**. Similar software architecture, but Lite geometry/servo limits differ, so it is less likely than M-family as the retrofit profile. |
| **XGO-mini2SW / mini3W line** | wheeled quadruped | ESP32-based dog-family controller; current public docs expose `xgomini`-style Python API and wheel-control functions, while common firmware docs still label the wheel family **W = mini3W** | **W** in common firmware guide; current mini2SW naming is not perfectly consistent across public docs | CM5 Lite **4 GB** shown as standard for mini3W / mini2s class | **Medium**. Useful software/architecture reference, but wheel outputs and firmware differ from the plain 12-servo quadruped. Do not flash W firmware to retrofit unless vendor explicitly identifies it. |
| **XGO-Rider2** | self-balancing two-wheel legged robot | Separate **XGOR/V1** ESP32 driver-board family; includes servo, power, external serial and wheel/FOC-specific control architecture | **R** prefix / Rider handler | CM5 Lite **2 GB** current standard | **High**. Clearly a different motion-controller family; not a likely retrofit board for the old quadruped. |
| **XGO-Ranger** | newer wheel-leg research platform | Exact lower-board revision not identified in the currently reviewed public docs; product uses CM5 plus dedicated low-level wheel/servo control and high-rate IMU/FOC architecture | Not established from reviewed docs | **CM5** | **Low/medium**. Interesting future reference for wheel-leg control only; not a plausible direct board match without vendor confirmation. |
| **RIG-Puppy / Hover / Arm / Core** | compact companion / desktop robots | **ESP32-S3** is the main embedded compute platform in the open-source RIG-Omni architecture; GC9A01 display, camera, I2S audio, IMU, Wi-Fi/BLE, XGO UART protocol | RIG-specific ESP-IDF builds | No Raspberry Pi required for core RIG stack | **High** for RIG, but this is a separate product architecture, not the XGO quadruped driver board. Useful as a custom upper-HMI reference. |

## Common current XGO driver-board characteristics

Official 2026 XGO common hardware documentation describes the current quadruped driver-board family with:

- **ESP32-WROVER-B** main MCU;
- integrated IMU;
- dedicated servo connectors;
- power and switch connectors;
- external serial interfaces supporting **5 V / 3.3 V**;
- servo-reset and ESP32-reset controls;
- high-current DC-DC capable of **5 V / 6 A continuous output**;
- status LEDs for power, IMU and servo communication state.

The common page explicitly separates the quadruped boards into **XGOMINI** and **XGOLITE** families and shows a separate **XGOR/V1** family for Rider.

## Firmware family map

Current official driver-board firmware guide:

- `M` -> XGO-mini2S
- `L` -> XGO-lite3
- `R` -> XGO-Rider2
- `W` -> XGO-mini3W

All are ESP32 lower-controller firmware families. Do not cross-flash between profiles.

## Current upper-compute map

Current official XGO AI-module documentation:

- **Lite3 / Rider2:** CM5 Lite 2 GB standard;
- **Mini2S / mini3W class:** CM5 Lite 4 GB standard;
- common current HMI: 2.0" 320x240 IPS, 5 MP CSI camera, MEMS microphone, speaker, Wi-Fi, Bluetooth, UART to lower controller.

For this retrofit, the upper compute is **not** a limiting dependency because an existing Raspberry Pi 4B can provide Wi-Fi, camera, sensors, UI and network/AI integration over the vendor-confirmed 3.3 V UART.

## Most likely incoming retrofit identity

Working probability order before physical inspection:

1. **M / XGO-MINI-family adapted ESP32 board** — most plausible;
2. custom/legacy-chassis-compatible ESP32 board derived from the same XGO-MINI controller design;
3. L/XGOLITE-derived board with custom firmware — possible but less likely because geometry and servo limits differ;
4. W/R/Ranger-specific board — unlikely for a plain 12-servo quadruped unless heavily repurposed.

This ranking is an engineering inference only. The board's silk-screen, ESP32 module, connector layout, firmware prefix and vendor command mapping will decide the actual identity.

## Arrival identification keys

Check, in this order:

1. PCB silk-screen name/revision/date;
2. exact ESP32 module (`ESP32-WROVER-B` or other);
3. number and layout of servo connectors;
4. power/switch connector layout;
5. 3.3 V / 5 V UART headers;
6. USB/programming interface;
7. firmware string (`M`, `L`, `W`, `R`, or custom);
8. vendor-supplied initialization profile and command mapping;
9. physical comparison against current XGOMINI / XGOLITE schematics.

## Sources

- Official XGO common control-system hardware: https://wiki.xgorobot.com/kb/common-resources/cmsss6atk0021mb24fnrmxahr
- Official driver-board firmware guide: https://wiki.xgorobot.com/kb/common-resources/83a7395c0f00416bb26303803de5b1e5
- Official resource/download center: https://wiki.xgorobot.com/kb/common-resources/f79a00a29e9f4a12a3f3c9a7d1313998
- Current XGO AI module / CM5 architecture: https://wiki.xgorobot.com/kb/zh-rider2/cmsra8xax005tjilgaqnyp4es
- XGO Lite3 development/API reference: https://wiki.xgorobot.com/kb/zh-lite3/cmsra8x4q001bjilgeidw0hp1
- Official RIG-Omni repository: https://github.com/LuwuDynamics/rig_omni
