from conceptnet5_client.web.api import LookUp, Association, Search
from conceptnet5_client.utils.result import Result
import Queue 

def obama():
  limit = 1
  conceptDict = {'food': []}
  value = 'food'
  a = Association()
  lookup = LookUp()
  for i in range(limit):
   data = lookup.search_concept(value)
   r = Result(data)
   edges = r.parse_all_edges(clean_self_ref = True)
   edgeQueue = Queue.PriorityQueue()
   for edge in edges:
      if edge.end.split('/')[-1] != value: 
       edgeQueue.put((-1 * edge.weight,edge.end))
   itemOne = edgeQueue.get()[1].split('/')
   stringOne = itemOne[-1]
   itemTwo = edgeQueue.get()[1].split('/')
   stringTwo = itemTwo[-1]
   queueList = conceptDict[value]
   queueList.append(stringOne)
   queueList.append(stringTwo)
   data = a.get_similar_concepts_by_term_list([value, stringOne, stringTwo])
   r = Result(data)
   cubs = r.result['similar']
   [queueList.append(term[0].split('/')[-1]) for term in cubs]
   conceptDict[value] = queueList
   value = stringOne
   conceptDict[value] = []
   conceptDict[
  return conceptDict 
   
   
print obama()
