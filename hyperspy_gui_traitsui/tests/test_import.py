# -*- coding: utf-8 -*-
# Copyright 2007-2026 The HyperSpy developers
#
# This file is part of HyperSpy.
#
# HyperSpy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# HyperSpy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with HyperSpy. If not, see <https://www.gnu.org/licenses/#GPL>.


import pytest

import hyperspy.api as hs
import hyperspy.ui_registry


def test_ui_registry():
    if "traitsui" in hyperspy.ui_registry.TOOLKIT_REGISTRY:
        assert "traitsui" in hyperspy.ui_registry.TOOLKIT_REGISTRY
    else:
        if "ipywidgets" in hyperspy.ui_registry.TOOLKIT_REGISTRY:
            with pytest.raises(ValueError):
                hs.preferences.gui(toolkit="traitsui")
        else:
            # As ipywidgets is not installed it should raise an import error
            with pytest.raises(ImportError):
                hs.preferences.gui(toolkit="traitsui")


def test_import_version():
    import hyperspy_gui_traitsui
    hyperspy_gui_traitsui.__version__


def test_import():
    import hyperspy_gui_traitsui
    for obj_name in hyperspy_gui_traitsui.__all__:
        getattr(hyperspy_gui_traitsui, obj_name)


def test_import_import_error():
    import hyperspy_gui_traitsui
    try:
        hyperspy_gui_traitsui.inexisting_module
    except AttributeError:
        pass


def test_dir():
    import hyperspy_gui_traitsui
    d = dir(hyperspy_gui_traitsui)
    assert d == [
        '__version__',
        'axes',
        'messages',
        'microscope_parameters',
        'model',
        'preferences',
        'tools',
        ]
