#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici

import numpy


# TODO: Définissez vos fonction ici

# 1. Volume et masse d'un ellipsoïde

def volume_masse(a, b, c, masse_volumique):
    
    # Calcul du volume
    volume = (4/3) * numpy.pi * a * b * c

    # Calcul de la masse

    masse = masse_volumique * volume

    return (volume, masse)

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass
