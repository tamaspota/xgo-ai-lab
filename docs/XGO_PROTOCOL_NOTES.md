# XGO protocol notes

Updated: 2026-09-03

These notes are based on inspection of the current public `LuwuDynamics/xgo_doglib` source at commit `cf72514273dc703284d3c47e46c67ce238caae11`. They are used only to establish a conservative bring-up path for an original Kickstarter-era XGO-Mini. Compatibility with the installed 2021-era firmware is not yet proven.

## Serial parameters

Current upstream defaults:

- baud: `115200`
- host interface: serial/UART
- current Python library uses `pyserial`

## Frame format observed in upstream source

General frame structure:

```text
55 00 LEN TYPE ADDR [DATA...] CHECKSUM 00 AA
```

For the upstream read helper:

- `TYPE = 0x02`
- request frame length = `0x09`
- byte after address is requested read length
- checksum is `255 - ((LEN + TYPE + ADDR + READ_LEN) % 256)`

## Firmware-version read

Upstream defines:

- `FIRMWARE_VERSION` address: `0x07`
- requested length: `10` bytes

Therefore the inspected upstream firmware query is:

```text
55 00 09 02 07 0A E3 00 AA
```

Checksum derivation:

```text
0x09 + 0x02 + 0x07 + 0x0A = 0x1C
0xFF - 0x1C = 0xE3
```

The upstream `read_firmware()` decodes the returned 10-byte payload as ASCII and strips trailing NUL bytes.

## Important constructor hazard

Do not instantiate the current `XGO_DOG` class during initial bring-up.

The inspected constructor:

1. opens the serial port;
2. reads firmware;
3. selects parameter limits;
4. calls `reset()`;
5. reads yaw.

`reset()` calls action `255`, so initialization is not passive.

## Local safe probe

`scripts/xgo_read_firmware_raw.py` implements only the firmware READ request above. It does not import `xgolib` and contains no motion, reset, calibration, upgrade, servo or action command.

Run only after the correct COM port is identified:

```powershell
python scripts\xgo_read_firmware_raw.py COM3
```

If there is no response, do not automatically try write/motion commands or firmware updates. Check robot/controller power, cabling and hardware revision first.
