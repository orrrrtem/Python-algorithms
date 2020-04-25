import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from algorithms.string_searching.naive import naive
from algorithms.string_searching.robin_carp import robin_carp
from algorithms.string_searching.kmp import kmp
from algorithms.string_searching.bmh import bmh

text_test = 'ohoh;oh Fuck, oh, oh fucj, Fuck Fuuuuck   shiiit oh'
pattern_test = 'oh'
answer = [0, 2, 5, 14, 18, 49]

methods = [naive, robin_carp, kmp, bmh]

for method in methods:
    if  answer  == method(pattern_test,text_test):
          print(str(method.__name__),' passed')
    else:
          print(str(method.__name__),' failed')
          print(str(method.__name__),' return ', method(pattern_test,text_test) , ' instead of ', answer)

