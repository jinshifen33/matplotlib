from unittest.mock import Mock

import matplotlib.lines as lines
import matplotlib.pyplot as plt
from matplotlib.backend_tools import ToolDataCursor
from matplotlib.backend_managers import ToolManager

from matplotlib.testing.decorators import image_comparison

from numpy.testing import assert_allclose

import pytest


def get_ax():
    fig, ax = plt.subplots(1, 1)
    ax.plot([0, 200], [0, 200])
    ax.set_aspect(1.0)
    ax.figure.canvas.draw()
    return ax

def setUp():
    matplotlib.rcParams['toolbar'] = 'toolmanager'
    fig = plt.figure()
    manager = ToolManager(fig)

    fig.canvas.manager.toolmanager.add_tool('ToolDataCursor', ToolDataCursor)
    fig.canvas.manager.toolbar.add_tool('ToolDataCursor', 'data-cursor')


def do_event(tool, etype, button=1, xdata=0, ydata=0, key=None, step=1):
    """
     *name*
        the event name

    *canvas*
        the FigureCanvas instance generating the event

    *guiEvent*
        the GUI event that triggered the matplotlib event

    *x*
        x position - pixels from left of canvas

    *y*
        y position - pixels from bottom of canvas

    *inaxes*
        the :class:`~matplotlib.axes.Axes` instance if mouse is over axes

    *xdata*
        x coord of mouse in data coords

    *ydata*
        y coord of mouse in data coords

     *button*
        button pressed None, 1, 2, 3, 'up', 'down' (up and down are used
        for scroll events)

    *key*
        the key depressed when the mouse event triggered (see
        :class:`KeyEvent`)

    *step*
        number of scroll steps (positive for 'up', negative for 'down')
    """
    event = Mock()
    event.button = button
    ax = tool.ax
    event.x, event.y = ax.transData.transform([(xdata, ydata),
                                               (xdata, ydata)])[00]
    event.xdata, event.ydata = xdata, ydata
    event.inaxes = ax
    event.canvas = ax.figure.canvas
    event.key = key
    event.step = step
    event.guiEvent = None
    event.name = 'Custom'

    func = getattr(tool, etype)
    func(event)


