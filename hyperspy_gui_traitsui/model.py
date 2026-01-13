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


import traitsui.api as tu

from hyperspy_gui_traitsui.utils import add_display_arg
from hyperspy_gui_traitsui.buttons import OurFitButton, OurCloseButton
from hyperspy_gui_traitsui.tools import SpanSelectorInSignal1DHandler


class ComponentFitHandler(SpanSelectorInSignal1DHandler):

    def fit(self, info):
        """Handles the **Apply** button being clicked.

        """
        obj = info.object
        obj._fit_fired()
        return


@add_display_arg
def fit_component_traitsui(obj, **kwargs):
    fit_component_view = tu.View(
        tu.Item('only_current', show_label=True,),
        tu.Item('iterpath', show_label=True, enabled_when='only_current==False'),
        buttons=[OurFitButton, OurCloseButton],
        title='Fit single component',
        handler=ComponentFitHandler,
    )
    return obj, {"view": fit_component_view}
