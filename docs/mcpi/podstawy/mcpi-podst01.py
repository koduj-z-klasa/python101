#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import mcpi.minecraft as minecraft  # import modułu minecraft
import mcpi.block as block  # import modułu block

os.environ["USERNAME"] = "Steve"  # nazwa użytkownika
os.environ["COMPUTERNAME"] = "mykomp"  # nazwa komputera

# utworzenie połączenia z minecraftem
mc = minecraft.Minecraft.create("192.168.1.10")  # podaj adres IP Rpi


def main(args):
    mc.postToChat("Czesc! Tak dziala MC chat!")  # wysłanie komunikatu do mc
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
