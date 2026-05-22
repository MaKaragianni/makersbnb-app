import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from lib.space import Space
from lib.space_repository import SpaceRepository
from lib.database_connection import DatabaseConnection
from datetime import date

"""
Testing that all() returns every space stored in the database
"""
def test_all_returns_all_spaces(db_connection):
    db_connection.seed("seeds/database_connection_test.sql")
    repository = SpaceRepository(db_connection)
    spaces = repository.all()
    assert spaces == [Space(1, 1, "Test Space", "Test Location", "Test Description", 100, date(2026, 5, 19), date(2026, 5, 30))]


"""
Testing that a user can successfully create a new space and it is added to the databases
"""
def test_user_can_create_a_space(db_connection):
    db_connection.seed("seeds/database_connection_test.sql")
    repository = SpaceRepository(db_connection)
    repository.create(Space(2, 1, "New Test Space", "New Test Location", "New Test Description", 200, date(2026, 6, 19), date(2026, 6, 30)))
    spaces = repository.all()
    assert spaces[-1] == Space(2, 1, "New Test Space", "New Test Location", "New Test Description", 200, date(2026, 6, 19), date(2026, 6, 30))