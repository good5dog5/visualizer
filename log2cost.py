#!/usr/bin/python

log = open('log', 'r')
cost = open('cost', 'w')
lines = log.readlines()

for line in lines :
	line = line.strip()
	inst, args = line.split(' ', 1)

	if inst == 'switch' :
		out_task, in_task, tick, tick_reload, out_minitick, in_minitick = args.split(' ')
		
		out_time = (float(tick) + (float(tick_reload) - float(out_minitick)) / float(tick_reload)) / 100 * 1000;
		in_time  = (float(tick) + (float(tick_reload) - float(in_minitick))  / float(tick_reload)) / 100 * 1000;
                switch_time = in_time - out_time;
                cost.write('switch from %s to %s cost %f\n' % (out_task, in_task, switch_time));
