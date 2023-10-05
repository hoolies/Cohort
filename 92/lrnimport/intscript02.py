#!/usr/bin/env python3
import subprocess  ## <-------- changed
subprocess.call(["ip", "link", "show", "up"])
print("This program will check your interfaces.")
interface = input("Enter an interface, like, ens3: ")
subprocess.call(["ip", "addr", "show", "dev", interface])  ## <--- changed
subprocess.call(["ip", "route", "show", "dev", interface]) ## <--- changed

choice = input("Would you like to run Wireshark on the interface?")

if choise.startswith("y"):
    subprocess.call(["tshark", "-i", f"{interface}"]

