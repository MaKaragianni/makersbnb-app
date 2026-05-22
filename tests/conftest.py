import pytest, sys, random, pytest, os
from pathlib import Path
from xprocess import ProcessStarter
from lib.database_connection import DatabaseConnection
from app import app

@pytest.fixture
def db_connection():
    conn = DatabaseConnection(test_mode=True)
    conn.connect()
    return conn


@pytest.fixture
def test_web_address(xprocess):
    python_executable = sys.executable
    app_file = Path(__file__).resolve().parent.parent / 'app.py'
    port = str(random.randint(4000, 4999))
    class Starter(ProcessStarter):
        env = {"PORT": port, "APP_ENV": "test", **os.environ}
        pattern = "Debugger PIN"
        args = [python_executable, app_file]

    xprocess.ensure("flask_test_server", Starter)

    yield f"localhost:{port}"

    xprocess.getinfo("flask_test_server").terminate()


@pytest.fixture
def web_client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client