#!/bin/python3

from datetime import datetime

name = input("Enter your name: ")

dt = datetime.now()
daynumber = dt.weekday()
week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

print(f"Hello, {name}! Happy {week[daynumber]}!")

