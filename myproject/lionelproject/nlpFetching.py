from conceptnet5_client.web.api import LookUp, Association
from conceptnet5_client.utils.result import Result


lookup = LookUp(limit = 1)
response = lookup.search_concept('chick-fil-a')
r = Result(response)
r.print_raw_result()
##edges = r.parse_all_edges(clean_self_ref = True) 
##[edge.print_edge() for edge in edges]

##a = Association()
##data = a.get_similar_concepts_by_term_list(['organization', 'company'])
##r = Result(data)
##r.print_raw_result()
