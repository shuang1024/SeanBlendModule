#  ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

def add(addend1, addend2):
    return addend1 + addend2

def subtract(num1, num2):
    return num1 - num2

def multiply(factor1, factor2):
    return factor1 * factor2

def divide(dividend, divisor):
    return dividend / divisor

def exponent(num, exponent):
    return num ** exponent

def abs(num):
    if num < 0:
        return -num
    else:
        return num

def scientificNotation(num):
    revs = 0
    if num < 10:
        return num
    elif num == 10:
        return "1x10^1"
    elif num > 10:
        while num >= 10:
            num /= 10
            revs += 1
        return str(num) + "x10^" + str(revs)