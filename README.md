# University Database
This is a project of a database for a university/school. It manages data of students, teachers, subjects, groups, and grades. Can be helpful in organizing and querying data

## Technologies Used
- **Python 3.11**
- **PostgreSQL** - for data storage
- **SQLAlchemy** - ORM used to interact with the database
- **Faker** - for generating random data to fill in the database

## Setup
1. Clone this repository:
```bash
git clone https://github.com/yourusername/university-database.git
cd university-database
```
2. Install Poetry (if you don't have it installed already):
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
3. Install project dependencies using Poetry:
```bash
poetry install
```
4. Set up your PostgreSQL database:

Ensure that PostgreSQL is installed and running on your system.
If you don't have the database set up yet, create a `.env` file based on `.env.example` (see below) and then run `reset_db.py` to create the database from scratch.

`.env.example`:
```env
# PostgreSQL Database connection parameters
DB_USER=your_database_username
DB_PASS=your_database_password
DB_NAME=your_database_name
DB_HOST=your_domain
DB_PORT=your_port
```
`reset_db.py`: This script will completely drop your existing database and recreate it from scratch (empty). To create the database, run the following command:
```bash
poetry run python reset_db.py
```
5. Run database migrations to create the required tables:
```bash
poetry run alembic upgrade head
```
## Usage
Once the setup is complete, you can populate the database with fake data, running `seed.py`, and interact with it through Python scripts in `my_select.py`