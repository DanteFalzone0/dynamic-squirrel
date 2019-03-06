# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (C) 2019 Dante Falzone

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

# This is a program for economic planning.
import datetime

print("Stalinator Economic Planning Tool v.1 - Coded in Python by Dante Falzone")
print("Input the resource to be calculated and press ENTER.")
resource_name = input()
print("Input the units of measurement for that resource and press ENTER. (e.g. kg, L, etc.)")
units = input()
print("Input the projected demand for that resource as a number and press ENTER.")
demand = input(units + " ")
print("Input the current supply for that resource as a number and press ENTER.")
supply = input(units + " ")
print("Input the estimated cost per unit to produce that resource and press ENTER.")
cost = input("$ ")
print("Generating economic planning report...")
demand0 = float(demand)
supply0 = float(supply)
cost0 = float(cost)
price = ((cost0*demand0)/supply0)
sh = (supply0-demand0)
if sh > 0:
    plan = "surplus"
if sh == 0:
    plan = ("low supply, but no shortage")
if sh < 0:
    plan = ("shortage - recommend increasing supply by " + str(abs(sh)) + " " + units)
print("Finished.")
print("-" * 88)
print("☭ Economic Planning Report ☭")
print("-" * 88)
print(">> Product: " + resource_name)
print(">> Production volume: " + str(supply0) + " " + units)
print(">> Projected demand: " + str(demand0) + " " + units)
print(">> Ideal price: $ " + str(round(price, 2)) + "/" + units)
print(">> Resource scarcity status: " + plan)
print(" ")
print("Generated " + str(datetime.datetime.now()))
print("-" * 88)
