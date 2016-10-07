#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from time import sleep
import mcpi.minecraft as minecraft  # import modułu minecraft
import mcpi.block as block  # import modułu block

os.environ["USERNAME"] = "Steve"  # nazwa użytkownika
os.environ["COMPUTERNAME"] = "mykomp"  # nazwa komputera

# utworzenie połączenia z minecraftem
mc = minecraft.Minecraft.create("192.168.1.10")  # podaj adres IP Rpi


def jakiBlok():
    while True:
        x, y, z = mc.player.getPos()
        blok_pod = mc.getBlock(x, y - 1, z)
        print(blok_pod)
        sleep(1)


def slad(blok=38):
    while True:
        x, y, z = mc.player.getPos()
        mc.setBlock(x, y, z, blok)
        sleep(0.1)


def slad_jezeli(pod=2, blok=38):
    while True:
        x, y, z = mc.player.getPos()
        blok_pod = mc.getBlock(x, y - 1, z)  # blok pod graczem

        if blok_pod == pod:
            mc.setBlock(x, y, z, blok)
        sleep(0.1)


def main(args):
    mc.postToChat("Czesc! Tak dziala MC chat!")  # wysłanie komunikatu do mc
    jakiBlok()
    # slad(7)
    # slad_jezeli(1)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
