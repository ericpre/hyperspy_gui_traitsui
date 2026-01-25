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


import traits.api as t
import traitsui.api as tu
from traitsui.menu import OKButton, CancelButton
from hyperspy_gui_traitsui.utils import add_display_arg



class Message(t.HasTraits):
    text = t.Str
    is_ok = t.Bool(False)

    def __init__(self, text):
        self.text = text


class MessageHandler(tu.Handler):

    def close(self, info, is_ok):
        # Removes the span selector from the plot
        if is_ok is True:
            info.object.is_ok = True
        else:
            info.object.is_ok = False
        return True


def information(text):
    message = Message(text)
    message.text = text
    view = tu.View(tu.Group(
        tu.Item('text',
                show_label=False,
                style='readonly',
                springy=True,
                width=300,
                padding=15),),
        kind='modal',
        buttons=[OKButton, CancelButton],
        handler=MessageHandler,
        title='Message')
    message.edit_traits(view=view)
    return message.is_ok


@add_display_arg
def simple_message(obj, **kwargs):
    view = tu.View(tu.Group(
        tu.Item('text',
                show_label=False,
                style='readonly',
                springy=True,
                width=300,
                padding=15),),
        kind='modal',
        buttons=[OKButton],
        title='Message')
    return obj, {"view": view}
