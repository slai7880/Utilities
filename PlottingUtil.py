import numpy as np
import sys, os
from random import shuffle
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

def makeMatrixPlot(M, title,\
                xTickLabels = None, yTickLabels = None,\
                xLabel = "", yLabel = "",\
                threshold = "auto", cmap = plt.cm.Blues, vmin = None, vmax = None,\
                figsize = (8, 6), dpi = 100,\
                integer = True):
    """
    Creates a 2D plot of a numpy matrix.
    Parameters
    ----------
    M : numpy matrix
    title : string
        The title of the plot.
    xTickLabels, yTickLabels : string
        The tick labels on the axis'.
    xLabel, yLabel : string
        The labels of the axis'.
    threshold : int or float
        The threshold where the text color should flip so that the text
        can be seen.
    cmap : matplotlib.pyplot color map object
    integer : boolean
        Indicates whether or not the values in M should be displayed as integers.
    Returns
    -------
    fig, ax
        The objects of matplotlib.pyplot figure.
    """
    if xTickLabels is None:
        xTickLabels = [i for i in range(M.shape[1])]
    if yTickLabels is None:
        yTickLabels = [i for i in range(M.shape[0])]
    fig, ax = plt.subplots(figsize = figsize, dpi = dpi)
    im = ax.imshow(M, interpolation = "nearest", cmap = cmap, vmin = vmin, vmax = vmax)
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size = "5%", pad = 0.05)
    ax.figure.colorbar(im, cax = cax)
    ax.set(xticks = np.arange(M.shape[1]), yticks = np.arange(M.shape[0]), xticklabels = xTickLabels, yticklabels = yTickLabels,\
            title = title, xlabel = xLabel, ylabel = yLabel)
    plt.setp(ax.get_xticklabels(), rotation = 45, ha = "right", rotation_mode = "anchor")
    if threshold == "auto":
        threshold = M.max() / 2
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            color = "white"
            if M[i, j] <= threshold:
                color = "black"
            text = str(M[i, j])
            if integer:
                text = str(int(M[i, j]))
            ax.text(j, i, text, ha = "center", va = "center", color = color)
    fig.tight_layout()
    return fig, ax

def makeHistogramPlot(data, title,\
                    xTickLabels = None, yTickLabels = None,\
                    xLabel = "", yLabel = "",figsize = (8, 6), dpi = 100,\
                    integer = True):
    """
    Creates a histogram plot.
    Parameters
    ----------
    data : array-like
        This should be a histogram array, not the original data array.
    title : string
        The title of the plot.
    xTickLabels, yTickLabels : string
        The tick labels on the axis'.
    xLabel, yLabel : string
        The labels of the axis'.
    threshold : int or float
        The threshold where the text color should flip so that the text
        can be seen.
    cmap : matplotlib.pyplot color map object
    integer : boolean
        Indicates whether or not the values in data should be displayed as integers.
    Returns
    -------
    fig, ax
        The objects of matplotlib.pyplot figure.
    """
    if xTickLabels is None:
        xTickLabels = [i for i in range(len(data))]
    if yTickLabels is None:
        yTickLabels = [i for i in range(0, int(np.ceil(max(data))), 100)]
    xticks = np.arange(len(data))
    yticks = np.arange(0, int(np.ceil(max(data))), 100)
    fig, ax = plt.subplots(figsize = figsize, dpi = dpi)
    ax.bar(xticks, data)
    for i in range(len(data)):
        text = str(data[i])
        if integer:
            text = str(int(data[i]))
        ax.text(xticks[i], data[i], text, ha = "center", va = "bottom")
    ax.set(xticks = xticks, yticks = yticks, xticklabels = xTickLabels, yticklabels = yTickLabels,\
            title = title, xlabel = xLabel, ylabel = yLabel)
    fig.tight_layout()
    return fig, ax


def makeBarPlotsOld(Ys, dates, frameOrder, fig, ax, title, stacked = True, textOnBar = True, filename = None):
    normalized = "Normalized" in title
    
    ax.tick_params(axis = 'both', which = 'major', labelsize = 32)
    X = np.array([i for i in range(len(dates))])
    colors = ["b", "g", "r", "c", "y", "m", "k", "#6D4EA2", "#E98400","#9B0055"]
    bottomP = np.array([0.0] * Ys.shape[1])
    bottomN = np.array([0.0] * Ys.shape[1])
    YsP = Ys.copy()
    YsN = Ys.copy()
    YsP[YsP < 0] = 0
    YsN[YsN > 0] = 0
    
    if stacked:
        for i in range(N_FRAMES):
            if i > 0:
                bottomP += YsP[frameOrder[i - 1], :]
                bottomN += YsN[frameOrder[i - 1], :]
            ax.bar(X, YsP[frameOrder[i], :], color = colors[frameOrder[i]], bottom = bottomP, label = FRAME_NAMES[frameOrder[i]])
            # ax.bar(X, YsN[tuples[i][1], :], color = colors[i], bottom = bottomN)
        bottomP += YsP[frameOrder[-1], :]
    
        
        if textOnBar:
            for i in range(Ys.shape[1]):
                ax.text(X[i] - 0.25, bottomP[i] + 0.02 * bottomP[i], str(int(bottomP[i])), fontsize = 14, fontweight = "bold")
    else:
        w = [-0.4, -0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3, 0.4]
        for i in range(N_FRAMES):
            ax.bar(X + w[i], YsP[frameOrder[i], :], color = colors[frameOrder[i]], width = 0.05, label = FRAME_NAMES[frameOrder[i]])
    name2index = {FRAME_NAMES[i] : i for i in range(N_FRAMES)}
    handles, labels = ax.get_legend_handles_labels()
    newHandles, newLabels = [], FRAME_NAMES[:]
    for i in range(N_FRAMES):
        newHandles.append(handles[frameOrder.index(name2index[FRAME_NAMES[i]])])
    if not stacked and not normalized:
        ax.plot(X, YsP.sum(axis = 0), color = colors[N_FRAMES], marker = "o", label = "Total")
        handles, labels = ax.get_legend_handles_labels()
        newHandles.append(handles[0])
        newLabels.append("Total")
    if not normalized:
        ax.legend(newHandles, newLabels, fontsize = 24)
    ax.set_title(title, fontsize = 34, pad = 20, fontweight = "bold")
    # ax.set_xlabel("Time")
    # ax.set_ylabel("Count")
    ax.set_xticks(X)
    ax.set_xticklabels(dates)
    return fig, ax
    
def makeStackedBarPlot(data, colors, title, labels = None,\
                    xTickLabels = None, yTickLabels = None,\
                    xLabel = "", yLabel = "", figsize = (8, 6), dpi = 100,\
                    text = True):
    """
    Creates a stacked bar plot.
    Parameters
    ----------
    data : numpy matrix
        Each column will be associated with a bar in the figure.
        data[0, :] is the bottom layer for each bar. Also note
        that the values inside are assumed to be non-negative.
    colors : array-like
        The colors for the classes in data.
    title : string
        The title of the plot.
    xTickLabels, yTickLabels : string
        The tick labels on the axis'.
    xLabel, yLabel : string
        The labels of the axis'.
    text : boolean
        Indicates whether or not the sum of each column should be displayed.
    Returns
    -------
    fig, ax
        The objects of matplotlib.pyplot figure.
    """
    assert data.shape[0] == len(colors)
    if labels is None:
        labels = ["Class " + str(i) for i in range(data.shape[0])]
    if xTickLabels is None:
        xTickLabels = [i for i in range(data.shape[1])]
    
    fig, ax = plt.subplots(figsize = figsize, dpi = dpi)
    ax.tick_params(axis = 'both', which = 'major', labelsize = 12)
    X = np.array([i for i in range(data.shape[1])])

    bottom = np.array([0.0] * data.shape[1])
    for i in range(data.shape[0]):
        if i > 0:
            bottom += data[i - 1, :]
        ax.bar(X, data[i, :], color = colors[i], bottom = bottom, label = labels[i])
    bottom += data[-1, :]
    if text:
        for i in range(data.shape[1]):
            ax.text(X[i], bottom[i], str(np.round(bottom[i], 4)), ha = "center", va = "bottom", fontsize = 10)
    
    # If there are multiple figures and the legends need to be fixed across them,
    # the handles and figLabels of the figure must be set manually starting with the
    # following code. Note that this is incomplete, please refer to the official
    # website for instruction.
    figHandles, figLabels = ax.get_legend_handles_labels()
    newFigHandles = figHandles
    newFigLabels = figLabels
    
    ax.legend(newFigHandles, newFigLabels, fontsize = 12)
    ax.set_title(title, fontsize = 12, pad = 20, fontweight = "bold")
    ax.set_xticks(X)
    ax.set_xticklabels(xTickLabels)
    return fig, ax
    
def makeMultibarPlot(data, colors, title, labels = None,\
                    xTickLabels = None, yTickLabels = None,\
                    xLabel = "", yLabel = "", width = 0.05, gapMultiplier = 1, figsize = (8, 6), dpi = 100,\
                    text = True):
    """
    Creates a multi-bar plot.
    Parameters
    ----------
    data : numpy matrix
        Each column will be associated with a bar in the figure.
        data[0, :] is the bottom layer for each bar. Also note
        that the values inside are assumed to be non-negative.
    colors : array-like
        The colors for the classes in data.
    title : string
        The title of the plot.
    xTickLabels, yTickLabels : string
        The tick labels on the axis'.
    xLabel, yLabel : string
        The labels of the axis'.
    text : boolean
        Indicates whether or not the sum of each column should be displayed.
    Returns
    -------
    fig, ax
        The objects of matplotlib.pyplot figure.
    """
    assert data.shape[0] == len(colors)
    if labels is None and data.shape[0] > 1:
        labels = ["Class " + str(i) for i in range(data.shape[0])]
    if xTickLabels is None:
        xTickLabels = [i for i in range(data.shape[1])]
    
    fig, ax = plt.subplots(figsize = figsize, dpi = dpi)
    ax.tick_params(axis = 'both', which = 'major', labelsize = 12)
    X = np.array([i for i in range(data.shape[1])])

    w = []
    gap = width * gapMultiplier
    multiplier = -1
    if data.shape[0] % 2 == 0:
        w = [-gap / 2, gap / 2]
        start = 2
    else:
        w = [0]
        start = 1
    previous = w[0]
    for i in range(start, data.shape[0]):
        w.append(previous + gap * multiplier)
        previous = w[-2]
        multiplier *= -1
    w.sort()
    for i in range(data.shape[0]):
        if not labels is None:
            ax.bar(X + w[i], np.squeeze(np.array(data[i, :])), color = colors[i], width = width, label = labels[i])
        else:
            ax.bar(X + w[i], np.squeeze(np.array(data[i, :])), color = colors[i], width = width)
        if text:
            Xs = X + w[i]
            for j in range(len(Xs)):
                ax.text(Xs[j], data[i, j], str(data[i, j]), ha = "center", va = "bottom", fontsize = 10)
    # If there are multiple figures and the legends need to be fixed across them,
    # the handles and figLabels of the figure must be set manually starting with the
    # following code. Note that this is incomplete, please refer to the official
    # website for instruction.
    figHandles, figLabels = ax.get_legend_handles_labels()
    newFigHandles = figHandles
    newFigLabels = figLabels
    
    if not labels is None:
        ax.legend(newFigHandles, newFigLabels, fontsize = 12)
    ax.set_title(title, fontsize = 12, pad = 20, fontweight = "bold")
    ax.set_xticks(X)
    ax.set_xticklabels(xTickLabels)
    return fig, ax
    
