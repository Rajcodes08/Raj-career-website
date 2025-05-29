from flask import Flask, render_template, jsonify, request # flask is module # Flask is a class
from database import load_jobs_from_db,load_job_from_db, add_application_to_db # this function will load the jobs from the database

app = Flask(__name__) # __name__ is a special variable in Python that holds the name of the current module load_jobs_from_db # this function will load the jobs from the database   

@app.route('/') # jovian.ai/learn here jovian.ai is the domain and /learn is the path or route
 # / is empty path or root path
# @app.route('/hello') # this is a decorator that tells Flask what URL should call the function that follows
def hello_world():
    jobs = load_jobs_from_db() # this function will load the jobs from the database
    return render_template('home.html', jobs=jobs) # this function returns a string that will be displayed in the browser when the URL is accessed

@app.route('/friend/')
def hello_world2():
    return 'Hello, friend!'

@app.route('/api/jobs') # this is the API endpoint that will return the list of jobs in JSON format, that is a format that can be easily read by machines
def list_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)


@app.route("/job/<id>") 
def show_job(id):
    job = load_job_from_db(id)
    
    if not job:
        return "Job not found", 404

    return render_template('jobpage.html', job=job) 


@app.route("/job/<id>/apply", methods =['post']) # this is the API endpoint that will handle the job application
def apply_to_job(id):
    data = dict(request.form) # this will get the data from the query string of the URL
    
    job= load_job_from_db(id)
    add_application_to_db(id, data)
    return render_template('application_submitted.html', application=data, job=job) # this function will return the application submitted page in HTML format

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)