# CURRENT_STATE

Updated: 2026-09-05

## Status

Original 2021 XGO-Mini hardware generation is identified as **K210 + STM32**. The current blocker is the **battery / power path**, not firmware. The robot was opened and found to use two removable 18650-format cells in an internal holder. The original cells are now being tested separately in an XTAR VC2 charger and their actual voltages still need measurement.

The lower/controller board is now physically exposed. Its silkscreen includes `XGO MINI V2.5` according to Tamás, plus a 2021-era code/date marking. Visible service features include lower-board micro-USB, a `SWITCH` harness connector, a `G CLK DIO 3V3` 4-pin header, and DOWNLOAD/CALIBRATE mode switches.

## Confirmed

- target robot: original Kickstarter-era XGO-Mini;
- repository: `tamaspota/xgo-ai-lab`;
- local checkout: `C:\projects\xgo-ai-lab`;
- period hardware architecture: K210 high-level/AI module + STM32 motion controller;
- period battery specification: 7.4 V 2500 mAh;
- actual battery implementation observed: two removable 18650-format cells in a chassis holder;
- normal battery-powered boot currently fails after charging attempt;
- USB enumeration previously works through Silicon Labs CP210x/CP2102 on COM3, VID:PID `10C4:EA60`;
- installed K210 firmware text approximately matches `xgo-210722`, closely matching a historical July 22, 2021 recovery package;
- historical K210 app/self-test path and original STM32 TTL protocol have been located;
- current ESP32-generation XGO firmware must not be flashed to this original STM32 generation.

## New lower-board findings

Visible/service interfaces from the opened robot:

- micro-USB on the lower board;
- `SWITCH` 4-pin connector;
- `G CLK DIO 3V3` 4-pin header (P2);
- two board switches identified from silkscreen as DOWNLOAD and CALIBRATE;
- additional internal 4-pin connectors still unmapped.

`G CLK DIO 3V3` is strongly consistent with STM32 SWD (GND/SWCLK/SWDIO/3.3 V reference), but this is not yet electrically verified.

The exposed lower-board USB and service controls mean the previous working assumption that COM3 is necessarily the K210-side interface is now uncertain. It may be a lower-board service/programming interface. This must be mapped physically after stable power is restored.

## Current milestone

### M1 — restore stable power and map the original controller interfaces

Completed:

1. CP2102 driver/COM3 working.
2. Historical K210 + STM32 architecture verified.
3. Historical STM32 TTL protocol documented.
4. Historical K210 recovery material and factory self-test found.
5. Battery-powered startup failure identified.
6. Battery compartment opened: two removable 18650 cells confirmed.
7. Lower/controller board service connectors and switches exposed.
8. Likely STM32 SWD header identified from silkscreen.

## Next action

Do **not** replace the controller board or flash firmware yet.

First complete power diagnosis:

1. measure each original 18650 cell directly with a multimeter;
2. if either cell is severely low or not accepted by a normal charger, retire that cell rather than force-charge it;
3. use two known-good matched 18650 cells at similar state of charge for the next test;
4. measure holder/output voltage before connecting/booting;
5. attempt normal power-on and observe voltage sag.

Only after stable power is restored:

1. run the built-in factory/self-test;
2. map which USB connector produces COM3;
3. verify the `G CLK DIO 3V3` header electrically as SWD;
4. identify the internal UART between high-level controller and STM32;
5. then decide whether to keep or replace the K210/display layer.

## Architecture direction under consideration

No replacement decision has been made. The preferred modernization path, if the original STM32 motion board is healthy, is likely:

- keep chassis, 12 servos and original STM32 motion board;
- replace or bypass only the old K210 high-level layer if it becomes limiting;
- use a modern SBC/PC as the AI/vision/controller layer;
- attach a new display/camera to that high-level controller if useful.

This minimizes mechanical/electrical rework and preserves the robot-specific gait/servo controller. Full lower-board replacement should be considered only if the original motion board is actually faulty or its servo bus proves unusable.

## Blockers

- original 18650 cell voltages unknown;
- stable battery-powered boot not yet restored;
- exact lower-board model/silkscreen code not fully recorded;
- internal connector pinouts still unmapped;
- COM3 physical routing uncertain;
- self-test/SD state still unknown.

## Do not do yet

- do not force-charge deeply discharged Li-ion cells;
- do not use mismatched cells as a permanent pack;
- do not toggle CALIBRATE casually: calibration can alter servo reference data;
- do not flash current ESP32 XGO-Mini firmware;
- do not replace the STM32 board merely because the K210/display layer is old;
- do not assume COM3 interface ownership until physically verified.

## Later scope

- safe Python control API;
- replacement/bypass of K210 with Raspberry Pi/PC-class controller if justified;
- modern camera/display;
- child-friendly controls;
- voice/vision AI via PC or Local GPU Helper;
- separate legacy robot-arm station;
- coordinated multi-robot tasks.
