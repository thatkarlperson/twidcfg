#!/usr/bin/env python3

from construct import *


class ChordAdapter(Adapter):
    '''Encoded chords are containers with chord, hidmod, hidkey.
    Decoded are containers with mod letters, key character, and spelled-out
    chord (e.g. OLOO).
    '''

    def _encode(self, obj, ctx):
        pass

    def _decode(self, obj, ctx):
        pass




