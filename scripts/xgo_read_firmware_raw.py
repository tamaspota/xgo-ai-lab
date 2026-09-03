#!/usr/bin/env python3
"""Minimal read-only firmware probe for XGO-Mini.

This script deliberately does NOT import or instantiate xgolib.  The current
upstream XGO_DOG constructor performs a reset/action during initialization.

The request implemented here is the firmware-version READ request inspected in
LuwuDynamics/xgo_doglib commit cf72514273dc703284d3c47e46c67ce238caae11:

    mode       = 0x02 (read)
    address    = 0x07 (FIRMWARE_VERSION)
    read_len   = 10 bytes
    baud       = 115200

No write-mode, action, gait, servo, reset, calibration or upgrade command is
implemented in this file.
"""

from __future__ import annotations

import argparse
import time
from typing import Optional

import serial


BAUD = 115200
READ_MODE = 0x02
FIRMWARE_ADDRESS = 0x07
FIRMWARE_READ_LEN = 10


def build_read_packet(address: int, read_len: int) -> bytes:
    """Build the XGO read request used by upstream __read()."""
    length = 0x09
    checksum = 255 - ((length + READ_MODE + address + read_len) % 256)
    return bytes(
        [
            0x55,
            0x00,
            length,
            READ_MODE,
            address,
            read_len,
            checksum,
            0x00,
            0xAA,
        ]
    )


def collect_response(ser: serial.Serial, timeout_s: float) -> bytes:
    deadline = time.monotonic() + timeout_s
    raw = bytearray()

    while time.monotonic() < deadline:
        waiting = ser.in_waiting
        if waiting:
            raw.extend(ser.read(waiting))
        else:
            time.sleep(0.02)

    return bytes(raw)


def find_first_packet(raw: bytes) -> Optional[bytes]:
    """Return the first complete 0x55 0x00 framed packet, if present.

    In the inspected upstream implementation the packet's length byte is also
    the total frame length.
    """
    for start in range(max(0, len(raw) - 1)):
        if raw[start : start + 2] != b"\x55\x00":
            continue
        if start + 3 > len(raw):
            return None

        frame_len = raw[start + 2]
        if frame_len < 8:
            continue

        end = start + frame_len
        if end <= len(raw):
            return raw[start:end]

    return None


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Send only the XGO firmware-version READ query and print the raw response."
    )
    parser.add_argument("port", help="Windows serial port, e.g. COM3")
    parser.add_argument(
        "--timeout",
        type=float,
        default=1.5,
        help="response collection time in seconds (default: 1.5)",
    )
    args = parser.parse_args()

    request = build_read_packet(FIRMWARE_ADDRESS, FIRMWARE_READ_LEN)

    print("XGO read-only firmware probe")
    print(f"port:          {args.port}")
    print(f"baud:          {BAUD}")
    print(f"request hex:   {request.hex(' ')}")
    print("request type:  READ firmware address 0x07, 10 bytes")
    print("No xgolib object will be created; no reset/action command is sent.")

    ser = serial.Serial()
    ser.port = args.port
    ser.baudrate = BAUD
    ser.timeout = 0.1
    ser.write_timeout = 1.0
    ser.xonxoff = False
    ser.rtscts = False
    ser.dsrdtr = False
    # Keep modem-control outputs inactive before opening the CP210x port.
    ser.dtr = False
    ser.rts = False

    try:
        ser.open()
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        time.sleep(0.10)

        ser.write(request)
        ser.flush()
        raw = collect_response(ser, args.timeout)
    except serial.SerialException as exc:
        print(f"Serial error: {exc}")
        return 2
    finally:
        if ser.is_open:
            ser.close()

    if not raw:
        print("response:      <none>")
        print("No reply was received. This does not prove a protocol failure; the robot/controller may need power or further interface inspection.")
        return 1

    print(f"response hex:  {raw.hex(' ')}")

    frame = find_first_packet(raw)
    if frame is None:
        print("frame:         no complete 0x55 0x00 packet found")
        return 1

    print(f"frame hex:     {frame.hex(' ')}")
    print(f"frame length:  {len(frame)}")

    # XGO frame: 55 00 LEN TYPE ADDR <payload...> CHECKSUM 00 AA
    if len(frame) >= 8:
        frame_type = frame[3]
        address = frame[4]
        payload = frame[5:-3]
        print(f"frame type:    0x{frame_type:02X}")
        print(f"address:       0x{address:02X}")
        print(f"payload hex:   {payload.hex(' ')}")
        try:
            text = payload.decode("ascii").rstrip("\x00")
        except UnicodeDecodeError:
            text = "<payload is not ASCII>"
        print(f"payload ASCII: {text}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
