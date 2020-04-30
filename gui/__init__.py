# Copyright (c) 2018 SMHI, Swedish Meteorological and Hydrological Institute
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).

# @Johannes. Append paths
import sys
for add_path in ['C:/Utveckling/sharkpylib', 'C:/Utveckling/ctdpy', 'C:/Utveckling/algaware']:
    sys.path.append(add_path)

from gui.page_start import PageStart
from gui.page_about import PageAbout


from gui.widgets import InformationPopup
from gui.widgets import SaveWidget
from gui.widgets import SaveWidgetHTML
from gui.widgets import show_information
from gui.widgets import show_error
from gui.widgets import show_warning
from gui.widgets import show_internal_error

from gui import communicate
