from sqlalchemy import create_engine,text
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the database URL
DATABASE_URL = os.getenv('DATABASE_URL')

# Create engine
engine = create_engine(DATABASE_URL)

engine = create_engine('postgresql://postgres:Supabaseraj%40123@db.udfbyewmnfssfnyxzthr.supabase.co:5432/postgres')

with engine.connect() as connection:
    # Example query to test the connection
    result = connection.execute(text("SELECT * from jobs"))
    for row in result:
        print(row)
    
    # result_dicts = []
    # for row in result.all():
    #     result_dicts.append(row._asdict())  # Convert each row to a dictionary
    
    # print("type(result): ",type(result))
    # result_all= result.all()
    # print("type(result.all()): ",type(result_all))
    # #print("result.all(): ",result_all)
    
    # #print("result.all()[0]: ",result_all[0])
    # first_result = result_all[0]
    # print("type(first_result) : ", type(first_result))
    # first_result_dict = result_all[0]._asdict() # Convert to dictionary
    # print("type(first_result_dict) : ", type(first_result_dict))
    # print("first_result_dict: ", first_result_dict)
    
   #print(result_dicts)  # Print the list of dictionaries
    # Close the connection
    
def load_jobs_from_db():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * from jobs")) # this will execute the SQL query to select all rows from the jobs table
    jobs = []
    for row in result.all():
        jobs.append(row._asdict())
    return jobs     