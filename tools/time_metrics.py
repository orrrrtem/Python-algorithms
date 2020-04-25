import math 

def get_median(time_list, sorted = True):
    if len(time_list) is 0:
        return NaN
    if not sorted:
        time_list.sort()
    if len(time_list) % 2 == 0:
        return (time_list[int(len(time_list)/2)] + time_list[int(1 + len(time_list)/2)]) / 2
    else:
        return time_list[int(len(time_list)/2)]


def get_min(time_list, sorted = True):
    if len(time_list) is 0:
        return NaN 
    if not sorted:
        time_list.sort()  
    return time_list[0]


def get_max(time_list, sorted = True):
    if len(time_list) is 0:
        return NaN 
    if not sorted:
        time_list.sort()  
    return time_list[-1]

def get_variance(time_list):
    if len(time_list) is 0:
        return NaN 
    mean = sum(time_list) / len(time_list) 
    variance = sum([((x - mean) ** 2) for x in time_list]) / len(time_list)
    return variance

def get_mean(time_list):
    if len(time_list) is 0:
        return NaN 
    mean = sum(time_list) / len(time_list) 
    return mean
