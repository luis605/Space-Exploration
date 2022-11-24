'''
Copyright © 2022 <Luís Almeida>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

from ursina import *

from math import pi


# Units
Km=1000.0
m=Km/1000
AU=149597870700

StarRadius = 695508*Km

spaceGravity = 0
planetGravity = 9.1

pi = pi



# Convert Time
def hourToMinutes(hour):
    minutes = 60*hour
    return minutes

def hourToSeconds(hour):
    seconds = 3600*hour
    return seconds


def secondsToMinutes(seconds):
    minutes = seconds/60
    return minutes

def secondsToHours(seconds):
    hours = seconds/3600
    return hours


def minutesToSeconds(minutes):
    seconds = minutes*60
    return seconds

def minutesToHours(minutes):
    hours = minutes/60
    return hours

