#!/usr/bin/python
import os
import time
from controller import Server

username = os.environ.get("IDRAC_USERNAME")
password = os.environ.get("IDRAC_PASSWORD")

MIN_TEMP = 20
MAX_TEMP = 32

with open("./hosts.txt", 'r') as file:
  for line in file:
    host = line.strip()
    s = Server(host=host, username=username, password=password)

    temp = s.get_temp()
    print(f'Current temp: {temp}')

    if temp >= MAX_TEMP:
      s.set_fan_speed_auto()
    else:
      s.set_fan_speed_manual(fan_speed_pct=20)
