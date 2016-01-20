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

    game_adj=request.args.get("adj")
    game_ptverb = request.args.get("pt-verb")
    game_plnoun =request.args.get("pl-noun")
    game_drink= request.args.get("drink")
    game_meal= request.args.get("meal")
    game_location= request.args.get("location")
    game_noun= request.args.get("noun")
    game_celebrity= request.args.get("celebrity")
    game_pers_trait= request.args.get("pers-trait")
    game_tv= request.args.get("tv")
    game_clothing= request.args.get("clothing")
    game_n_adj= request.args.get("n-adj")
    game_num=request.args.get("num")

    return render_template("madlib.html",
                            noun=game_noun,
                            ptverb=game_ptverb,
                            plnoun=game_plnoun,
                            adj=game_adj,
                            drink=game_drink,
                            meal=game_meal,
                            location=game_location,
                            celebrity=game_celebrity,
                            perstrait=game_pers_trait,
                            tv=game_tv,
                            clothing=game_clothing,
                            nadj=game_n_adj,
                            num=game_num)




if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)