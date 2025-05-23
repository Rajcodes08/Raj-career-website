from flask import Flask, render_template # flask is module # Flask is a class

app = Flask(__name__) # __name__ is a special variable in Python that holds the name of the current module # app is object of class Flask
# __name__ is used to determine if the script is being run directly or imported as a module

@app.route('/') # jovian.ai/learn here jovian.ai is the domain and /learn is the path or route
 # / is empty path or root path
# @app.route('/hello') # this is a decorator that tells Flask what URL should call the function that follows
def hello_world():
    return render_template('home.html') # this function returns a string that will be displayed in the browser when the URL is accessed

@app.route('/friend/')
def hello_world2():
    return 'Hello, friend!'

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)