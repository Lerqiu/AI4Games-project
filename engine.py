import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ipywidgets import interact


def Heatmap(*matrix, scale=1.0, cbar = False, cmap="nipy_spectral", **kwargs):
    "Create one or multiple heatmaps and arrange them into a row"
    shape = np.shape(matrix)
    #assert(len(shape) == 3)

    # make grid
    fig, axs = plt.subplots(ncols=shape[0])
    fig.dpi = 100 * scale
    if np.shape(matrix)[0] == 1:
        axs = [axs]

    # render heatmaps
    for i, ax in enumerate(axs):
        ax.axis('scaled')
        sns.heatmap(matrix[i], ax=ax, cmap=cmap, yticklabels=False,
                    xticklabels=False, cbar=cbar, **kwargs)


def Noise(noise_function, scale=1.0, **kwargs):
    interact(lambda **kwargs: Heatmap(noise_function(**kwargs)), **kwargs)
