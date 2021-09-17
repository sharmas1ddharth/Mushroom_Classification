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
                           stalk_shape=md.stalk_shape,
                           stalk_root=md.stalk_root,
                           stalk_surface_above_ring=md.stalk_surface_above_ring,
                           stalk_surface_below_ring=md.stalk_surface_below_ring,
                           stalk_color_above_ring=md.stalk_color_above_ring,
                           stalk_color_below_ring=md.stalk_color_below_ring,
                           veil_color=md.veil_color,
                           ring_number=md.ring_number,
                           ring_type=md.ring_type,
                           spore_print_color=md.spore_print_color,
                           population=md.population,
                           habitat=md.habitat
                           )


#TODO: function to collect form values
#TODO: prdict function
#TODO: show predicition in the web page
#TODO: make random button work



if __name__ == '__main__':
    app.run()
