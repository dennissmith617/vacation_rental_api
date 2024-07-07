import json
from flask import Flask, jsonify, request
from vacation.model.home import Home, HomeSchema
from vacation.model.user import User, UserSchema

app = Flask(__name__)

homes = [
    Home('Denny House', 'Beach House', 'Dennis'),
    Home('Maddie House', 'Beach House', 'Barnstable'),
    Home('Luke House', 'Lake House', 'Yarmouth'),
    Home('Hans House', 'City Apartment', 'Wakefield'),
    Home('Jamie House', 'City Apartment', 'Wakefield'),
]

users = [
	Users('Maddie', 'maddie@gmail.com'),
	Users('Dennis', 'dennis@gmail.com')

]

@app.route('/rentals', methods=['GET'])
def get_rentals():
 return jsonify(rentals)


if __name__ == '__main__':
   app.run(port=5000)