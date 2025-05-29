from sqlalchemy import create_engine,text
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the database URL
DATABASE_URL = os.getenv('DATABASE_URL')

# Create engine
engine = create_engine(DATABASE_URL)

# with engine.connect() as connection:
#     # Example query to test the connection
#     result = connection.execute(text("SELECT * from jobs"))
#     for row in result:
#         print(row)
    
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

def load_job_from_db(id):
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * from jobs where id = :val"), {"val": id})
        rows = result.all()
        # print("rows: ", rows)
        if len(rows) == 0:
            return None
        else:
            return rows[0]._asdict()
        
        
def add_application_to_db(job_id, data):
    with engine.begin() as connection:
        query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
        print("inserting this into db ",data)
        connection.execute(query, {
            'job_id': job_id,
            'full_name': data['full_name'],
            'email': data['email'],
            'linkedin_url': data['linkedin_url'],
            'education': data['education'],
            'work_experience': data['work_experience'],         
            'resume_url': data['resume_url']
        })        