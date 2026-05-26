from playwright.sync_api import Page, expect
from lib.space_repository import SpaceRepository
from app import app
from lib.booking import Booking
from lib.booking_repository import BookingRepository
from lib.space import Space
from datetime import date


def test_get_single_space(db_connection, web_client):
    db_connection.seed("seeds/database_connection_test.sql")
    response = web_client.get('/spaces/1')
    assert response.status_code == 200
    assert b'<form' in response.data
    assert b'Test Space' in response.data


def test_get_index(page: Page):
    page.goto("http://127.0.0.1:5001/")
    h1 = page.locator("h1")
    expect(h1).to_have_text("Find Beautiful Spaces To Stay")


def test_get_spaces(db_connection, web_client):
    db_connection.seed("seeds/database_connection_test.sql")
    with web_client.session_transaction() as sess:
        sess['user_email'] = 'test@test.com'
    response = web_client.get('/spaces/new')
    assert response.status_code == 200
    assert b'<form' in response.data


def test_post_spaces_creates_new_space(db_connection, web_client):
    db_connection.seed("seeds/database_connection_test.sql")
    with web_client.session_transaction() as sess:
        sess['user_email'] = 'test@test.com'
    response = web_client.post('/spaces', data={'space_name': 'Cozy Cottage', 'space_location': 'Cornwall', 'space_description': 'A lovely cottage by the sea', 'price_per_night': 150, 'available_from': '2026-06-01', 'available_to': '2026-08-31'})
    assert response.status_code == 302
    repository = SpaceRepository(db_connection)
    spaces = repository.all()
    assert len(spaces) == 2


def test_get_spaces_shows_all_spaces(db_connection, web_client):
    db_connection.seed("seeds/database_connection_test.sql")
    response = web_client.get('/spaces')
    assert response.status_code == 200
    assert b'Test Space' in response.data


def test_get_request_shows_booking_made_and_received(db_connection, web_client):
    db_connection.seed("seeds/database_connection_test.sql")
    with web_client.session_transaction() as sess:
        sess['user_email'] = 'test@test.com'
        sess['user_id'] = 1
        
    response = web_client.get('/requests')
    assert response.status_code == 200


def test_get_signup_form_returns_200():
    client = app.test_client()
    response = client.get("/signup")
    assert response.status_code == 200


def test_create_user_inserts_into_database():
    from lib.database_connection import DatabaseConnection
    connection = DatabaseConnection(test_mode=True)
    connection.connect()
    connection.execute("TRUNCATE TABLE users CASCADE;")
    client = app.test_client()
    response = client.post("/users", data={
        "email": "test@test.com",
        "password": "hashed_password"
    })
    assert response.status_code == 302
    assert response.headers["Location"] == "/spaces"
    result = connection.execute(
        "SELECT email, password_hash FROM users WHERE email = %s",
        ["test@test.com"]
    )[0]
    assert result["email"] == "test@test.com"
    assert result["password_hash"] == "hashed_password"
