from datetime import datetime, timedelta
import re
import sys

if (len(sys.argv) < 2):
    print 'Usage: detect.py [logfile]'
    exit()

LOGFILE = str(sys.argv[1])
MAX_TIME = 5
MAX_ATTEMPT = 6

f = open(LOGFILE, 'r')

#Getting the first date to compare

first_date = f.readline().split()
read_file = f.read().split("\n")
ip_address = dict()
ban_ip = []
format = '%b %d %H:%M:%S'
date = first_date[0] + " " + first_date[1] + " " + first_date[2]
date = datetime.strptime(date, format)

#Reading through the log file
#read_line = read_line[1:1000]

for line in filter(None,read_file):

    get_date = line.split()
    match = re.search(('Remote-Address=(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'), line)
    if match:
            if match.group(1) in ip_address:
                ip_address[match.group(1)] += 1
            else:
                ip_address[match.group(1)] = 1

    #Extracting date from each line in the log file

    date_compare = get_date[0] + " " + get_date[1] + " " + get_date[2]
    date_compare = datetime.strptime(date_compare,format)
    diff = date_compare - date

    if (diff > timedelta(minutes=MAX_TIME)):
        date = str(date)
        date = date[5:len(date)]
        print 'Date:',date, '\n'
        for key in ip_address:
            if ip_address[key] >= MAX_ATTEMPT:
                print 'Attempted IP Addresses: \n'
                print key, '\n'
                ban_ip.append(key)
                ip_address[key] = 0

        date = date_compare

#print ban_ip
