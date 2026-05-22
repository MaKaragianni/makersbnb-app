from playwright.sync_api import Page, expect
from app import app

def test_user_can_log_in(web_client, db_connection):
    db_connection.seed("seeds/database_connection_test.sql")

    response = web_client.post('/sessions', data={
        'email': "test@test.com",
        'password': 'hashed_password'
    })

    assert response.status_code == 302
    assert response.headers["Location"] == "/spaces"


def test_user_can_log_out(web_client):
    with web_client.session_transaction() as sess:
        sess["user_email"] = "test@test.com"

    response = web_client.post('/logout')
    assert response.status_code == 302
    assert response.headers["Location"] == "/"

    with web_client.session_transaction() as sess:
        assert "user_email" not in sess
    