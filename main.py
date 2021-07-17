import time
import json
from flask import Flask, jsonify
from flask.wrappers import Request
from flask_restx import reqparse, inputs, Resource, Api
import functions

app = Flask(__name__)
api = Api(app)

@api.errorhandler(RecursionError)
def handle_RecursionError(error):
    return ({'message': 'Reach recursion limit.'}, 500) 

@api.route('/ping')
class ping(Resource):
    def get(self):
        """
        Ping to verify the API is online
        """
        return {'status': 'ok'}

@api.route('/fibonacci/<int:n>', endpoint='fibonacci')
class fibonacci(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'page', 
        type=inputs.int_range(low=1,high=10000000), 
        default=1,
        help='Page index',
        required=False,
        location='args')
    parser.add_argument(
        'size', 
        type=inputs.int_range(low=1,high=10000000), 
        default=100,
        help='Page size',
        required=False,
        location='args')

    @api.expect(parser)
    def get(self,n):
        """
        Calculate Fibonacci sequence
        """

        args = self.parser.parse_args()
        page = args['page']
        size = args['size']

        start_time = time.perf_counter()
        fab = functions.F_with_cache(n,page,size)
        end_time = time.perf_counter()

        result = {}
        result['duration']  = round((end_time - start_time) * 1000,2)
        result['sequence']  = fab

        return result

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

