'''
Dennis Smith

Vacation Rental API ("home")

This File defines Home objects for the Vacation Rental API.
'''
import datetime as dt
from marshmallow import Schema, fields
from vacation.model.reservations import Reservation, ReservationSchema


class Home(object):
    '''
    A Home consists of an id, name, home type, location, list of
    reservations, date of Home creation, and a type.   
    '''
    def __init__(self,id, name, homeType, location, reservations):
        '''
        Method -- __init__
            Initializes a Home object.
        '''
        self.id = id
        self.name = name
        self.homeType = homeType
        self.location = location
        self.reservations = reservations
        self.created_at = dt.datetime.now()
        self.type = type

    def __repr__(self):
        '''
        Method -- __repr__
            Returns a printable representation of a Home Object.
        '''
        return '<Home(name={self.name!r})>'.format(self=self)


class HomeSchema(Schema):
    '''
        Schema -- HomeSchema
            HomeSchema defines the Schema of the Home object.
            This includes the data types for each parameter.
    '''
    id = fields.Integer(required=True)
    name = fields.Str()
    homeType = fields.Str()
    location = fields.Str()
    created_at = fields.Date()
    reservations = fields.List(fields.Nested(ReservationSchema))
    type = fields.Str()