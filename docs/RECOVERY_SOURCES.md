# Recovery sources

Updated: 2026-09-03

This file records external sources that are useful for recovering and modernizing the original 2021 Kickstarter-era XGO-Mini. Source quality is labeled explicitly because current XGO products use different controller hardware.

## 1. RobotShop legacy XGO-Mini product page — strong hardware match

URL:

- https://eu.robotshop.com/products/xgo-mini-quadruped-robot-dog

RobotShop identifies the discontinued legacy product as `XGO-MINI` / SKU `RB-Xgo-01` and specifies:

- processor: **K210 + STM32**;
- 240 x 240 LCD;
- OV2640 0.3 MP camera;
- 16 GB SD card;
- MEMS microphone;
- three programmable keys;
- 7.4 V 2500 mAh battery;
- micro-USB cable included;
- Blockly and Python programming via app/PC;
- open underlying serial protocol for secondary development.

The product page links a period K210 manual/datasheet hosted on RobotShop CDN.

## 2. RobotShop-hosted period K210 manual — strong period documentation

URL:

- https://cdn.robotshop.com/media/x/xgo/rb-xgo-05/pdf/xgo-mini_k210_4-1-.pdf

Relevant documented behavior:

- boot application menu on the K210 LCD;
- menu includes `DOG`, `Dog show`, face/gesture/mask demos and similar examples;
- firmware date/version is shown on screen;
- documentation refers to an `XGO Edu` PC application for Blockly-style programming;
- the K210 application depends on SD-card content.

## 3. Historical XGO AI demo repository — recovery candidate, not verified official vendor source

Parent repository:

- https://github.com/geluu/XgoAI

Useful fork discovered during recovery research:

- https://github.com/mynameiskristopher/k210-XgoAI

The repository description is `XGO AI demo code`. The English branch contains a package whose file names and structure closely match the 2021 K210 product generation:

- `xgo-ai-module-firmware-210722-en-2021-07-22-14-48-10.kfpkg`
- `sd/main.py`
- `sd/xgo.py`
- `sd/device_test.py`
- `sd/try_demo.py`
- `sd/language/`
- `sd/preset/`
- `sd/user/`
- Blockly XML examples.

Important source observation from historical `sd/xgo.py`:

- it is written for MaixPy/MicroPython (`machine.UART`);
- the internal XGO motion UART is opened at **115200 8N1**;
- it implements the original XGO motion protocol and commands such as movement, attitude, leg/motor control and actions.

Important source observation from historical `sd/main.py`:

- the board runs a custom menu application rather than a plain interactive REPL;
- it executes uploaded `user_latest_code.py` and demo files from SD;
- therefore failure of Ctrl-C to expose a `>>>` prompt on COM3 does **not** prove that the K210 serial path is dead.

### Trust limitation

`geluu/XgoAI` is not currently verified as an official Luwu/XGO vendor repository. Treat its firmware and SD tree as a **historical recovery candidate**, not as an automatically trusted image. Do not mirror or flash it blindly until the board identity and recovery process are checked.

## 4. K210 flashing tool — established upstream tool

Sipeed K210 flashing utility:

- https://github.com/sipeed/kflash_gui

It supports `.kfpkg` and `.bin` firmware files and Windows serial ports. If K210 reflashing is selected, use an established K210 flashing path rather than an ad-hoc writer.

## 5. Current XGO resources — useful but hardware-generation warning applies

Current XGO wiki/resource center:

- https://wiki.xgorobot.com/

Current resources include XGO Python libraries, firmware packages, schematics and mechanical files. However, current XGO-Mini lower-board material may target ESP32-based hardware.

**Do not flash current ESP32 M-series lower-board firmware onto this original STM32 generation.**

## Recovery order

Preferred order before writing flash:

1. Photograph powered LCD/menu and board markings.
2. Capture serial output during K210 boot.
3. Remove/read the microSD card and make a byte-for-byte or full-file backup if practical.
4. Compare installed SD files with the historical XGO AI demo tree.
5. If the K210 firmware is broken or inconvenient, restore a known K210 baseline only after confirming board/flash compatibility.
6. Treat the STM32 motion controller separately; do not overwrite it unless an original-generation image is positively identified.

This recovery sequence preserves an easy rollback while still allowing complete modernization afterward.
