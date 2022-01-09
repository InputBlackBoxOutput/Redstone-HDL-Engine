import os, re, json
import pymongo
from bson.json_util import ObjectId

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from synth import RedstoneSynth
from yosys import Yosys

api = Flask(__name__)
cors = CORS(api)

# Connect with mongoDB
DB_USER = os.environ.get("DB_USER")
DB_PASSWD = os.environ.get("DB_PASSWD")

client = pymongo.MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASSWD}@cluster0.ff8np.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client['Redstone-HDL']
collection = db['contraption']

# Setup JSON encoder for ObjectId
class JSON_Encoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super(JSON_Encoder, self).default(obj) 

api.json_encoder = JSON_Encoder

# Helper function to create verilog file to process
def create_verilog_file(code):
	code = code[2:-1]
	code = code.split("\\r\\n")
	code = "\n".join(code)

	verilog_file = f"{abs(hash(code))}.v"
	with open(verilog_file, 'w') as _file:
		_file.write(code)

	return verilog_file


@api.route('/synthesize', methods=['POST'])
@cross_origin()
def synthesize():
	verilog_file = create_verilog_file(str(request.data))

	try:
		s = RedstoneSynth(verilog_file)
		redstone_circuit = {"contraption": s.synthesize()}
		
		collection.insert_one(redstone_circuit)
		response = redstone_circuit
	except:
		response = jsonify({"error": "Something went wrong!"})
	finally:
		os.remove(verilog_file)

	return response

@api.route('/link', methods=['GET'])
@cross_origin()
def link():
	if request.args.get("id"):
		_id = request.args.get("id")
		db_data = []
		for x in collection.find({"_id" : ObjectId(_id)}):
			db_data.append(x)
		
		response = jsonify(db_data)
	else:
		response = (jsonify({"error": "ID required"}), 400)

	return response

@api.route('/netlist', methods=['POST'])
@cross_origin()
def netlist():
	verilog_file = create_verilog_file(str(request.data))

	try:
		y = Yosys()
		netlist_json = y.process(verilog_file)	
		response = (jsonify({"output": netlist_json}), 200)
	except:
		response = (jsonify({"error": "Something went wrong!"}), 400)
	finally:
		os.remove(verilog_file)

	return response

@api.route('/',methods=['GET'])
@cross_origin()
def root():
	return jsonify({"success": 1})	

if __name__ == '__main__':
    api.run(port=5000, debug=True)