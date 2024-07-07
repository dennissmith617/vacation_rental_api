'''
Dennis Smith

Vacation Rental API ("index")

This File houses the methods used in the Vacation Rental API Program.
The program uses 5 existing homes to show the functionality of the API.
/rentals serves as a GET method which returns all existing homes in the API.
/rent serves as a POST method, where users can request a reservation at an
existing vacation home. If the user's date input is correct (including
formatting, start date preceding end date, and a stay of one day or
greater), the home exists in the system, and the home is available for rental
for the user's requested dates, the system will add the user's requested
reservation to their selected home and notify the user of the successful
booking.
'''
import json
from flask import Flask, jsonify, request
from vacation.model.home import Home, HomeSchema
from vacation.model.reservations import Reservation, ReservationSchema
from datetime import datetime

app = Flask(__name__)

homes = [
    Home(1, 'Denny House', 'Beach House', 'Dennis',[]),
    Home(2, 'Maddie House', 'Beach House', 'Barnstable', []),
    Home(3, 'Luke House', 'Lake House', 'Yarmouth', []),
    Home(4, 'Hans House', 'City Apartment', 'Wakefield', []),
    Home(5, 'Jamie House', 'City Apartment', 'Wakefield', []),
]

@app.route('/rentals', methods=['GET'])
def get_rentals():
    '''
    Method -- get_rentals
        Returns the existing rental homes in the API
    '''
    schema = HomeSchema(many=True)
    rentals = schema.dump(homes)
    return jsonify(rentals)


@app.route('/rent', methods=['POST'])
def rent_home():
    '''
    Method -- rent_home
        Takes the user's reservation request as data, and parses
        it out to home_id, start_date, and end_date. Checks that
        start/end dates fulfill formatting requirements as well
        as program requirements (start date before end date, start
        and end date are not same day). Checks that home exists
        based on home_id, and that start/end dates do not overlap
        with any other rentals.

        Returns error statements if the request does not meet
        specified parameters, otherwise appends the reservation
        and returns a message of success.
    '''
    data = request.json
    home_id = data['home_id']
    start_date = data['start_date']
    end_date = data['end_date']

    try:
        # Clean dates
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'error': 'Invalid Date Format. Please use YY-MM-DD'}), 400

    if start_date > end_date:
        return jsonify({'error': 'Invalid Date Selection. Please ensure that the start date of your reservation occurs before the end date.'}), 400

    if start_date == end_date:
        return jsonify({'error': 'Invalid Date Selection. Please make your end date at least one day after your start date.'}), 400

    # Find the vacation home by id
    home_to_rent = None
    for home in homes:
        if home.id == home_id:
            home_to_rent= home

    if not home_to_rent:
        return jsonify({'error': 'Rental home not found, please try another ID.'}), 404

    # Check if the requested dates overlap with existing reservation dates
    for reservation in home_to_rent.reservations:
        if start_date < reservation.end_date and end_date > reservation.start_date:
            return jsonify({'error': 'Rental is already booked for this time period, please try again.'}), 400

    # Reserve the home
    res = Reservation(start_date,end_date)
    home_to_rent.reservations.append(res)
    return jsonify({'message': 'Reservation success!'})


if __name__ == '__main__':
   app.run(port=5000)