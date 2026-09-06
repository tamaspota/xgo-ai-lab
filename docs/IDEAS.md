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

- Raspberry Pi Zero 2 W, CM4/CM5 or other SBC depending on actual workload;
- inexpensive SPI/DSI/HDMI display rather than an expensive proprietary HMI;
- modern CSI or USB camera;
- microphone + speaker;
- Wi-Fi connection to PC / Local GPU Helper for heavier AI workloads;
- simple web UI for debugging and child-friendly control.

Key architecture principle: keep motion on the vendor ESP32 board and communicate through the confirmed 3.3 V TTL UART / xgolib-compatible command layer.

## Do not copy a full Lite3 / mini2 system unnecessarily

Idea rule: current XGO Lite3 / mini2-class robots are useful references for architecture and UI, but there is no requirement to reproduce their complete hardware stack.

The current chassis, 12 servos and new ESP32 motion board already provide the expensive mechanical/motion foundation. Display, camera and AI compute can be implemented with inexpensive generic parts if that is simpler and cheaper.

## Optional newer XGO-style display/head appearance

Idea: if the vendor later offers an inexpensive spare display/camera/head module that is electrically compatible with the replacement ESP32 board, consider it as a convenience option.

Do not buy a complete newer robot merely to obtain the display/camera module.

## Future custom arm / gripper

Idea: after stable locomotion is restored, investigate a lightweight custom arm or gripper.

Constraints:

- vendor confirmed current Lite3/mini2 arm modules are not direct plug-and-play on the old chassis;
- do not assume current arm wiring/firmware compatibility;
- mechanical bracket/connector changes are acceptable if a future arm is worth implementing;
- alternatively keep using the separate university-era robot arm as an independent manipulator station.

Possible experiment:

- XGO transports an object;
- fixed arm picks/places it;
- later AI planning coordinates both.

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
- compute limitation -> move compute to SBC/PC/Local GPU;
- vision limitation -> replace/add camera;
- interaction limitation -> add display/microphone/speaker/UI;
- manipulation limitation -> evaluate custom gripper or existing robot arm;
- mechanical locomotion limitation -> only then evaluate a newer robot chassis.

This is an engineering heuristic, not a prohibition on future purchases.
