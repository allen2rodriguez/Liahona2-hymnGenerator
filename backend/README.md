# Hymn Selection

A tool for selecting and tracking hymns for my church, using python and a MySQL database.

## Features

- Randomly selects hymns for opening, sacrament, intermediate, and closing positions.
- Avoids recent repeats for each hymn position.
- Tracks hymn history and allows editing past selections.
- Simple command-line interface.

## Requirements

- Python 3.11+
- [mysql-connector-python](https://pypi.org/project/mysql-connector-python/)
- MySQL server

## Setup

1. **Clone the repository** and navigate to the project directory.

2. **Install dependencies:**
   ```sh
   pip install mysql-connector-python
   ```

3. **Configure the database:**
   - Edit [`serverInfo.json`](serverInfo.json) with your MySQL connection credentials.
   - Run the SQL scripts in [`sql_scripts/`](sql_scripts/) to set up the database:
     ```sh
     mysql -u <user> -p < database_name < sql_scripts/createTables.sql
     mysql -u <user> -p < database_name < sql_scripts/insertTables.sql
     ```

## Usage

Run the main program:
```sh
python main.py
```
Follow the prompts to select hymns or view/edit hymn history.

## File Overview

- [`main.py`](main.py): Main entry point and CLI.
- [`selector.py`](selector.py): Logic for selecting hymns.
- [`inserter.py`](inserter.py): Inserts new hymn selections into the database.
- [`history.py`](history.py): View and edit hymn history.
- [`connect2server.py`](connect2server.py): Handles database connection.
- [`sql_scripts/`](sql_scripts/): SQL scripts to set up and populate the database.

## License

MIT License. See [`LICENSE`](LICENSE) for details.