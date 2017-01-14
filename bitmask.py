#!/bin/env python3
'''Class that represents a bit mask.
It has methods representing all
the bitwise operations plus some
additional features. The methods
return a new BitMask object or
a boolean result. See the bits
module for more on the operations
provided.
'''

classs BitMask(int):
    def AND(self,bm):
        return BitMask(self & bm)
    def OR(self,bm):
        return BitMask(self | bm)
    def XOR(self,bm):
        return BitMask
