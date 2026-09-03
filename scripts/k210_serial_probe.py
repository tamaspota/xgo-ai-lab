"""Probe the original XGO-Mini K210 USB-UART interface without flashing firmware.

Default mode is passive: open the serial port and print any bytes received.
Optional --repl mode sends MicroPython-style Ctrl-C / newline characters and, only
if a >>> prompt is detected, asks Python to print sys.implementation. These bytes
are not valid XGO motion-protocol frames, so a motion controller expecting 0x55 0x00
framing should ignore them.
"""

from __future__ import annotations

import argparse
import sys
import time

import serial


def read_available(ser: serial.Serial, duration: float) -> bytes:
    deadline = time.time() + duration
    data = bytearray()
    while time.time() < deadline:
        waiting = ser.in_waiting
        if waiting:
            data.extend(ser.read(waiting))
        else:
            time.sleep(0.02)
    return bytes(data)


def show(label: str, data: bytes) -> None:
    print(f"{label} bytes: {len(data)}")
    if not data:
        print("  <none>")
        return
    print("  hex:  " + data.hex(" "))
    text = data.decode("utf-8", errors="replace")
    print("  text:")
    for line in text.splitlines() or [text]:
        print("    " + line)


def main() -> int:
    parser = argparse.ArgumentParser(description="Original XGO-Mini K210 serial probe")
    parser.add_argument("port", help="Windows COM port, e.g. COM3")
    parser.add_argument("--baud", type=int, default=115200)
    parser.add_argument("--listen", type=float, default=3.0, help="passive listen seconds")
    parser.add_argument(
        "--repl",
        action="store_true",
        help="attempt to interrupt a K210/MaixPy program and detect a MicroPython REPL",
    )
    args = parser.parse_args()

    print("XGO original K210 serial probe")
    print(f"port: {args.port}")
    print(f"baud: {args.baud}")
    print("No firmware flashing and no XGO motion packet is sent.")

    try:
        with serial.Serial(args.port, args.baud, timeout=0.1) as ser:
            ser.reset_input_buffer()
            initial = read_available(ser, args.listen)
            show("passive RX", initial)

            if not args.repl:
                print("Passive probe complete. Use --repl only if K210 console probing is intended.")
                return 0

            print("Attempting K210/MicroPython REPL detection...")
            ser.write(b"\x03\x03\r\n")
            ser.flush()
            repl_rx = read_available(ser, 2.0)
            show("after Ctrl-C", repl_rx)

            if b">>>" not in repl_rx:
                print("No >>> prompt detected. No further command will be sent.")
                return 2

            ser.write(b'import sys; print("XGO_K210_REPL_OK", sys.implementation)\r\n')
            ser.flush()
            ident_rx = read_available(ser, 2.0)
            show("REPL identity", ident_rx)
            return 0

    except serial.SerialException as exc:
        print(f"Serial error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
