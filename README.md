# MakersBnB 

A Flask + PostgreSQL accommodation booking platform.

## Features

- User authentication
- List spaces
- Request bookings
- View booking requests
- PostgreSQL database
- Pytest test suite

## Tech Stack

- Python
- Flask
- PostgreSQL
- Pytest
- Playwright


## Installation
Step-by-step instructions on how to set up the development environment.
1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/MaKaragianni/makersbnb-python-seed.git
   \`\`\`
2. Navigate into the directory:
   \`\`\`bash
   cd your-repo-name
   \`\`\`
3. Set up your virtual environment:
   \`\`\`bash
   python -m venv <your-venv-name>
   \`\`\`bash
   source <your-venv-name>/bin/activate
4. Install dependencies:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`
5. Create your database:
   \`\`\`bash
   createdb makersbnb
   createdb makersbnb_test
6. Seed database:
   \`\`\`bash
   psql -d makersbnb -f seeds/makersbnb.sql
   psql -d makersbnb_test -f seeds/database_connection_test.sql
7. Run the app and go to the server link in your browser (http://127.0.0.1:5001):
   \`\`\`bash
   python app.py
8. In a new terminal run Pytest to make sure all tests are passing:
   \`\`\`bash
   pytest
 
 Your app is running! 



