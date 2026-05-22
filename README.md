# MakersBnB 

## Project Description

**MakersBnB** is a full-stack web application designed to simplify the process of listing, discovering, and booking unique accommodations. Inspired by the core functionalities of Airbnb, the platform acts as a centralised marketplace that connects property owners with guests. 

Built with a focus on seamless user experience and secure data handling, MakersBnB handles the entire lifecycle of a property rental, from user authentication and dynamic space creation to availability management and booking requests.

### Key Features

*   **User Authentication & Security:** Secure sign-up and log-in portals ensuring user data privacy. Users must be authenticated to list or book spaces.
*   **Dynamic Space Listings:** Users can effortlessly list their own properties with details such as name, descriptions, price per night, and available dates.
*   **Interactive Marketplace:** An intuitive dashboard where users can browse all available spaces posted by the community.
*   **Streamlined Booking System:** Guests can select a space, choose their desired dates, and instantly submit a booking request.


## Getting Started

Follow these steps to get a local copy up and running.

## Tech Stack

*   **Frontend:** [HTML, CSS, Python]
*   **Backend:** [Python/Flask] 
*   **Database Adapter:** [psycopg]
*   **Templating Engine:** [Jinja2 (HTML/CSS)]
*   **Database:** [PostgreSQL]
*   **Testing Suite:** [PyTest]

### Installation
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



