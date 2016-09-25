# import sys
# sys.path.append("/root/mcpi-sim")  # uwaga: sprawdź ścieżkę!
import mcpi.minecraft as minecraft  # import modułu minecraft
import mcpi.block as block  # import modułu block
import os
os.environ["USERNAME"] = "Steve"  # wpisz dowolną nazwę użytkownika
os.environ["COMPUTERNAME"] = "mykomp"  # wpisz dowolną nazwę komputera
mc = minecraft.Minecraft.create("192.168.1.8")
