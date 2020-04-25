import time
import pandas as pd

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir2 = os.path.dirname(parentdir)
sys.path.insert(0,parentdir)
sys.path.insert(0,parentdir2)
from time_metrics import *
from algorithms.string_searching.naive import naive
from algorithms.string_searching.robin_carp import robin_carp
from algorithms.string_searching.kmp import kmp
from algorithms.string_searching.bmh import bmh

def get_time_df(num_iterations = 10, methods = [naive], len_cases = 4 ):
    time_total = pd.DataFrame(columns=['file', 'method', 'mean', 'median', 'min', 'max', 'variance'])
    df_index = 0
    for i in range(0, len_cases):
        for method in methods:
            time_good = []
            time_bad = []
            for j in range(0, num_iterations):
                t0 = time.time()
                method(good_patterns[i], good_texts[i])
                t1 = time.time()
                total = t1-t0
                time_good.append(total)

                t0 = time.time()
                method(bad_patterns[i], bad_texts[i])
                t1 = time.time()
                total = t1-t0
                time_bad.append(total)
            time_good.sort()
            time_bad.sort()
            time_total.loc[df_index] = [good_files[i], str(method.__name__), get_mean(time_good),
                                         get_median(time_good), get_min(time_good), get_max(time_good), get_variance(time_good)]
            time_total.loc[df_index + 1] = [bad_files[i], str(method.__name__), get_mean(time_bad),
                                             get_median(time_bad), get_min(time_bad), get_max(time_bad), get_variance(time_bad)]
            df_index += 2
    return time_total




all_methods = [naive, robin_carp, kmp, bmh]
bad_patterns = []
bad_texts = []
good_patterns = []
good_texts = []
bad_files = []
good_files = []
for i in range(1,5):
    bad_files.append('bad_t_' + str(i) +'.txt')
    good_files.append( 'good_t_' + str(i) +'.txt')

    with open(BENCH_DIR + '/' + bad_files[-1], 'r') as file:
        bad_texts.append(file.read())
    with open(BENCH_DIR + '/bad_w_' + str(i) +'.txt', 'r') as file:
        bad_patterns.append(file.read())
    with open(BENCH_DIR + '/' +good_files[-1], 'r') as file:
        good_texts.append(file.read())
    with open(BENCH_DIR + '/bad_w_' + str(i) +'.txt', 'r') as file:
        good_patterns.append(file.read())

all_methods = [naive, robin_carp, kmp, bmh]


time_df = get_time_df(num_iterations=100, methods = all_methods)
time_df.to_csv('measurements')
