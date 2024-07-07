'''
Dennis Smith

Vacation Rental API ("reservations")

This File defines Reservation objects for the Vacation Rental API.
'''
import datetime as dt
from marshmallow import Schema, fields


class Reservation(object):
    '''
    A Reservation consists of a start date, end date,
    date at which the Reservation was created, and a type.  
    '''
    def __init__(self,start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.created_at = dt.datetime.now()
        self.type = type

    def __repr__(self):
        '''
        Method -- __repr__
            Returns a printable representation of a Reservation Object.
        '''
        return '<Reservation(start_date={self.start_date!r})>'.format(self=self)


class ReservationSchema(Schema):
    '''
        Schema -- ReservationSchema
            ReservationSchema defines the Schema of the Reservation object.
            This includes the data types for each parameter.
    '''
    start_date = fields.Date()
    end_date = fields.Date()
    created_at = fields.Date()
    type = fields.Str()