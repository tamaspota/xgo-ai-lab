# IDEAS

Updated: 2026-09-03

Purpose: keep useful brainstorms and upgrade directions without silently turning them into commitments or active work.

Rules:

- An entry here is an **idea**, not a decision or current task.
- Promote an idea to `docs/DECISIONS.md` or `docs/CURRENT_STATE.md` only after it is explicitly chosen or implementation starts.
- Prefer reusing the existing XGO-Mini, legacy robot arm, PC, Local GPU Helper and available cameras/controllers before buying another robotics platform.
- Record useful external references in the relevant source/reference document when they become implementation inputs.

## Existing XGO as a modernized robotics platform

Idea: keep the original XGO-Mini mechanics and motion controller, but modernize the high-level software and sensing around it instead of replacing the whole robot.

Possible directions:

- write a clean maintainable control layer for the existing robot;
- use the existing K210 only where it remains useful;
- move heavier AI/vision/speech work to a PC, Raspberry Pi-class gateway or Local GPU Helper;
- add or replace the camera later if the original OV2640 becomes the limiting component;
- add microphone / voice control using the broader AI-recorder work where useful;
- expose motion, camera and sensor functions through a simple API that other agents/applications can call.

Rationale: newer educational/AI quadrupeds can cost roughly four figures, while much of the useful value may come from software, sensors and compute that can be added around the existing hardware. Exact market-price comparison is not treated as a verified project fact here.

## Child-friendly robot mode

Idea: create a mode that is safe and simple enough for Tamás's child to use.

Possible features:

- simple web/desktop controller;
- bounded joystick movement;
- named tricks/actions;
- voice commands;
- camera view;
- simple programmable sequences or Blockly/Scratch-like commands;
- explicit stop and speed limits.

## Legacy robot arm integration

Idea: bring the university-era robot arm into this same repository as a second robot device.

Initial architecture:

- XGO remains the mobile platform;
- robot arm remains a separate fixed manipulator station;
- coordinate them in software rather than mechanically mounting the arm on the XGO initially.

Possible child/demo task:

- XGO transports a small object to the arm;
- arm picks/places the object;
- later AI planning coordinates both devices.

Needed before implementation:

- photos;
- controller board identification;
- actuator types;
- power supply;
- communication interface;
- any original university source code or documentation.

## Upgrade decision rule

Before buying a newer robot or major replacement hardware, first identify the actual limitation of the existing system:

- compute limitation -> move compute off-board;
- vision limitation -> replace/add camera;
- interaction limitation -> add microphone/speaker/UI;
- motion limitation -> only then evaluate newer mechanical platforms;
- manipulation limitation -> use/integrate the existing robot arm first.

This is an engineering heuristic, not a prohibition on future purchases.
