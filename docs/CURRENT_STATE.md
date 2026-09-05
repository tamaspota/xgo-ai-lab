# CURRENT_STATE

Updated: 2026-09-05

## Status

Original 2021 XGO-Mini hardware generation is identified as **K210 + STM32**. The current blocker is the **battery / power path**, not firmware. The robot is opened and the lower/controller board is exposed.

Both original 18650 cells now measure normal-looking open-circuit voltage: approximately **3.74 V** and **3.70 V**. The robot still does not start from the normal power switch. This means the cells are not obviously deeply discharged, but open-circuit voltage does not prove current capability; aged cells can still collapse under load.

A public board-level schematic/boardview for this exact original lower board has not yet been found. Diagnosis is therefore proceeding from period XGO documentation, photographed silkscreen and continuity/voltage mapping.

## Confirmed

- target robot: original Kickstarter-era XGO-Mini;
- repository: `tamaspota/xgo-ai-lab`;
- local checkout: `C:\projects\xgo-ai-lab`;
- architecture: K210 high-level/AI module + STM32 motion controller;
- period battery specification: 7.4 V 2500 mAh, standard 18650, 3C discharge;
- actual battery implementation: two removable 18650-format cells in chassis holder;
- measured original cell voltages: ~3.74 V and ~3.70 V;
- normal battery-powered startup still fails;
- lower-board silkscreen/date photo clearly shows **20211027**;
- `SWITCH` harness is physically connected during normal startup attempts;
- lower board exposes micro-USB, DOWNLOAD/CALIBRATE switches and multiple 4-pin connectors;
- a populated white 4-pin connector sits directly next to silkscreen `G CLK DIO 3V3`;
- original XGO-Mini Communication Protocol V1.0 documents **two 4-pin TTL serial connectors** on the motherboard, with 5 V and 3.3 V supply variants; the 3.3 V connector is occupied by the AI module by default;
- USB enumeration previously worked through Silicon Labs CP210x/CP2102 on COM3, VID:PID `10C4:EA60`;
- installed K210 firmware text approximately matches `xgo-210722`;
- current ESP32-generation XGO firmware must not be flashed to this original STM32 generation.

## Connector interpretation

### `G CLK DIO 3V3`

Correction: this is **not a test point**. It is silkscreen adjacent to a physically populated white 4-pin connector.

Engineering inference only: the names are highly consistent with STM32 SWD (`GND`, `SWCLK`, `SWDIO`, `3.3 V reference`). Do not connect ST-Link until continuity/voltage confirms the interpretation.

### 4-pin connectors near lower-board micro-USB

The photographed layout now matches the original protocol statement that the motherboard has two serial connectors. Working hypothesis: these are the documented 5 V / 3.3 V TTL UART interfaces, with one used by the AI module. Exact pin order still needs a clearer silkscreen read or continuity mapping.

### COM3 ownership

COM3 must now be treated as **unresolved**. It may belong to the K210 path or to lower-board service/programming hardware. Do not build further assumptions on COM3 until physical routing is mapped.

## Current milestone

### M1 — identify pack rails and restore stable power

Completed:

1. original K210 + STM32 architecture verified;
2. historical STM32 TTL protocol documented;
3. historical K210 recovery material and factory self-test found;
4. battery compartment opened: two removable 18650 cells confirmed;
5. lower/controller board service connectors exposed;
6. both original cells measured at ~3.7 V open circuit;
7. lower-board date `20211027` recorded;
8. connector map/reverse-engineering notes added in `docs/BOARD_DIAGNOSTICS.md`.

## Next action

Do **not** flash firmware or remove the lower board yet.

With USB disconnected and cells removed:

1. use continuity mode to map accessible battery-holder solder tabs to the four metal cell contacts;
2. identify the 2S series bridge, if directly visible in continuity;
3. the remaining two rails are the expected pack endpoints;
4. install two matched cells with verified polarity;
5. measure pack voltage across those end rails — expected magnitude with the current cells is about 7.4 V;
6. press the power switch while watching the same voltage for collapse.

If pack voltage stays healthy during switch press, trace voltage forward to the first board input/power rail. Only then investigate switch/latch/DC-DC/MCU state.

## Supporting evidence

A RobotShop support case describes essentially the same K210 XGO-Mini symptom — charger behavior normal but power switch produces no startup — and was resolved by replacement batteries. This makes battery/current-delivery failure plausible, but it does not prove the diagnosis for this unit.

## Architecture direction under consideration

If the original STM32 motion board proves healthy, retain:

- aluminum chassis;
- 12 original serial-bus servos;
- original STM32 motion controller.

Replace/bypass only the old K210 high-level layer later if justified, using modern SBC/PC compute, camera and display. Full lower-board replacement remains a fallback, not the default.

## Blockers

- holder/pack endpoint rails not yet electrically mapped;
- total pack voltage and switch-press voltage sag unknown;
- exact lower-board power topology/schematic unavailable;
- exact UART connector pin order not yet verified;
- COM3 physical routing uncertain;
- self-test/SD state still unknown because normal boot is unavailable.

## Do not do yet

- do not reverse 18650 polarity by trial;
- do not infer polarity only from spring shape;
- do not toggle CALIBRATE casually;
- do not flash current ESP32 XGO-Mini firmware;
- do not connect ST-Link to `G CLK DIO 3V3` until pin function is electrically verified;
- do not replace the STM32 board before the pack/power path is measured.

## Later scope

- safe Python control API;
- K210 bypass/replacement with Raspberry Pi/PC-class controller if justified;
- modern camera/display;
- child-friendly controls;
- voice/vision AI via PC or Local GPU Helper;
- separate legacy robot-arm station;
- coordinated multi-robot tasks.
