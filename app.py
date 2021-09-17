from flask import Flask, render_template
import mushroom_data as md

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html',
                           cap_shape=md.cap_shape,
                           cap_surface=md.cap_surface,
                           cap_color=md.cap_color,
                           bruises=md.bruises,
                           odor=md.odor,
                           gill_attachment=md.gill_attachment,
                           gill_spacing=md.gill_spacing,
                           gill_size=md.gill_size,
                           gill_color=md.gill_color,
                           )


if __name__ == '__main__':
    app.run()
