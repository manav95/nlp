from conceptnet5_client.web.api import Search
# get how similar cats and dogs 
a = Association(filter='/c/en/dog', limit=1)
data = a.get_similar_concepts('cat')
r = Result(data)
# print results in key = value format 
r.print_raw_results()

a = Association()
data = a.get_similar_concepts_by_term_list(['toast', 'cereal', 'juice', 'egg'])
r = Result(data)
# print results in key = value format 
r.print_raw_results()
