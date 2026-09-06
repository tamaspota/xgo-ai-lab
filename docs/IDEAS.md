# IDEAS

Updated: 2026-09-06

Purpose: keep useful brainstorms and upgrade directions without silently turning them into commitments or active work.

Rules:

- An entry here is an **idea**, not a decision or current task.
- Promote an idea to `docs/DECISIONS.md` or `docs/CURRENT_STATE.md` only after it is explicitly chosen or implementation starts.
- Prefer reusing the existing XGO-Mini chassis, original 12 servos, legacy robot arm, PC, Local GPU Helper and available cameras/controllers before buying another robotics platform.

## Modern upper compute / HMI on the ESP32 retrofit

Idea: after the vendor ESP32 motion-controller retrofit is installed and validated, replace or bypass the old K210 upper module with a simple modern compute/HMI stack.

Possible components:

- **existing Raspberry Pi 4B first**, because it is already available and is more than sufficient for UART control, Wi-Fi, camera, sensors, web UI and offload;
- Pi 5 / CM5 only if a real local-compute bottleneck later appears;
- inexpensive SPI/DSI/HDMI display rather than an expensive proprietary HMI;
- modern CSI or USB camera;
- microphone + speaker;
- Wi-Fi connection to PC / Local GPU Helper for heavier AI workloads;
- simple web UI / phone UI for debugging and child-friendly control.

Key architecture principle: keep motion on the vendor ESP32 board and communicate through the confirmed 3.3 V TTL UART / xgolib-compatible command layer.

## Display may be optional

Idea: do not assume the robot needs a large onboard display.

If normal interaction happens from a phone/web UI or through voice/AI, the onboard display can be minimal or omitted. A small display may be useful only for:

- status / battery / Wi-Fi;
- simple face / eye animations;
- mode indication;
- errors / IP address;
- occasional local camera preview.

This can reduce cost, power draw and mechanical complexity.

## ESP32-S3 compact upper controller

Idea: if Raspberry Pi is unnecessary for the final compact build, use an ESP32-S3 upper HMI inspired by Luwu's current open-source RIG-Omni architecture.

Potential functions:

- Wi-Fi / BLE;
- small LCD;
- camera;
- microphone / speaker;
- local buttons;
- web control;
- UART bridge to the XGO motion board;
- remote AI calls to the PC / Local GPU rather than running heavy models onboard.

This is a later optimization, not part of the first bring-up.

## Do not copy a full Lite3 / mini2 system unnecessarily

Idea rule: current XGO Lite3 / mini2-class robots are useful references for architecture and UI, but there is no requirement to reproduce their complete hardware stack.

The current chassis, 12 servos and new ESP32 motion board already provide the expensive mechanical/motion foundation. Display, camera and AI compute can be implemented with inexpensive generic parts if that is simpler and cheaper.

## Use newer XGO families as architecture references

Idea: treat Lite3, Mini2S, Mini2SW, Rider2 and Ranger as sources of useful engineering patterns rather than as mandatory donor hardware.

Possible things to borrow conceptually:

- current UART layering between motion board and upper compute;
- current XGO firmware / xgolib conventions;
- camera/display placement;
- sensor ideas;
- wheel-leg control concepts;
- arm/gripper control API patterns;
- power-distribution ideas;
- service/flash/test workflows.

Exact board family and connector compatibility must be verified on the purchased retrofit board before adapting any current-generation hardware.

See `docs/XGO_BOARD_FAMILY_2026.md`.

## Optional newer XGO-style display/head appearance

Idea: if the vendor later offers an inexpensive spare display/camera/head module that is electrically compatible with the replacement ESP32 board, consider it as a convenience option.

Do not buy a complete newer robot merely to obtain the display/camera module.

## Future custom arm / gripper

Idea: after stable locomotion is restored, investigate a lightweight custom arm or gripper.

Constraints:

- vendor confirmed current Lite3/mini2 arm modules are not direct plug-and-play on the old chassis;
- do not assume current arm wiring/firmware compatibility;
- mechanical bracket/connector changes are acceptable if a future arm is worth implementing;
- the current `xgolib` API includes arm/gripper concepts and servo IDs, which may provide a useful software reference even if the physical arm is custom;
- alternatively keep using the separate university-era robot arm as an independent manipulator station.

Possible experiment:

- XGO transports an object;
- fixed arm picks/places it;
- later AI planning coordinates both.

## Battery / power experimentation after baseline success

Idea: first prove the retrofit with a matched pair of existing 18650 cells. If the robot runs only briefly, that is enough to validate the board/chassis/servo combination.

Only after the new board's actual voltage range, current demand and connector arrangement are known, consider:

- a matched high-current 18650 pair;
- higher-capacity 2S pack;
- a suitable 2S LiPo conversion;
- separate regulated supply for upper compute if needed.

Do not design power modifications before measuring the incoming board.

## Archive the original 2021 electronics

Idea: do not throw away or physically destroy the original K210 + STM32 V2.5 electronics even if the ESP32 retrofit works.

Keep them as:

- historical reference from the original Kickstarter generation;
- possible later reverse-engineering/debugging exercise;
- teaching/demo material showing the 2021 vs 2026 controller architecture;
- source of reusable connectors, dimensions and mechanical references if useful.

No active repair effort is planned unless there is a specific educational/research reason later.

## Education / research platform

Idea: use the revived XGO as an engineering teaching and PhD/research platform rather than as a restored demo toy.

Possible educational topics:

- embedded UART protocol integration;
- ESP32 motion controller + SBC layered architecture;
- robotics middleware and Python control;
- computer vision;
- voice/AI control;
- local GPU offload;
- fault diagnosis / retrofit engineering;
- safe human/child interaction;
- multi-robot coordination.

## Child-friendly robot mode

Possible features:

- bounded joystick movement;
- named tricks/actions;
- voice commands;
- camera view;
- simple programmable sequences or Blockly/Scratch-like commands;
- explicit stop and speed limits.

## Upgrade decision rule

Before buying major hardware, identify the actual limitation:

- motion-controller limitation -> use vendor ESP32 retrofit first;
- compute limitation -> move compute to existing Pi 4B / PC / Local GPU before buying Pi 5 or CM5;
- vision limitation -> replace/add camera;
- interaction limitation -> add display/microphone/speaker/UI;
- manipulation limitation -> evaluate custom gripper or existing robot arm;
- mechanical locomotion limitation -> only then evaluate a newer robot chassis.

This is an engineering heuristic, not a prohibition on future purchases.
