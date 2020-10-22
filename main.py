# import packages
import os
from flask import Flask
from flask_restx import Api, Resource


# import python file
import SparseArray

  
app = Flask(__name__)
api = Api(app)


@api.route('/sparse-array/<queries>/')
class MyResource (Resource):
    
    def get(self, queries):
        
        # Get strings from environment variables list and transform it into list
        # strings = ["tran", "ngoc", "phi", "tran", "ngoc"]
        strings = os.environ ["strings"]
        strings = strings.split (",")
        
        message = f"This is the strings : {strings}"
        print ("-" * len (message))
        print (message)
        print ("-" * len (message))
        
        # Transform queries into list
        #queries = input ()
        queries = queries.split (",")
        
        message = f"This is the queries : {queries}"
        print (message)
        print ("-" * len (message))
        
        # Matching
        sp = SparseArray.SparseArray (strings)
        sp.matching_strings (queries)
        
        result = sp.matching_strings (queries)
    
        print (f"This is the matching result : {result}")
        
        return {"string" : strings, "queries" : queries, "result" : result}
    
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', use_reloader=False)
    