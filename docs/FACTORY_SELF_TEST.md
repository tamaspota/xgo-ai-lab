# Factory K210 self-test path

Updated: 2026-09-03

This procedure is derived from the historical `geluu/XgoAI` English-branch source for the original K210-based XGO-Mini. It is intended to verify the installed K210 application, camera, microphone, SD card, speaker and buttons **without reflashing firmware**.

## Why this is relevant

Tamás reports that the powered robot displays firmware text approximately matching `xgo-210722` / `210722`. A historical recovery package exists with the filename:

`xgo-ai-module-firmware-210722-en-2021-07-22-14-48-10.kfpkg`

This is a strong version/date match, but it is still treated as supporting evidence rather than cryptographic proof that the installed image is identical.

The same historical source tree contains `sd/main.py` and `sd/device_test.py`.

## Entering test mode

Historical `sd/main.py` maps the three physical buttons as:

- left / A button: GPIO 9
- right / B button: GPIO 10
- down / C button: GPIO 11

At startup, if the **left/A button is held** and the right/B button is not held, `main.py` enters test mode and executes:

`/sd/device_test.py`

Practical procedure:

1. Disconnect the USB serial terminal/program that may hold COM3 open.
2. Power the robot off.
3. Hold the **left/A** button.
4. Power the robot on while continuing to hold left/A for the initial boot period.
5. Observe the LCD.
6. Release the button after the test screen appears.

If no test screen appears, repeat once while ensuring only the left/A button is held.

## What the historical factory test checks

`sd/device_test.py` performs, in order:

1. LCD RGB test
2. camera test
3. microphone / FFT test
4. SD-card test
5. speaker playback test
6. A/B/C button test
7. LED test

The SD test executes `os.listdir("/sd")` and considers the SD stage successful only if `try_demo.py` is present.

Therefore **we do not need to physically locate/remove the SD card first**. The built-in self-test can establish whether the K210 currently mounts `/sd` and sees the expected application file.

## Evidence to capture

Photograph or transcribe:

- displayed firmware/version string;
- each `OK`, `Failed`, or `Error` line;
- any Python exception text;
- whether live camera image appears;
- whether microphone visualization reacts;
- whether boot sound / speaker test works;
- whether A/B/C button prompts can be completed.

## Interpretation

### If all tests pass

Do **not** flash the K210. The original K210 stack, camera, microphone, SD and UI are working. Move directly to establishing a supported way to upload/run a small user program and then test K210 -> STM32 movement using the historical `xgo.py` API.

### If SD fails but other K210 peripherals pass

Prefer SD recovery first. Compare/rebuild the SD contents from the historical XgoAI tree before touching K210 flash.

### If K210 peripherals fail broadly or the application will not boot

Only then evaluate reflashing the matching 2021 K210 `.kfpkg`, after confirming the K210 flash/recovery tool path.

## Source evidence

Historical source reviewed:

- `geluu/XgoAI`, branch `en`
- `sd/main.py`
- `sd/device_test.py`
- `sd/try_demo.py`
- `sd/xgo.py`
- `xgo-ai-module-firmware-210722-en-2021-07-22-14-48-10.kfpkg`

This repository is a strong period source but has not been established as an official current vendor repository.
