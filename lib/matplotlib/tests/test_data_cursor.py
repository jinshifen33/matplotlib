from unittest.mock import Mock

import matplotlib
import matplotlib.pyplot as plt
import time
from matplotlib.backend_tools import ToolDataCursor
from matplotlib.backend_managers import ToolManager


from numpy.testing import assert_allclose

import pytest

DELAY = 0.5

def get_tool(fig):
    return fig.canvas.manager.toolmanager.tools['data-cursor']

def add_line(ax, xs, ys):
    line, = ax.plot(xs, ys, '-', picker=5)
    ax.figure.canvas.draw()
    return line

def add_scatter(ax, xs, ys):
    scatter, = ax.plot(xs, ys, 'bs', picker=5)
    ax.figure.canvas.draw()
    return scatter

def add_bars(ax, xs, ys):
    bars = ax.bar(xs, ys, picker=5)
    ax.figure.canvas.draw()
    return bars

def set_up():
    # need to use a backend that has toolmanager
    plt.switch_backend('Qt5Agg')
    matplotlib.rcParams['toolbar'] = 'toolmanager'
    fig, ax = plt.subplots(1, 1)
    manager = ToolManager(fig)

    fig.canvas.manager.toolmanager.add_tool('data-cursor', ToolDataCursor)
    fig.canvas.manager.toolbar.add_tool('data-cursor', 'zoompan')
    return (fig, ax)


def do_event(tool, ax, etype, artist, index, button=1, xdata=0, ydata=0, key=None, step=1, delay=DELAY):
    """
    *tool*
        the tool instance handling the event

    *ax*
        the axes where the event was triggered

    *etype*
        event type - onpress or onpick

    *index*
        the index of the artist

    *artist*
        the artist on which the event was triggered

     *name*
        the event name

    *canvas*
        the FigureCanvas instance generating the event

    *guiEvent*
        the GUI event that triggered the matplotlib event

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
    """
    # Need to add delay due to time threshold for events
    time.sleep(delay)

    event = Mock()
    event.button = button
    event.artist = artist
    event.artist.axes = ax
    event.ind = index
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

def test_line():
    fig, ax=set_up()
    tool = get_tool(fig)
    line = add_line(ax, [1, 2, 3], [1, 2, 3])
    tool.enable()

    do_event(tool, ax, 'onpick', line, 0, xdata=1, ydata=1)
    assert tool.artist == line

    do_event(tool, ax, 'onpress', line, 1, xdata=2, ydata=2, key='d')
    assert len(tool.annotations) > 0
    annotation = tool.annotations[0].get_text().split(',')
    assert_allclose ((float(annotation[0].strip()), float(annotation[1].strip())), (1.05,1.05))

    do_event(tool, ax, 'onpress', line, 0, xdata=1, ydata=1, key='a')
    assert len(tool.annotations) > 0
    annotation = tool.annotations[0].get_text().split(',')
    assert_allclose ((float(annotation[0].strip()), float(annotation[1].strip())), (1,1))

    do_event(tool, ax, 'onpress', line, 0, xdata=1, ydata=1, key='a')
    assert len(tool.annotations) > 0
    annotation = tool.annotations[0].get_text().split(',')
    assert_allclose ((float(annotation[0].strip()), float(annotation[1].strip())), (1,1))

    tool.remove_annotations()
    assert len(tool.annotations) == 0


def test_scatter():
    fig, ax=set_up()
    tool = get_tool(fig)
    scatter = add_scatter(ax, [1, 2, 3], [1, 2, 3])
    tool.enable()
    do_event(tool, ax, 'onpick', scatter, 0, xdata=1, ydata=1)
    assert tool.artist == scatter

    do_event(tool, ax, 'onpress', scatter, 1, xdata=2, ydata=2, key='d')
    assert len(tool.annotations) > 0
    annotation = tool.annotations[0].get_text().split(',')
    assert_allclose ((float(annotation[0].strip()), float(annotation[1].strip())), (2,2))

    do_event(tool, ax, 'onpress', scatter, 0, xdata=1, ydata=1, key='a')
    assert len(tool.annotations) > 0
    annotation = tool.annotations[0].get_text().split(',')
    assert_allclose ((float(annotation[0].strip()), float(annotation[1].strip())), (1,1))

    do_event(tool, ax, 'onpress', scatter, 0, xdata=1, ydata=1, key='a')
    assert len(tool.annotations) > 0
    annotation = tool.annotations[0].get_text().split(',')
    assert_allclose ((float(annotation[0].strip()), float(annotation[1].strip())), (3,3))

    tool.remove_annotations()
    assert len(tool.annotations) == 0

def test_bar():
    fig, ax=set_up()
    tool = get_tool(fig)
    bars = add_bars(ax, [1, 2, 3], [1, 2, 3])
    tool.enable()
    do_event(tool, ax, 'onpick', bars[0], 0, xdata=1, ydata=1)
    assert tool.artist == bars

    do_event(tool, ax, 'onpress', bars[1], 1, xdata=2, ydata=2, key='d')
    assert len(tool.annotations) > 0
    annotation = tool.annotations[0].get_text().split(',')
    assert_allclose ((float(annotation[0].strip()), float(annotation[1].strip())), (2,2))

    do_event(tool, ax, 'onpress', bars[0], 0, xdata=1, ydata=1, key='a')
    assert len(tool.annotations) > 0
    annotation = tool.annotations[0].get_text().split(',')
    assert_allclose ((float(annotation[0].strip()), float(annotation[1].strip())), (1,1))

    do_event(tool, ax, 'onpress', bars[0], 0, xdata=1, ydata=1, key='a')
    assert len(tool.annotations) > 0
    annotation = tool.annotations[0].get_text().split(',')
    assert_allclose ((float(annotation[0].strip()), float(annotation[1].strip())), (1,1))

    tool.remove_annotations()
    assert len(tool.annotations) == 0
