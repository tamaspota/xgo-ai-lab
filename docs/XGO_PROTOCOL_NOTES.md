# XGO protocol notes

Updated: 2026-09-03

These notes separate two different interfaces present in the original Kickstarter-era XGO-Mini:

1. K210 AI-module USB/programming path;
2. STM32 motion-controller TTL protocol path.

Conflating these interfaces can make a correct XGO motion-protocol request appear to fail.

## Original 2021 motion-controller interface

The XGO-Mini Communication Protocol V1.0 dated 2021-08-05 documents:

- physical link: standard TTL serial;
- connector: XH2.54 4-pin;
- baud: `115200`;
- data bits: 8;
- stop bits: 1;
- parity: none.

The protocol also states that the core board has two serial interfaces. The 3.3 V terminal is occupied by the AI module by default. For direct communication from another controller, the AI-module terminal must be unplugged first.

This matters because the Windows-visible CP2102 on COM3 is not yet proven to bridge directly to the STM32 core board.

## Frame format

The original protocol and current upstream library use the same general framing family:

```text
55 00 LEN TYPE ADDR [DATA...] CHECKSUM 00 AA
```

Current upstream read helper:

- `TYPE = 0x02`;
- firmware address = `0x07`;
- read length = 10 bytes;
- checksum = `255 - ((LEN + TYPE + ADDR + READ_LEN) % 256)`.

Firmware query used in the repository:

```text
55 00 09 02 07 0A E3 00 AA
```

## COM3 test result

`python scripts\xgo_read_firmware_raw.py COM3` sent the firmware query above at 115200 baud and received no bytes.

Interpretation changed after reviewing the period hardware/protocol documentation:

- the original robot is K210 + STM32;
- direct STM32 control is documented on an internal/core-board TTL connector;
- the AI module normally occupies that TTL connection;
- therefore a no-response result on the K210-side USB CP2102 does **not** imply failed STM32 firmware.

## K210 identification path

`scripts/k210_serial_probe.py` is the next probe.

Passive mode:

```powershell
python scripts\k210_serial_probe.py COM3 --listen 5
```

Optional MicroPython/MaixPy REPL probe:

```powershell
python scripts\k210_serial_probe.py COM3 --listen 2 --repl
```

The REPL probe sends Ctrl-C/newline ASCII rather than an XGO motion frame. If a `>>>` prompt is detected, it sends a Python identity print command. It does not flash firmware.

## Current-library constructor hazard

Do not use current `XGO_DOG` merely to identify the hardware. The inspected constructor:

1. opens serial;
2. reads firmware;
3. selects parameter limits;
4. calls `reset()`;
5. reads yaw.

`reset()` executes action 255, so initialization is not a passive probe.

## Firmware warning

Current XGO-Mini driver-board documentation and firmware packages target ESP32-based generations. The original 2021 XGO-Mini is documented as K210 + STM32.

Do not flash current ESP32 `M` firmware to the original STM32 motion board. Firmware replacement is allowed only after the target board and matching image/tool are verified.
