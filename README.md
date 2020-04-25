# Python-algorithms
Python algorithms for HSE PMI course
## Currently supported:
 - String Searching
 
## String Searching algorithms:
  - Naive
  - Knuth Morris Pratt 
  - Boyer–Moore–Horspool
  - Rabin-Karp  
  
[Examples](https://github.com/orrrrtem/Python-algorithms/blob/master/Pattern_Searching.ipynb) of string searching algorithms with measurements. 

Avaiable [tests](https://github.com/orrrrtem/Python-algorithms/blob/master/tests/test_string_searching.py) and [measurements](https://github.com/orrrrtem/Python-algorithms/tree/master/tools/string_searching) 



[Graphs](https://github.com/orrrrtem/Python-algorithms/blob/master/tools/string_searching/image.png) for middle complexity dataset
![Graphs for middle complexity dataset](https://github.com/orrrrtem/Python-algorithms/blob/master/tools/string_searching/image.png)

FULL Perfomance table: 

|file|method      |mean      |median                |min                   |max                   |variance              |
|----|------------|----------|----------------------|----------------------|----------------------|----------------------|
|good_t_1.txt|naive       |0.000159  |0.000156              |0.000154              |0.000201              |0.000000              |
|bad_t_1.txt|naive       |0.000004  |0.000004              |0.000004              |0.000007              |0.000000              |
|good_t_1.txt|robin_carp  |0.000421  |0.000395              |0.000386              |0.000821              |0.000000              |
|bad_t_1.txt|robin_carp  |0.000007  |0.000006              |0.000005              |0.000023              |0.000000              |
|good_t_1.txt|kmp         |0.000168  |0.000166              |0.000164              |0.000184              |0.000000              |
|bad_t_1.txt|kmp         |0.000006  |0.000006              |0.000005              |0.000011              |0.000000              |
|good_t_1.txt|bmh         |0.000456  |0.000428              |0.000419              |0.000819              |0.000000              |
|bad_t_1.txt|bmh         |0.000126  |0.000116              |0.000114              |0.000240              |0.000000              |
|good_t_2.txt|naive       |0.000266  |0.000262              |0.000259              |0.000355              |0.000000              |
|bad_t_2.txt|naive       |0.000135  |0.000133              |0.000132              |0.000161              |0.000000              |
|good_t_2.txt|robin_carp  |0.000653  |0.000649              |0.000632              |0.000751              |0.000000              |
|bad_t_2.txt|robin_carp  |0.000046  |0.000045              |0.000044              |0.000080              |0.000000              |
|good_t_2.txt|kmp         |0.000286  |0.000284              |0.000277              |0.000373              |0.000000              |
|bad_t_2.txt|kmp         |0.000055  |0.000054              |0.000052              |0.000080              |0.000000              |
|good_t_2.txt|bmh         |0.000216  |0.000213              |0.000211              |0.000285              |0.000000              |
|bad_t_2.txt|bmh         |0.000186  |0.000182              |0.000180              |0.000265              |0.000000              |
|good_t_3.txt|naive       |0.000799  |0.000787              |0.000772              |0.001430              |0.000000              |
|bad_t_3.txt|naive       |0.013747  |0.013629              |0.013514              |0.017201              |0.000000              |
|good_t_3.txt|robin_carp  |0.002014  |0.001959              |0.001907              |0.003601              |0.000000              |
|bad_t_3.txt|robin_carp  |0.000499  |0.000483              |0.000466              |0.000870              |0.000000              |
|good_t_3.txt|kmp         |0.000936  |0.000868              |0.000845              |0.002857              |0.000000              |
|bad_t_3.txt|kmp         |0.000575  |0.000540              |0.000518              |0.002301              |0.000000              |
|good_t_3.txt|bmh         |0.000154  |0.000151              |0.000148              |0.000234              |0.000000              |
|bad_t_3.txt|bmh         |0.000904  |0.000896              |0.000879              |0.001052              |0.000000              |
|good_t_4.txt|naive       |0.002653  |0.002610              |0.002524              |0.004799              |0.000000              |
|bad_t_4.txt|naive       |0.715517  |0.713572              |0.701930              |0.754016              |0.000066              |
|good_t_4.txt|robin_carp  |0.006410  |0.006349              |0.006261              |0.008467              |0.000000              |
|bad_t_4.txt|robin_carp  |0.002593  |0.002562              |0.002497              |0.004555              |0.000000              |
|good_t_4.txt|kmp         |0.003075  |0.003064              |0.003049              |0.003221              |0.000000              |
|bad_t_4.txt|kmp         |0.003313  |0.003296              |0.003270              |0.003584              |0.000000              |
|good_t_4.txt|bmh         |0.000263  |0.000256              |0.000247              |0.000500              |0.000000              |
|bad_t_4.txt|bmh         |0.003982  |0.003909              |0.003859              |0.007074              |0.000000              |

