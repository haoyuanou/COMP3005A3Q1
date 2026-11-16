# COMP3005 A3 Q1: Database Interaction

## Project Structure
- `main.py`: Python application containing CRUD operations (add, update, delete, get all students).
- `db_setup.sql`: SQL script to create the `students` table and insert initial dummy data.

## Setup Instructions
1. **Database Setup**: 
   Open pgAdmin, create a database, and execute the SQL script found in `db_setup.sql` to initialize the `students` table.
2. **Install Dependencies**:
   Open a terminal and run the following command to install the PostgreSQL adapter:
   ```bash
   pip install psycopg2-binary