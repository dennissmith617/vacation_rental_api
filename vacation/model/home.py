import datetime as dt

from marshmallow import Schema, fields
from vacation.model.reservations import Reservation, ReservationSchema


class Home(object):
    def __init__(self,id, name, homeType, location, reservations):
        self.id = id
        self.name = name
        self.homeType = homeType
        self.location = location
        self.reservations = reservations
        self.created_at = dt.datetime.now()
        self.type = type

    def __repr__(self):
        return '<Home(name={self.name!r})>'.format(self=self)


class HomeSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.Str()
    homeType = fields.Str()
    location = fields.Str()
    created_at = fields.Date()
    reservations = fields.List(fields.Nested(ReservationSchema))
    type = fields.Str()