# CURRENT_STATE

Updated: 2026-09-06

## Status

The project direction has changed from repairing the unsupported 2021 STM32 V2.5 lower board to a **vendor-supported ESP32 retrofit** while preserving the original XGO-Mini chassis and 12 servos.

Luwu Dynamics / XGO confirmed directly that they can supply an **ESP32-based replacement driver board + compatible battery kit for USD 75 including shipping to Hungary**. They explicitly confirmed that this replacement board is designed to work with the **original chassis and all 12 original servos**.

This is now the preferred recovery path unless a materially better/cheaper official option appears. The old STM32 board can remain as a reverse-engineering/archive item, but repairing it is no longer the primary objective.

## Vendor-confirmed retrofit facts — 2026-09-06

Pengfei (Bency) Liu / Luwu Dynamics confirmed:

- replacement board is **ESP32-based**, not the old STM32 V2.5 generation;
- it is adapted to the original XGO-Mini chassis and **existing 12 servos**;
- it runs the standardized underlying XGO serial protocol;
- standard locomotion, pose and kinematics calls are compatible with **`xgolib`**;
- exact firmware version / model identifier and command mapping sheet will be provided with the replacement board;
- board exposes **3.3 V TTL UART** (`TX/RX/GND`) for external Raspberry Pi / SBC / PC control;
- direct Raspberry Pi GPIO connection is supported without a level shifter on that UART;
- current Lite3 / CM5 AI modules and current modular robotic arms are **not direct plug-and-play** with the old chassis because of mechanical, cable-routing and newer integration differences;
- custom upper-layer development is expected to be done as secondary development;
- vendor will not provide the legacy servo bus protocol, legacy board schematic or full legacy hardware documentation;
- current practical official solution is the ESP32 replacement board + battery kit.

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
custom modern upper controller
  - Raspberry Pi / CM / other SBC
  - inexpensive modern display/HMI
  - modern camera
  - microphone / speaker as needed
  - Wi-Fi / network access
  - Local GPU Helper / PC for heavier AI
```

The motion layer should stay vendor-compatible. The upper AI/HMI layer should be treated as replaceable and project-owned.

## HMI / camera direction

The old K210 display/camera module is no longer considered strategically important.

If it happens to work with the new board, it may be useful temporarily, but the preferred long-term direction is a **new simple display + camera + SBC** rather than carrying the old K210 firmware/software constraints forward.

There is no requirement to buy a complete Lite3/mini2-class robot or a full current-generation head assembly. A low-cost custom HMI is acceptable and likely preferable for education/research.

## Battery direction

Original robot uses two removable 18650-format cells and historical specification is 7.4 V / 2500 mAh.

Known old cells were degraded; one original cell was later measured around ~1 V during troubleshooting, while replacement/test cells around ~3.7 V did not revive the old STM32 board.

Because the vendor quote includes a compatible battery, the exact battery requirement of the new ESP32 retrofit should be recorded when the kit details arrive.

Potential cost optimization for later discussion only:

- if the replacement board accepts a standard 2S 18650 arrangement and no proprietary pack/BMS is required, Tamás can source suitable cells locally;
- if vendor battery/connector/BMS is specific to the retrofit, use the supplied kit.

No new email is required now; wait for the vendor's next response/invoice before changing the order scope.

## Robot arm / future expansion

Current-generation Lite3/mini2 robotic-arm modules are **not plug-and-play** on the old chassis according to the vendor.

This does not prohibit future custom manipulation work. It means:

- do not assume current arm hardware mechanically/electrically drops in;
- first revive locomotion with the ESP32 retrofit;
- later evaluate a custom gripper/arm or the separate legacy university robot arm;
- treat any arm integration as a separate secondary-development phase.

## Current milestone

### M1 — procure and validate ESP32 retrofit

Pending:

1. receive vendor invoice/payment link;
2. confirm final shipping details and exact kit contents;
3. order the ESP32 replacement board + battery kit if no better official option is offered;
4. record exact replacement-board firmware/model identifier when received;
5. record supplied connector/pinout/command mapping;
6. install board into original chassis and connect original 12 servos;
7. perform first vendor-baseline motion test;
8. verify UART control from PC/Pi using the supplied mapping / `xgolib`;
9. only then design the custom modern HMI/camera layer.

## Procurement context

Original XGO-Mini was backed on Kickstarter in 2021 for approximately **USD 624 total** including shipping. The current goal is not to obtain a newer USD 1000+ robot cheaply; it is to revive and modernize the already-owned platform at the lowest sensible cost.

A roughly USD 75 ESP32 motion-controller retrofit is considered reasonable if it restores reliable locomotion and provides a current, documented development interface.

## Superseded troubleshooting path

The following work remains documented but is no longer the primary path:

- repair/reverse-engineer original STM32 V2.5 power path;
- recover old K210 firmware stack;
- identify COM3 ownership on the legacy electronics;
- locate original board schematic / servo protocol.

Keep these notes for reference, but do not spend additional time on them unless the ESP32 retrofit fails or becomes unavailable.

## Do not do now

- do not continue blind component-level repair of the old STM32 board;
- do not buy a complete Lite3 / mini2-class robot solely to modernize this chassis;
- do not assume current Lite3/CM5 head or current robotic arm is plug-and-play;
- do not design the new HMI around undocumented legacy K210 behavior;
- do not create another support email until the vendor responds or an ordering decision requires clarification.
