import traceback

class SparseArray:
    
    def __init__ (self, strings):
        self.strings = strings
        
    def matching_strings (self, queries):
        try:
            # only take unique values of queries
            queries = list (set (queries))
            
            # length of arrays
            n_strings = len (self.strings)
            n_queries = len (queries)
            
            # max size of elements in arrays
            size_strings = max ([len (element) for element in self.strings])
            size_queries = max ([len (element) for element in queries])
            
            if min (n_strings, n_queries) < 1 or max (n_strings, n_queries) > 1000:
                raise Exception ("length of arrays must be in [1, 1000]")
            
            if min (size_strings, size_queries) < 1 or max (size_strings, size_queries) > 20:
                raise Exception ("size of elements in array must be in [1, 20]")
                
            
            dictionary = {}
             
            for query in queries:
                dictionary [query] = self.strings.count (query)
        
            return (dictionary)
        
        except Exception as e:
            return ({"error" : e, "traceback" : traceback.format_exc ()})