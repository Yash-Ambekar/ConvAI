from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import sys
sys.path.insert(0, '/home/yash/Wallmart-Hackathon-Project/flask/services')
from fewShotAgent import mainFunc

# Initializing flask app
app = Flask(__name__)
CORS(app) 


@app.route('/', methods=["POST"])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])

def llmCall():
    try:
        data = request.json
        query = data['query']
        print("Incoming Query: ", query)
        result = mainFunc(query)
        response = jsonify({"result": result['output']})
        return response
    except:
        print("LLM call error")
        response = jsonify({"Error": "LLM call error"})
        return response
                
    
      
# Running app
if __name__ == '__main__':
    app.run(debug=True)