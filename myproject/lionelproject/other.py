from conceptnet5_client.web.api import LookUp, Association, Search
from conceptnet5_client.utils.result import Result
import Queue 

limit = 5
conceptDict = {'food': []}
value = '/c/en/food'
a = Association()
lookup = LookUp()
for i in range(limit):
   data = lookup.search_concept(value)
   r = Result(data)
   edges = r.parse_all_edges(clean_self_ref = True)
   edgeQueue = Queue.PriorityQueue()
   for edge in edges:
      if edge.end != value: 
       edgeQueue.put((-1 * edge.weight,edge.end))
   itemOne = edgeQueue.get()[1]
   itemTwo = edgeQueue.get()[1]
   print itemOne
   print itemTwo
