# BOARD_DIAGNOSTICS

Updated: 2026-09-05

## Scope

Power-path and connector mapping for the opened original XGO-Mini K210 + STM32 generation.

This file deliberately separates **confirmed observations**, **period documentation**, and **engineering inference**.

## Confirmed from current hardware

- Two removable 18650-format cells are used in the chassis holder.
- Individual measured open-circuit voltages reported 2026-09-05: approximately **3.74 V** and **3.70 V**.
- Normal power-button startup still produces no visible response.
- Lower/controller board is exposed.
- Board has a `SWITCH` connector for the external power switch harness.
- Board has lower-board micro-USB.
- Board has two small mode switches labelled DOWNLOAD and CALIBRATE.
- Board silkscreen/date visible in photos includes **20211027**.
- A white 4-pin connector is physically present immediately next to silkscreen `G CLK DIO 3V3`.
- At least two additional 4-pin connectors are visible near the lower-board micro-USB.
- The battery holder has a visible `+` marking in the photographed upper cell bay.

## Correction to earlier wording

`G CLK DIO 3V3` should not be called a "test point". It is silkscreen adjacent to a populated 4-pin connector. The labels are strongly suggestive of a debug interface, but the electrical function has not yet been verified.

## Period documentation that matches the board layout

The original XGO-Mini Communication Protocol V1.0 specifies:

- standard TTL serial communication;
- XH2.54 4-pin interface;
- 115200 baud, 8 data bits, 1 stop bit, no parity;
- **two serial communication interfaces on one side of the motherboard**;
- terminal supply options of **5 V** and **3.3 V**, not to be used simultaneously;
- the **3.3 V terminal is occupied by the AI module by default**.

This matches the photographed lower-board layout much better than the earlier assumption that all visible 4-pin connectors were generic service ports.

## Connector interpretation from photo + period protocol

### `G CLK DIO 3V3` 4-pin connector

Engineering inference only:

- `G` -> likely GND;
- `CLK` -> likely SWCLK;
- `DIO` -> likely SWDIO;
- `3V3` -> likely target-voltage reference.

This is highly consistent with STM32 SWD naming, but must be verified by continuity/voltage before connecting ST-Link.

### 4-pin connectors near lower-board micro-USB

Period documentation says there are two motherboard TTL serial connectors with 5 V and 3.3 V supply options. The photographed board shows two 4-pin connectors in the expected area, one carrying colored wires.

Working hypothesis:

- these are the documented TTL serial interfaces;
- one is likely the AI-module link;
- one may be the exposed external host interface.

Do not assign exact pin order until the silkscreen is photographed/read clearly.

## Battery diagnosis

Open-circuit cell voltage around 3.7 V does **not** prove a cell can supply the robot. Aged cells can show normal unloaded voltage and collapse under load.

RobotShop legacy specification describes the original battery as standard **18650, 2500 mAh, 3C discharge** cells in a 7.4 V system.

A RobotShop support case for the same XGO-Mini K210 symptom (charger behavior normal, power switch does nothing) was resolved by replacing the batteries. This is supporting evidence, not proof for this unit.

### How to identify pack rails without a schematic

With **all USB disconnected and cells removed**:

1. Use continuity mode to map each accessible battery-holder solder tab to its corresponding metal cell contact.
2. Identify whether any two holder contacts are directly joined as the 2S series bridge.
3. The two contacts not forming the series bridge are the pack end rails.
4. Only after the holder topology is known, install two matched cells with correct polarity.
5. Measure across the identified pack end rails; expected magnitude for two ~3.7 V cells is roughly **7.4 V**.
6. Repeat while pressing the power switch and watch for voltage collapse.

Do not infer polarity only from spring shape. Use the holder `+` marking and continuity mapping.

## What to measure next

Priority order:

1. Pack voltage across holder end rails with cells installed.
2. Pack voltage during power-button press.
3. If pack voltage stays healthy, trace that voltage to the first accessible board input/solder pad.
4. Then check whether logic rails appear after power-on.
5. Only after power-path status is known should SWD, boot/download mode, firmware or board replacement be investigated.

## Public documentation status

A public board-level schematic/boardview for the photographed `XGO MINI V2.5` / 2021 lower board has **not** yet been found. Current useful sources are:

- RobotShop legacy XGO-Mini K210 manual/datasheet;
- XGO-Mini Communication Protocol V1.0;
- historical XgoAI source/firmware tree;
- photographed silkscreen and connector layout from this unit.

Until a real schematic is found, board-level work should use continuity mapping and measured rails rather than guessed component functions.
