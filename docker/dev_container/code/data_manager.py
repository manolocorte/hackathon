import pandas as pd
import psycopg2
from psycopg2 import sql
from sqlalchemy import create_engine

# Define your PostgreSQL database credentials
DATABASE = 'your_database'
USER = 'your_username'
PASSWORD = 'your_password'
HOST = 'localhost'
PORT = '5432'

# Create a SQLAlchemy engine
engine = create_engine(f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')

# Load your CSV data into a pandas DataFrame
df = pd.read_csv('your_file.csv')

# Write data from DataFrame to PostgreSQL table
df.to_sql('your_table', engine, if_exists='replace', index=False)