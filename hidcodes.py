#!/usr/bin/env python3
#
# Read a mapping of keyboard HID codes.
# Input format is one line per key, space-separated, with 

FILE = "usb_hid_codes"

# Each key symbol (e.g. '%' or 'ENTER') corresponds to a HID code and a
# shift bit (False for unshifted, True for shifted).

# KEYS :: key -> (code, bool)
KEYS = {}
# CODES :: code -> [key, ...]
CODES = {}

with open(FILE) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        (code, *keys) = line.split()
        code = int(code)
        CODES[code] = keys
        KEYS[keys[0]] = (code, False)
        if len(keys) == 2:
            KEYS[keys[1]] = (code, True)
        elif len(keys) != 1:
            raise ValueError("Bad line:", line)


def hidcode(key):
    """Return the USB HID key code and modifier byte for this key."""
    code, shift = KEYS[key]
    return (code, 0x20 if shift else 0x00)

