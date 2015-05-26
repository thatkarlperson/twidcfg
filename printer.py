#!/usr/bin/env python3

import parser

data = open("default.cfg", "rb")
s = parser.filemap.parse(data.read())

print(s)


