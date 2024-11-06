from flask import Flask
import random
random_number = random.randint(0,9)
print(random_number)
app = Flask(__name__)
@app.route("/")
def CreateHead():
    return ("<h1>Guess The Number From 0 To 9<h1>/" \
            "<img src='https://media.giphy.com/media/IokAQCByJS254Dmw6f/giphy.gif?cid=790b76114w2cumjesjz5nkaxi27ihft4hxarb5xq5flcb420&ep=v1_gifs_search&rid=giphy.gif&ct=g', width=500, height=500/>")
@app.route("/<int:guess>")
def Check(guess):
    if guess > random_number:
        return "<h1style='color: red text-align = center'> The Guess number is To High, Try Again</h1>" \
                "<img src='https://media.giphy.com/media/EVV3azBPAF3kyKxX1S/giphy.gif?cid=790b7611dlzs8wx83aitb1laoomx0x200vjjivdtkr7wm6j0&ep=v1_gifs_search&rid=giphy.gif&ct=g'/>"
    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)