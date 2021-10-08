import pickle
import pandas as pd

columns = {'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
           'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
           'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
           'stalk-surface-below-ring', 'stalk-color-above-ring',
           'stalk-color-below-ring', 'veil-color', 'ring-number',
           'ring-type', 'spore-print-color', 'population', 'habitat'}


cap_shape = {0: 'convex', 5: 'bell', 2: 'sunken', 3: 'flat', 4: 'knobbed', 1: 'conical'}
# ['x', 'b', 's', 'f', 'k','c']
cap_surface = {2: 'smooth', 0: 'scaly', 3: 'fibrous', 1: 'grooves'}  # ['s', 'y', 'f', 'g']
cap_color = {8: 'brown', 3: 'yellow', 4: 'white', 2: 'gray', 9: 'red', 7: 'pink', 0: 'buff', 1: 'purple', 6: 'cinnamon',
             5: 'green'}  # ['n', 'y', 'w', 'g', 'e', 'p', 'b', 'u', 'c', 'r']
bruises = {0: 'bruises', 1: 'no bruises'}  # {'t', 'f'}
odor = {5: 'pungent', 8: 'almond', 2: 'anise', 7: 'none', 3: 'foul', 1: 'creosote', 0: 'fishy', 6: 'spicy', 4: 'musty'}
# {'p', 'a', 'l', 'n', 'f', 'c', 'y', 's', 'm'}
gill_attachment = {1: 'free', 0: 'attached'}  # {'f', 'a'}
gill_spacing = {1: 'close', 0: 'crowded'}  # {'c', 'w'}
gill_size = {0: 'narrow', 1: 'broad'}  # {'n', 'b'}
gill_color = {2: 'black', 4: 'brown', 9: 'gray', 0: 'pink', 7: 'white', 5: 'chocolate', 10: 'purple', 3: 'red',
              11: 'buff',
              1: 'green', 8: 'yellow', 6: 'orange'}  # {'k', 'n', 'g', 'p', 'w', 'h', 'u', 'e', 'b', 'r', 'y', 'o'}
stalk_shape = {0: 'enlarging', 1: 'tapering'}  # {'e', 't'}
stalk_root = {0: 'equal', 3: 'club', 1: 'bulbous', 2: 'rooted', 4: 'missing'}  # {'e', 'c', 'b', 'r', '?'}
stalk_surface_above_ring = {2: 'smooth', 0: 'fibrous', 1: 'silky', 3: 'scaly'}  # {'s', 'f', 'k', 'y'}
stalk_surface_below_ring = {1: 'smooth', 0: 'fibrous', 2: 'scaly', 3: 'silky'}  # {'s', 'f', 'y', 'k'}
stalk_color_above_ring = {7: 'white', 6: 'gray', 4: 'pink', 3: 'brown', 0: 'buff', 5: 'red', 1: 'orange', 2: 'cinnamon',
                          8: 'yellow'}  # {'w', 'g', 'p', 'n', 'b', 'e', 'o', 'c', 'y'}
stalk_color_below_ring = {7: 'white', 3: 'pink', 6: 'gray', 0: 'buff', 4: 'brown', 5: 'red', 1: 'yellow', 8: 'orange',
                          2: 'cinnamon'}  # {'w', 'p', 'g', 'b', 'n', 'e', 'y', 'o', 'c'}
veil_color = {2: 'white', 0: 'brown', 1: 'orange', 3: 'yellow'}  # {'w', 'n', 'o', 'y'}
ring_number = {2: 'one', 1: 'two', 0: 'none'}  # {'o', 't', 'n'}
ring_type = {4: 'pedant', 0: 'evanescent', 2: 'large', 1: 'flaring', 3: 'none'}  # {'p', 'e', 'l', 'f', 'n'}
spore_print_color = {7: 'black', 3: 'brown', 2: 'purple', 1: 'chocolate', 8: 'white', 5: 'green', 0: 'orange',
                     4: 'yellow',
                     6: 'buff'}  # {'k', 'n', 'u', 'h', 'w', 'r', 'o', 'y', 'b'}
population = {2: 'scattered', 0: 'numerous', 4: 'abundant', 3: 'several', 5: 'solitary', 1: 'clustered'}
# {'s', 'n', 'a', 'v', 'y', 'c'}
habitat = {1: 'urban', 0: 'grasses', 4: 'meadows', 5: 'woods', 2: 'paths', 3: 'waste', 6: 'leaves'}
# {'u', 'g', 'm', 'd', 'p', 'w', 'l'}

mushroom_class = [1, 0]  # 1 : poisonous, 0 : edible

model = pickle.load(open('models/mushroom_classifier.model', 'rb'))
