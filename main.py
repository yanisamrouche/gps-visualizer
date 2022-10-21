#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Source pour le calcul:
https://geodesie.ign.fr/contenu/fichiers/Distance_longitude_latitude.pdf
"""

from math import sin, cos, acos, pi
import folium


#############################################################################
def dms2dd(d, m, s):
    """Convertit un angle "degrés minutes secondes" en "degrés décimaux"
    """
    return d + m / 60 + s / 3600


#############################################################################
def dd2dms(dd):
    """Convertit un angle "degrés décimaux" en "degrés minutes secondes"
    """
    d = int(dd)
    x = (dd - d) * 60
    m = int(x)
    s = (x - m) * 60
    return d, m, s


#############################################################################
def deg2rad(dd):
    """Convertit un angle "degrés décimaux" en "radians"
    """
    return dd / 180 * pi


#############################################################################
def rad2deg(rd):
    """Convertit un angle "radians" en "degrés décimaux"
    """
    return rd / pi * 180


#############################################################################
def distanceGPS(latA, longA, latB, longB):
    """Retourne la distance en mètres entre les 2 points A et B connus grâce à
       leurs coordonnées GPS (en radians).
    """
    # Rayon de la terre en mètres (sphère IAG-GRS80)
    RT = 6378137
    # angle en radians entre les 2 points
    S = acos(sin(latA) * sin(latB) + cos(latA) * cos(latB) * cos(abs(longB - longA)))
    # distance entre les 2 points, comptée sur un arc de grand cercle
    return S * RT


#############################################################################
if __name__ == "__main__":
    latA = deg2rad(43.91955602015508)  # Nord
    longA = deg2rad(4.57328580852187)  # Est

    latB = deg2rad(43.91929689802079)  # Nord
    longB = deg2rad(4.573327853256498)  # Est

    dist = distanceGPS(latA, longA, latB, longB)
    print(int(dist))
    coords1 = (43.91929689802079, 4.573327853256498)
    map = folium.Map(location=coords1, tiles='OpenStreetMap', zoom_start=15)
    coords2= [43.91929689802079, 4.573327853256498]
    folium.Marker(location=coords2, tiles='OpenStreetMap', zoom_start=15).add_to(map)
    folium.Rectangle([(43.91955602015508,4.57328580852187),(45,5)]).add_to(map)
    map.save(outfile='map.html')
