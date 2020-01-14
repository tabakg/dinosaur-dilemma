"""

Copyright (C) 2020 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""


import numpy
import random


def dinosaurXdinosaur(dino1, dino2):
    """A dinosaur by dinosaur interaction. The first (dino1) is the entity
       that has come upon the second (dino2) in the game. More than one
       interaction are possible (e.g., mate then death, fight then mate, etc.).
    """
    outcomes = {}
    print("%s is interacting with %s" % (dino1, dino2))

    # Case 1: a male/female dinosaur can mate
    if dino1.gender != "hybrid" and dino2.gender != "hybrid":
        if dino1.gender != dino2.gender:
            if dino1.reproduce(entity=dino2):
                outcomes["reproduce"] = True

    # Case 2: Any two dinosaurs can fight, depending on the aggressiveness
    if dino1.is_aggressive and dino2.is_aggressive:

        # The probability of fighting is the mean of the hunger
        p_fight = (dino1.hunger + dino2.hunger) / 2
        they_fight = numpy.random.choice([True, False], p=[p_fight, 1 - p_fight])

        # If they fight, if the strength difference is big enough, the smaller one dies
        if they_fight:
            print("FIGHT: %s and %s!" % (dino1, dino2))
            if abs(dino1.strength - dino2.strength) > 0.4:
                outcomes["death"] = dino1 if dino1.strength > dino2.strength else dino2

    return outcomes


def dinosaurXavocado(dino, tree):
    """A dinosaur by avocado interaction, meaning that the dinosaur was moving
       and finds an avocado tree.
    """
    outcomes = {}
    print("%s is interacting with %s" % (dino, tree))

    # Case 1: The tree is mature with avocados, the dinosaur eats some
    if tree.is_mature and tree.avocados > 0:
        eaten = random.choice(range(tree.avocados))
        dino.hunger = dino.hunger + (0.1 * eaten)
        tree.avocados -= eaten
        print("EATEN %s %s avocados!" % (dino, eaten))

    return outcomes