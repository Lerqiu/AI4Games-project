from tokenize import Number
import numpy as np

def clearAt(array:np.ndarray,filterValue:Number):
    arrayMax = np.max(array)
    if arrayMax > 1.0:
        array = array/arrayMax
    return np.where(array >= filterValue, array,0)

def joinOnMax(array1,array2):
    com = np.dstack((array1, array2))
    return np.max(com,axis=2)

def normalize(array):
    arrayMax = np.max(array)
    if arrayMax > 1.0:
        array = array/arrayMax
    arrayMin = np.min(array)
    if arrayMin < -1.0:
        array = array/abs(arrayMin)
    return array



#### improvement
import __init__
import numpy as np
from engine import Noise,Heatmap,CombineNoises,gradient,interact
from noises import *
from utilities import *
import random
from matplotlib import pyplot as plt
import matplotlib


def norm(matrix):
    matrix -= np.min(matrix)
    matrix /= np.max(matrix)
    return matrix

def cut(matrix, threshold = 0):
	matrix[matrix <= threshold] = 0
	return matrix


def getTexture(SEED=1234,RESOLUTION=500,fragments_n=2,fragment_mass=2.5,moisture=1,mass_prescaler=1.0):
    assert fragments_n > 1
    assert fragment_mass > 0
    assert moisture > 0

    random.seed(SEED)

    def worley_land_mass(points=2, cutoff=0, radius=1, seed=1234):
        return norm(cut(-worley(resolution=RESOLUTION, points=points, n=1, seed=seed) + 1, cutoff) ** radius)

    isLandBoundares = worley_land_mass(fragments_n,0,fragment_mass,SEED)

    terainNoises = CombineNoises(
    [1.0,0.4,0.1],
    [
        simplex(RESOLUTION,8,2,0.35,seed = SEED),
        simplex(500,8,2,0.5,seed=SEED+100),
        simplex(500,8,2,0.7,seed=SEED+200),
    ]
    )
    terainNoises = norm(terainNoises)

    terainHightMap = (terainNoises * np.abs(isLandBoundares))**0.5
    terainHightMap = norm(terainHightMap) * mass_prescaler

    terainMoisture = simplex(resolution=RESOLUTION,octaves=5,persistence=2,lacunarity=0.27,seed=SEED+300)
    terainMoisture = norm(terainMoisture) + 0.1
    terainMoisture *= moisture


    WATER_DARK = np.array([19,35,86])
    WATER_MEDIUM = np.array([35,51,106])
    WATER_BRIGHT = np.array([76,96,157])

    NATURE_DRY = np.array([107,106,87])
    NATURE_SMALL = np.array([96,106,84])
    NATURE_NORMAL = np.array([57,81,55])
    NATURE_BIG = np.array([40,66,40])


    STONES_NATURE_LITTLE = np.array([142,132,109])
    STONES_NATURE = np.array([94,99,73])
    STONES_NATURE_BIG = np.array([102,101,80])

    STONES = np.array([173,158,131])
    STONES_DESERT = np.array([177,145,110])

    DESERT_LITTLE = np.array([173,158,131])
    DESERT_MIDDLE = np.array([235,187,135])
    DESSERT = np.array([243,203,153])

    SNOW_LOW =  np.array([132,136,128])
    SNOW =  np.array([255,255,255])


    mapBioms = [
        [WATER_DARK for _ in range(10)],
        [WATER_MEDIUM for _ in range(10)],
        [WATER_BRIGHT for _ in range(10)],
        [NATURE_DRY,NATURE_DRY,NATURE_DRY,NATURE_DRY,NATURE_DRY,NATURE_SMALL,NATURE_SMALL,NATURE_SMALL,NATURE_SMALL,NATURE_SMALL],
        [DESERT_LITTLE,DESERT_LITTLE,NATURE_DRY,NATURE_DRY,NATURE_DRY,NATURE_SMALL,NATURE_SMALL,NATURE_NORMAL,NATURE_NORMAL,NATURE_NORMAL],
        [DESERT_MIDDLE,DESERT_LITTLE,DESERT_LITTLE,NATURE_DRY,NATURE_DRY,NATURE_SMALL,NATURE_NORMAL,NATURE_NORMAL,NATURE_BIG,NATURE_BIG],
        [DESSERT,DESERT_MIDDLE,DESERT_LITTLE,NATURE_DRY,NATURE_DRY,NATURE_SMALL,NATURE_NORMAL,NATURE_NORMAL,NATURE_BIG,NATURE_BIG],
        [DESSERT,DESERT_MIDDLE,DESERT_LITTLE,NATURE_DRY,NATURE_DRY,NATURE_SMALL,NATURE_NORMAL,NATURE_NORMAL,NATURE_BIG,NATURE_BIG],
        [DESSERT,DESERT_MIDDLE,DESERT_LITTLE,NATURE_DRY,NATURE_DRY,NATURE_SMALL,NATURE_NORMAL,NATURE_NORMAL,NATURE_BIG,NATURE_BIG],
        [DESSERT,DESERT_MIDDLE,DESERT_LITTLE,STONES_NATURE_LITTLE,NATURE_DRY,NATURE_SMALL,NATURE_NORMAL,NATURE_NORMAL,NATURE_BIG,NATURE_BIG],
        [DESSERT,DESERT_MIDDLE,DESERT_LITTLE,STONES_NATURE_LITTLE,NATURE_DRY,NATURE_SMALL,NATURE_NORMAL,NATURE_NORMAL,NATURE_BIG,NATURE_BIG],
        [DESSERT,DESERT_MIDDLE,DESERT_LITTLE,STONES_NATURE_LITTLE,NATURE_DRY,NATURE_SMALL,NATURE_NORMAL,NATURE_NORMAL,NATURE_BIG,NATURE_BIG],
        [DESSERT,DESERT_MIDDLE,DESERT_LITTLE,STONES_NATURE_LITTLE,NATURE_DRY,NATURE_SMALL,NATURE_NORMAL,NATURE_NORMAL,NATURE_BIG,NATURE_BIG],
        [STONES_DESERT,STONES,DESERT_LITTLE,STONES_NATURE_LITTLE,NATURE_DRY,STONES_NATURE,STONES_NATURE,STONES_NATURE,STONES_NATURE,STONES_NATURE_BIG],
        [STONES_DESERT,STONES_DESERT,STONES,STONES,STONES,STONES_NATURE_LITTLE,STONES_NATURE_LITTLE,STONES_NATURE_LITTLE,SNOW_LOW,SNOW_LOW],
        [SNOW_LOW,SNOW_LOW,SNOW_LOW,SNOW_LOW,SNOW_LOW,SNOW_LOW,SNOW_LOW,SNOW,SNOW,SNOW],
        [SNOW_LOW,SNOW_LOW,SNOW_LOW,SNOW,SNOW,SNOW,SNOW,SNOW,SNOW,SNOW],
        [SNOW,SNOW,SNOW,SNOW,SNOW,SNOW,SNOW,SNOW,SNOW,SNOW],
    ]
    mapBiomsLevels = len(mapBioms)
    mapBiomsDepth = len(mapBioms[0])

    heightMin = 0.4
    heightMax = 1.0
    heightStep = (heightMax - heightMin)/mapBiomsLevels
    #heightMax = np.max(terainHightMap)

    moistureMin = 0
    moistureMax = 1
    moisureStep = (moistureMax - moistureMin)/mapBiomsDepth

    map = np.zeros(shape=(RESOLUTION,RESOLUTION,3),dtype=np.ubyte)
    for y in range(RESOLUTION):
        for x in range(RESOLUTION):
            height = max(terainHightMap[y][x],heightMin)
            moisture = max(terainMoisture[y][x],moistureMin)

            level = int((height - heightMin)/heightStep)
            if level >= mapBiomsLevels:
                level = mapBiomsLevels -1
            depth =  int((moisture - moistureMin)/moisureStep)
            if depth >= mapBiomsDepth:
                depth = mapBiomsDepth-1
            map[y][x] = mapBioms[level][depth]
    
    return map

def showTexture(**kwargs):
    fig = plt.figure(figsize=(6,6),dpi=500)
    plt.imshow(getTexture(**kwargs))

def show(**kwargs):
    interact(lambda **fargs: showTexture(**fargs),**kwargs)