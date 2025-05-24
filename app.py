from flask import Flask, render_template, jsonify # flask is module # Flask is a class

app = Flask(__name__) # __name__ is a special variable in Python that holds the name of the current module # app is object of class Flask
# __name__ is used to determine if the script is being run directly or imported as a module

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Remote'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'San Francisco, USA',
        'salary': 'Rs. 25,00,000'
    }
]

@app.route('/') # jovian.ai/learn here jovian.ai is the domain and /learn is the path or route
 # / is empty path or root path
# @app.route('/hello') # this is a decorator that tells Flask what URL should call the function that follows
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name=' Raj ') # this function returns a string that will be displayed in the browser when the URL is accessed

@app.route('/friend/')
def hello_world2():
    return 'Hello, friend!'

@app.route('/api/jobs') # this is the API endpoint that will return the list of jobs in JSON format, that is a format that can be easily read by machines
def list_jobs():
    return jsonify(JOBS)



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)