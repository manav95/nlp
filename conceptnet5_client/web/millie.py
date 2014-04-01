from conceptnet5_client.web.api import Association
from conceptnet5_client.utils.result import Result
# get how similar cats and dogs 
a = Association(filter='/c/en/taco bell', limit=12)
data = a.get_similar_concepts('chick-fil-a')
r = Result(data)
# print results in key = value format 
r.print_raw_result()

a = Association()
data = a.get_similar_concepts_by_term_list(['chick-fil-a', 'restaurant', 'food', 'mcdonalds'])
r = Result(data)
# print results in key = value format 
r.print_raw_result()
