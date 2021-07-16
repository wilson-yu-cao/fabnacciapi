import time
from flask import Flask, jsonify
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

@api.route('/fibonacci')
class fibonacci(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'n', 
        type=inputs.int_range(low=0, high=9999), 
        help='N [0..9999] in Fibonacci number.', 
        required=True,
        location='args')

    @api.expect(parser)
    def get(self):
        """
        Calculate Fibonacci sequence
        """
        args = self.parser.parse_args()
        n = args['n']

        result = {}
        start_time = time.perf_counter()
        result['sequence'] = functions.F(n)
        result['duration'] = round((time.perf_counter() - start_time) * 1000,2)

        return result

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

