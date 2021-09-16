import pickle

columns = ['cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor',
           'gill-attachment', 'gill-spacing', 'gill-size', 'gill-color',
           'stalk-shape', 'stalk-root', 'stalk-surface-above-ring',
           'stalk-surface-below-ring', 'stalk-color-above-ring',
           'stalk-color-below-ring', 'veil-color', 'ring-number',
           'ring-type', 'spore-print-color', 'population', 'habitat']

cap_shape = {0: 'convex', 5: 'bell', 2: 'sunken', 3: 'flat', 4: 'knobbed',
             1: 'conical'}  # ['x', 'b', 's', 'f', 'k', 'c']

cap_surface = [2, 0, 3, 1]  # ['s', 'y', 'f', 'g']
cap_color = [8, 3, 4, 2, 9, 7, 0, 1, 6, 5]  # ['n', 'y', 'w', 'g', 'e', 'p', 'b', 'u', 'c', 'r']
bruises = [0, 1]  # ['t', 'f']
odor = [5, 8, 2, 7, 3, 1, 0, 6, 4]  # ['p', 'a', 'l', 'n', 'f', 'c', 'y', 's', 'm']
gill_attachment = [1, 0]  # ['f', 'a']
gill_spacing = [1, 0]  # ['c', 'w']
gill_size = [0, 1]  # ['n', 'b']
gill_color = [2, 4, 9, 0, 7, 5, 10, 3, 11, 1, 8, 6]  # ['k', 'n', 'g', 'p', 'w', 'h', 'u', 'e', 'b', 'r', 'y', 'o']
stalk_shape = [0, 1]  # ['e', 't']
stalk_root = [0, 3, 1, 2, 4]  # ['e', 'c', 'b', 'r']
stalk_surface_above_ring = [2, 0, 1, 3]  # ['s', 'f', 'k', 'y']
stalk_surface_below_ring = [1, 0, 2, 3]  # ['s', 'f', 'y', 'k']
stalk_color_above_ring = [7, 6, 4, 3, 0, 5, 1, 2, 8]  # ['w', 'g', 'p', 'n', 'b', 'e', 'o', 'c', 'y']
stalk_color_below_ring = [7, 3, 6, 0, 4, 5, 1, 8, 2]  # ['w', 'p', 'g', 'b', 'n', 'e', 'y', 'o', 'c']
veil_color = [2, 0, 1, 3]  # ['w', 'n', 'o', 'y']
ring_number = [2, 1, 0]  # ['o', 't', 'n']
ring_type = [4, 0, 2, 1, 3]  # ['p', 'e', 'l', 'f', 'n']
spore_print_color = [7, 3, 2, 1, 8, 5, 0, 4, 6]  # ['k', 'n', 'u', 'h', 'w', 'r', 'o', 'y', 'b']
population = [2, 0, 4, 3, 5, 1]  # ['s', 'n', 'a', 'v', 'y', 'c']
habitat = [1, 0, 4, 5, 2, 3, 6]  # ['u', 'g', 'm', 'd', 'p', 'w', 'l']

mushroom_class = [1, 0]  # 1 : poisonous, 0 : edible

model = pickle.load(open('models/mushroom_classifier.model', 'rb'))
