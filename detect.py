from datetime import datetime, timedelta
import re

logfile = 'csacsExample'
time = 5

f = open(logfile, 'r')

#Getting the first date to compare

first_date = f.readline().split()
read_file = f.read().split("\n")
ip_addr = dict()
format = '%b %d %H:%M:%S'
date = first_date[0] + " " + first_date[1] + " " + first_date[2]
date = datetime.strptime(date, format)

#Reading through the log file

for line in filter(None,read_file):
    get_date = line.split()
    match = re.search(('Remote-Address=(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'), line)
    if match:
            if match.group(1) in ip_addr:
                ip_addr[match.group(1)] += 1
            else:
                ip_addr[match.group(1)] = 1

    #Extracting date from each line in the log file
    date_compare = get_date[0] + " " + get_date[1] + " " + get_date[2]
    date_compare = datetime.strptime(date_compare,format)
    diff = date_compare - date

    if (diff > timedelta(minutes=time)):

        date = date_compare

for key in ip_addr:

    print "Key: ", key, "ip_addr: ", ip_addr[key]
