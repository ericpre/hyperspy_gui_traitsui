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

OurOKButton = tu.Action(name="OK",
                        action="OK",)

OurApplyButton = tu.Action(name="Apply",
                           action="apply")

OurResetButton = tu.Action(name="Reset",
                           action="reset")

OurCloseButton = tu.Action(name="Close",
                           action="close_directly")

OurFindButton = tu.Action(name="Find next",
                          action="find",)

OurPreviousButton = tu.Action(name="Find previous",
                              action="back",)

OurFitButton = tu.Action(name="Fit",
                         action="fit")

StoreButton = tu.Action(name="Store",
                        action="store")

SaveButton = tu.Action(name="Save",
                       action="save")

HelpButton = tu.Action(name="Help",
                       action="show_help")
