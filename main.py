# import
import os
import SparseArray


if __name__ == '__main__':
    
    strings = os.environ ["strings"]
    strings = strings.split (",")
    
    message = f"This is the strings : {strings}"
    print ("-" * len (message))
    print (message)
    print ("-" * len (message))
    
    # strings = ["tran", "ngoc", "phi", "tran", "ngoc"]
    
    print ("Please enter the queries. For example : tran,ngoc,phi")
    queries = input ()
    queries = queries.split (",")
    
    message = f"This is the queries : {queries}"
    print (message)
    print ("-" * len (message))
    
    sp = SparseArray.SparseArray (strings)
    
    sp.matching_strings (queries)
    
    
    result = sp.matching_strings (queries)

    print (f"This is the matching result : {result}")