import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ipywidgets import interact
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib.cm import register_cmap


def gradient(colors=[], ranges=[], name=""):
    return LinearSegmentedColormap.from_list(name, list(zip(ranges, colors)))


def colors(colors=[], name=""):
    return ListedColormap(colors, name=name)


islands = gradient(
    name="islands",
    colors=["#2B3A67", "#0E79B2", "#8F754F", "#41521F", "#256D1B"],
    ranges=[0.0, 0.45, 0.5, 0.6, 1.0],
)

mountains = gradient(
    name="mountains",
    colors=[
        "#2B3A67",
        "#0E79B2",
        "#8F754F",
        "#41521F",
        "#256D1B",
        "#E1C16E",
        "#CD7F32",
        "#EADDCA",
    ],
    ranges=[0.0, 0.35, 0.40, 0.55, 0.65, 0.75, 0.85, 1.0],
)

register_cmap(name="mountains",cmap=mountains)



def Heatmap(*matrix, scale=1.0, cbar=False, cmap=islands, **kwargs):
    "Create one or multiple heatmaps and arrange them into a row"

    # make grid
    shape = np.shape(matrix)[0]
    fig, axs = plt.subplots(ncols=shape)
    fig.dpi = 100 * scale
    if shape == 1:
        axs = [axs]

    # render heatmaps
    for i, ax in enumerate(axs):
        ax.axis("scaled")
        sns.heatmap(
            matrix[i],
            ax=ax,
            cmap=cmap,
            yticklabels=False,
            xticklabels=False,
            cbar=cbar,
            **kwargs
        )


def Noise(noise_function, **kwargs):
    """Create interactive heatmap.
    Every matched keyword argument is passed to the noise function.
    Arguments that failed to match are passed to the heatmap instead.
    """

    tokens = noise_function.__code__.co_varnames
    fargs = {k: v for k, v in kwargs.items() if k in tokens}
    hargs = dict(set(kwargs.items()) - set(fargs.items()))
    interact(lambda **fargs: Heatmap(noise_function(**fargs), **hargs), **fargs)


def WeightSum(weights, noises):
    """Weight sum of noises"""
    assert len(weights) == len(noises)

    newNoise = np.zeros(noises[0].shape)
    for weight, noise in zip(weights, noises):
        newNoise += weight * noise
    return newNoise
