#!/usr/bin/python

from datetime import datetime


def getTime():
    n = datetime.now()
    t = n.timetuple()
    y, m, d, h, min, sec, wd, yd, i = t

    return [h, min, sec]


def toSeconds():
    station_hour = getTime()
    return station_hour[2] + (station_hour[1] * 60) + (station_hour[0] * 3600)


def toTime(seconds):
    h = seconds / 3600
    min = (seconds % 3600) / 60
    sec = (seconds % 3600) % 60
    return [h, min, sec]
