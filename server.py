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


@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html><a href='/hello'>Let's get started!</a></html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
        <style>
          form {
            display: inline-block;
            margin: 5px;
          }
        </style>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <p>Choose a compliment!</p>
          <select name="compliment">
            <option value="nice">Nice</option>
            <option value="great">Great</option>
            <option value="awesome">Awesome</option>
          </select>
          <input type="submit" value="Submit"> 
        </form>
        <br>
        <form action="/diss">
         What's your name? <input type="text" name="person">
          <p>Or choose an insult!</p>
          <select name="diss">
            <option value="smelly">smelly</option>
            <option value="mean">mean</option>
            <option value="just okay">just okay</option>
          </select>
          <input type="submit" value="Submit"> 
        </form>
      </body>
    </html>
    """

@app.route('/diss')
def insult_person():
  """Insults user"""

  player = request.args.get("person")
  diss = request.args.get("diss")

  return """
  <!doctype html>
  <html>
    <head>
      <title>A Compliment</title>
    </head>
    <body>
      Hi, {}! I think you're {}!
    </body>
  </html>
  """.format(player, diss)



@app.route('/greet')

def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
