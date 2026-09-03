"""Passive serial-port discovery for XGO bring-up.

This script intentionally does not open any serial port and sends no bytes.
Run it once before connecting the XGO and once after connecting it.
"""

from serial.tools import list_ports


def main() -> None:
    ports = sorted(list_ports.comports(), key=lambda item: item.device)

    if not ports:
        print("No serial ports detected.")
        return

    print(f"Detected {len(ports)} serial port(s):")
    for port in ports:
        print("-")
        print(f"  device:       {port.device}")
        print(f"  description:  {port.description}")
        print(f"  manufacturer: {port.manufacturer or '-'}")
        print(f"  hwid:         {port.hwid}")
        print(f"  vid:pid:      {port.vid!s}:{port.pid!s}")
        print(f"  serial:       {port.serial_number or '-'}")
        print(f"  location:     {port.location or '-'}")


if __name__ == "__main__":
    main()
