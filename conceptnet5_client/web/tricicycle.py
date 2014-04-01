from conceptnet5_client.utils.result import Result
from conceptnet5_client.web.api import Search
# Search for the edges whose relation is 'be often compared to'
s = Search(rel='/c/en/be_often_compare_to')
data = s.search()
r = Result(data)
# print results in key = value format 
r.print_raw_result()

# Search for any edge whose any of 'startLemmas', 'endLemmas' or 'relLemmas' matches 
# 'mariah carey' and whose 'surfaceText' matches 'dion'. Here the arg'something' is 
# not supported, so it will be ignored constructing query URL.
s = Search(text='mariah carey', surfaceText='dion', something='anything')
data = s.search()
r = Result(data)
# print results in key = value format 
r.print_raw_result()
