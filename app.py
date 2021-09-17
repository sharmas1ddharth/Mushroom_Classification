from flask import Flask, render_template
import mushroom_data as md

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html',
                           cap_shape=md.cap_shape,
                           )


if __name__ == '__main__':
    app.run()
