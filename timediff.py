from datetime import datetime


def time_diff():
	print 'Type the times in 24-hour format as so: HH:MM'
	time1 = raw_input("Initial Time: ")
	time2 = raw_input("Final Time: ")
	FMT = '%H:%M'

	timediff = datetime.strptime(time2, FMT) - datetime.strptime(time1, FMT)
	print timediff

time_diff()	
