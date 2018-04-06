from __future__ import absolute_import, division, print_function

import six
import matplotlib.pyplot as plt
import pytest


def test_stem_remove():
    ax = plt.gca()
    st = ax.stem([1, 2], [1, 2])
    st.remove()


def test_errorbar_remove():

    # Regression test for a bug that caused remove to fail when using
    # fmt='none'

    ax = plt.gca()

    eb = ax.errorbar([1], [1])
    eb.remove()

    eb = ax.errorbar([1], [1], xerr=1)
    eb.remove()

    eb = ax.errorbar([1], [1], yerr=2)
    eb.remove()

    eb = ax.errorbar([1], [1], xerr=[2], yerr=2)
    eb.remove()

    eb = ax.errorbar([1], [1], fmt='none')
    eb.remove()


def test_bar_container_iterator():
    ax = plt.gca()
    bars = ax.bar([2, 3, 4], [5, 7, 8])
    iter = bars.create_data_cursor_iterator([2, 3, 4], [5, 7, 8])

    assert iter.get_ind() == 0

    # test get_next method
    assert iter.get_next() == (3, 7)
    assert iter.get_ind() == 1
    assert iter.get_next() == (4, 8)
    assert iter.get_ind() == 2

    # get_next should stay at rightmost bar, if reached the end
    assert iter.get_next() == (4, 8)

    # test get_prev method
    assert iter.get_prev() == (3, 7)
    assert iter.get_ind() == 1

    assert iter.get_prev() == (2, 5)
    assert iter.get_ind() == 0

    # get prev should stay at leftmost bar, if reached the end
    assert iter.get_prev() == (2, 5)

    # test the set method
    iter.set_ind(1)
    assert iter.get_ind() == 1
