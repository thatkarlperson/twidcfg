#!/usr/bin/env python3
#
# Preliminary Twiddler.cfg Version 4 binary file parser

from construct import *
# from chorddata import ChordAdapter


class PrintContext(Construct):
    def _parse(self, s, ctx):
        print(ctx)

# Header (16 bytes)
header = Struct("header",
                Const(UBInt8("version"), 4),
                ULInt16("chordoffset"),
                ULInt16("mouseoffset"),
                ULInt16("stringoffset"),
                ULInt16("mousemodetime"),
                ULInt16("mousejumptime"),
                UBInt8("mousespeed"),
                UBInt8("mousejumpspeed"),
                UBInt8("mouseaccel"),
                UBInt8("repeatdelay"),
                UBInt8("options"))

# A single chord in the chord map
chord = Struct("chordmap",
               ULInt16("chord"),
               UBInt8("hidmod"),
               UBInt8("hidkey"))

# A single mouse-chord in the mouse map
mouse = Struct("mousemap",
               ULInt16("chord"),
               UBInt8("action"))

# A single string sequence in the string map
string = Struct("stringmap",
                ULInt16("length"),
                Array(lambda ctx: ctx.length / 2 - 1,
                      Struct("key",
                             UBInt8("hidmod"),
                             UBInt8("hidkey"))),
                      )

# Each map is delimited by an all-zeros object
# We just use the chord id or sequence length, since a zero here is enough
chords = RepeatUntil(lambda obj, ctx: obj.chord == 0, chord)
mouses = RepeatUntil(lambda obj, ctx: obj.chord == 0, mouse)
strings = RepeatUntil(lambda obj, ctx: obj.length == 0, string)

# The full file format
filemap = Struct("filemap",
    header,
    Pointer(lambda ctx: ctx.header.chordoffset, chords),
    Pointer(lambda ctx: ctx.header.mouseoffset, mouses),
    Pointer(lambda ctx: ctx.header.stringoffset, strings))


