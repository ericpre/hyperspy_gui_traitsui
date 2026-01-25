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
from traitsui.menu import OKButton, CancelButton

from hyperspy_gui_traitsui.utils import add_display_arg
from hyperspy_gui_traitsui.buttons import StoreButton


class SetMetadataItemsHandler(tu.Handler):

    def store(self, info):
        info.object.store()
        return True


@add_display_arg
def microscope_parameters_EDS_SEM(obj, **kwargs):
    view = tu.View(
        tu.Group('beam_energy',
                 'tilt_stage',
                 label='SEM', show_border=True),
        tu.Group('live_time', 'azimuth_angle',
                 'elevation_angle', 'energy_resolution_MnKa',
                 label='EDS', show_border=True),
        buttons=[StoreButton],
        handler=SetMetadataItemsHandler,
        title='SEM parameters definition wizard')
    return obj, {"view": view}


@add_display_arg
def microscope_parameters_EDS_TEM(obj, **kwargs):
    view = tu.View(
        tu.Group('beam_energy',
                 'tilt_stage',
                 'probe_area',
                 'beam_current',
                 label='TEM', show_border=True),
        tu.Group('real_time', 'live_time', 'azimuth_angle',
                 'elevation_angle', 'energy_resolution_MnKa',
                 label='EDS', show_border=True),
        buttons=[StoreButton],
        title='TEM parameters definition wizard')
    return obj, {"view": view}


@add_display_arg
def microscope_parameters_EELS(obj, **kwargs):
    view = tu.View(
        tu.Group('beam_energy',
                 'convergence_angle',
                 label='TEM', show_border=True),
        tu.Group('collection_angle',
                 label='EELS', show_border=True),
        buttons=[StoreButton],
        title='TEM parameters definition wizard')
    return obj, {"view": view}
