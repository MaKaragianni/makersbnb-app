import sys
import os
from datetime import date
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from lib.booking import Booking
from lib.booking_repository import BookingRepository
from lib.database_connection import DatabaseConnection

def test_create_booking(db_connection):
    db_connection.seed("seeds/database_connection_test.sql")
    repository = BookingRepository(db_connection)

    repository.create(Booking(None, 1, 1, date(2026, 5, 20), 'pending'))

    bookings = repository.all()

    assert len(bookings) == 2
    assert bookings[-1].space_id == 1
    assert bookings[-1].user_id == 1
    assert bookings[-1].booking_date == date(2026, 5, 20)
    assert bookings[-1].booking_status == 'pending'

def test_find_by_user_id_returns_booking_made_by_user(db_connection):
    db_connection.seed("seeds/database_connection_test.sql")
    repository = BookingRepository(db_connection)

    bookings = repository.find_by_user_id(1)
    assert len(bookings) == 1
    assert bookings[0].user_id == 1

def test_find_by_space_owner_returns_booking_received(db_connection):
    db_connection.seed("seeds/database_connection_test.sql")
    repository = BookingRepository(db_connection)

    bookings = repository.find_by_space_owner(1)
    assert len(bookings) == 1
    assert bookings[0].space_id == 1