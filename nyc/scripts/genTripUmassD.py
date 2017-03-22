#!/usr/bin/env python

import random

#source_list = ['--12805','-12790','-12811','-12808','-12797','--12816','-12798','-12804','-12782','--12786#0']

#dest_list = ['-12826']

source_list = ['zone'+str(i) for i in range(21)]

fl = '<?xml version="1.0"?>\n<trips>'


def gen_trips():
    tot_cars = 100000
    curr_car = 0
    st = ""
    while curr_car < tot_cars:
        zone = random.choice(source_list)
        st += '<trip id="%d" depart="%.2f" fromTaz="%s" toTaz="%s"/>\n' % (curr_car, curr_car*1.0,zone,zone)
        curr_car += 1
    return st
	
def gen_trips_new():
    tot_cars = 4000
    curr_car = 0
    st = ""
    while curr_car < tot_cars:
        st += '<trip id="%d" depart="%.2f" fromTaz="%s" toTaz="%s"/>\n' % (curr_car, curr_car*1.0,'source','source')
        curr_car += 1
    return st

fl += gen_trips()
fl += '</trips>'

f = open('../trips/trip.xml','w')
f.write(fl)
