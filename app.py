from flask import Flask, render_template, request
import mushroom_data as md
import random

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method != 'POST':
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
                               habitat=md.habitat,
                               prediction=None
                               )
    else:
        collected_values = [collect_form_values()]
        prediction = classify_mushroom(collected_values)
        if prediction == 1:
            prediction_value = 'Poisonous'
        else:
            prediction_value = 'Edible'

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
                               habitat=md.habitat,
                               prediction=prediction_value
                               )


def collect_form_values():
    mushroom_values = [request.form.get('cap-shape'), request.form.get('cap-surface'),
                       request.form.get('cap-color'), request.form.get('bruises'),
                       request.form.get('odor'), request.form.get('gill-attachment'),
                       request.form.get('gill-spacing'), request.form.get('gill-size'),
                       request.form.get('gill-color'), request.form.get('stalk-shape'),
                       request.form.get('stalk-root'), request.form.get('stalk-surface-above-ring'),
                       request.form.get('stalk-surface-below-ring'),
                       request.form.get('stalk-color-above-ring'),
                       request.form.get('stalk-surface-below-ring'), request.form.get('veil-color'),
                       request.form.get('ring-number'), request.form.get('ring-type'),
                       request.form.get('spore-print-color'), request.form.get('population'),
                       request.form.get('habitat')]

    return mushroom_values


def classify_mushroom(values):
    prediction = md.model.predict(values)
    return prediction



if __name__ == '__main__':
    app.run()
