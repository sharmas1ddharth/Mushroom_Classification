from flask import Flask, render_template
from mushroom_data import columns, model, mushroom_class, cap_shape

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html',
                           cap_shape=cap_shape)


if __name__ == '__main__':
    app.run()
