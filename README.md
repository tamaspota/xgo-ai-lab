# xgo-ai-lab

Safe bring-up and modernization workspace for an original Kickstarter-era XGO-Mini.

The immediate goal is **not** to rebuild the robot or flash firmware. First we identify the exact hardware/firmware and establish a reproducible PC control path. Later phases may add voice/vision AI, Local GPU Helper integration, and a separate legacy robot arm.

## Current status

- Original XGO-Mini hardware exists and will be connected to a Windows PC.
- Exact controller revision, firmware version, serial interface and battery state are **not yet verified**.
- No firmware update is approved.
- No motion command is approved during the first diagnostic pass.

## Important safety note

The current official `LuwuDynamics/xgo_doglib` supports XGO-Mini and uses 115200 baud by default, but its current `XGO_DOG` constructor calls `reset()` during initialization. That can command robot motion. Therefore the first bring-up step in this repository deliberately does **not** instantiate `xgolib`.

Reference reviewed 2026-09-03:
- https://github.com/LuwuDynamics/xgo_doglib
- reviewed source commit: `cf72514273dc703284d3c47e46c67ce238caae11`

## First run: passive serial discovery

Windows PowerShell:

```powershell
git clone https://github.com/tamaspota/xgo-ai-lab.git
cd xgo-ai-lab
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python scripts/list_serial_ports.py
```

Run the script once **without** the XGO connected and once **after** connecting it. Compare the outputs and record the newly appearing COM port/device in `docs/HARDWARE.md` or the current session log.

The script only enumerates serial ports. It does not open a port and cannot intentionally move the robot.

## Planned phases

1. **Passive discovery** — identify USB/serial device and COM port.
2. **Safe protocol probe** — read identity/firmware without sending motion/reset commands.
3. **Minimal motion test** — only after protocol and stop behavior are understood.
4. **Control layer** — stable Python API for XGO commands with explicit safety limits.
5. **AI integration** — voice/vision/task layer using PC or Local GPU Helper as the compute node.
6. **Robot-arm integration** — keep the legacy arm as a separate manipulator station initially.

## Repository memory

AI tools working on this repository must read these first:

- `AGENTS.md`
- `docs/CURRENT_STATE.md`
- `docs/DECISIONS.md`
- latest file under `logs/`

Implementation state belongs in this repository rather than in chat history.
