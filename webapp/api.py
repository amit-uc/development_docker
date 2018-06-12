from flask import Flask, request
import json
app = Flask(__name__)

@app.route("/product", methods=['get'])
def get_product():

	return json.dumps({
				'products': [
					'Ice Cream',
					'Chocolate',
					'Fruit',
					'Eggs',
					'Samosa',
					'Kachori',
					'lassi',
					'Pizza',
					'Shev Puri'
				]
			})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=9876, debug=True)