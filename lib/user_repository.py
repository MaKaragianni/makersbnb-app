from lib.user import User

class UserRepository:

    def __init__(self, connection):
        self._connection = connection

    def create(self, user):
        self._connection.execute(
            'INSERT INTO users (email, password_hash) VALUES (%s, %s)',
            [user.email, user.password]
        )
    
    def find_by_email(self, email):
        rows = self._connection.execute(
            "SELECT id, email, password_hash FROM users WHERE email = %s",
            [email]
        )

        if len(rows) == 0:
            return None

        row = rows[0]

        return User(row["email"], row["password_hash"], row["id"])