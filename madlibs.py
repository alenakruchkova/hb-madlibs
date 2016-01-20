from random import choice

from flask import Flask, render_template, request, redirect


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/', methods=["GET"])
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello', methods=["GET"])
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet', methods=["GET"])
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/redirect', methods=["GET"])
def redirect_answer():
    """redirect user answer."""

    wants_to_play = request.args.get("yesno")

    if wants_to_play == "yes":
        return redirect('/game')
    else:
        return redirect('/goodbye')


@app.route('/game', methods=["GET"])
def play_game():
    """play game with user."""
    return render_template("game.html")

@app.route('/goodbye', methods=["GET"])
def say_goodbye():
    """bye bitch."""
    return render_template("goodbye.html")

@app.route('/madlib', methods=["GET"])
def show_madlib():
    """run users madlib game"""

    game_person = request.args.get("person")
    game_color =request.args.get("color")
    game_noun= request.args.get("noun")
    game_adj=request.args.get("adj")

    return render_template("madlib.html",
                            noun=game_noun,
                            person=game_person,
                            color=game_color,
                            adj=game_adj)




if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
