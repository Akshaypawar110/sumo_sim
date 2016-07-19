#!/usr/bin/env python

import random

source_list = ['--12805','-12790','-12811','-12808','-12797','--12786#2','--12816','-12798','--12782','-12801#1']

dest_list = ['-12826']

fl = '<?xml version="1.0"?>\n<trips>'


def gen_trips():
    tot_cars = 2000
    curr_car = 0
    st = ""
    while curr_car < tot_cars:
        st += '<trip id="%d" depart="%.2f" from="%s" to="%s"/>\n' % (curr_car, curr_car*2.0,random.choice(source_list),random.choice(dest_list))
        curr_car += 1
    return st

fl += gen_trips()
fl += '</trips>'

f = open('./trips/trip.xml','w')
f.write(fl)
