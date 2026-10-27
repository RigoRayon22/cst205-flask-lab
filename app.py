from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return """
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Classmates' Acronyms</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <h2>Classmates' Favorite Acronyms</h2>

        <p>Pedro: MIMS (Make It Make Sense)</p>
        <p>Daniel: QTQP (Quality Time Quality People)</p>
        <p>Ricahrd: FEAR (Face Everything And Rise)</p>
    </body>
    </html>
    """


@app.route("/rigoberto")
def favorite_acronym():
    acronym = "TWIN (Together We Ignore Negativity)"
    return render_template("template.html", acronym=acronym)


@app.route("/photo")
def photo():
    return render_template("photo.html")