import csv
import pprint
from functools import reduce

detroit_data = []
detroitloc = (r'data/911_last_30_days.csv')

    
def get_file():
    global detroit_dict
    global detroit_dict

    with open('911_last_30_days.csv', 'r') as csvfile:
        d_file = csv.DictReader(csvfile)
        for line in d_file:
            detroit_data.append(line)

#parti

def filter_file():
    global detroit_data

    # filteout rows with empty zip_code
    detroit_data = list(filter(lambda row: row[5] != None, detroit_data))
    # filter out rows with empty neighborhood
    detroit_data = list(filter(lambda row: row[20] != None, detroit_data))

def avg_times():
    global detroit_data
    # reduce calc avg. 
    # response_time
    response_time = []
    for line in detroit_data:
        if line[17] != '':
            response_time.append(int(line[17]))

    r_time = reduce(lambda time1, time2: time1 + time2, [response_time])
    avg_response = (r_time/len(response_time))

    # dispatch time
    dispatch_time = []
    for line in detroit_data:
        if line[15] != "":
            dispatch_time.append(int(line[15]))
    
    d_time = reduce(lambda time1, time2: time1 + time2, [dispatch_time])
    avg_dispatch = (d_time/len(dispatch_time))

    # totaltimer_file()
    total_time = []
    for line in detroit_data:
        if line[19] != "":
            total_time.append(int(line[19]))
    
    total_time = reduce(lambda time1, time2: time1 + time2, [total_time])
    avg_total = (t_time/len(total_time))

    print(avg_dispatch)
    print(avg_response)
    print(avg_total)

avg_times()

# part ii
