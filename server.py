"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']
MEANNESS = ["lazy","lacking character","not motivated","a backstabber"]

@app.route('/')
def start_here():
    """Home page."""
    
    return """<!doctype html><html>Hi! This is the home page.
    <a href="http://127.0.0.1:5000/hello">Visit hello page</a>
    </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit">
          
          <p>Select a compliment: <p>
          <input type="radio" value="onion-like" name="compliments" id="onion-like">
          <label for="onion-like">Multi-Layered Like an Onion</label>
          <input type="radio" value="intelligent" id= "intelligence." name="compliments">
          <label for="intelligence">You are intelligent.</label>
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""
    player = request.args.get("person")
    nice_words = request.args.get("compliments")

    #compliment = choice(AWESOMENESS)

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {nice_words}!
      </body>
    </html>
    """

@app.route('/diss')
def diss_person():
  """Dish out insults"""
  player = request.args.get("person")
  insult = choice(MEANNESS)

  return f"""
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi, {player}! I think you're {insult}!
      </body>
    </html>
    """

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
