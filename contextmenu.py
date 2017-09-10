# -*- coding: utf-8 -*-

###############################################################################
from logging import getLogger
from os import path as os_path
from sys import path as sys_path

from xbmcaddon import Addon
from xbmc import translatePath, sleep
from xbmcgui import Window

_addon = Addon(id='plugin.video.plexkodiconnect')
try:
    _addon_path = _addon.getAddonInfo('path').decode('utf-8')
except TypeError:
    _addon_path = _addon.getAddonInfo('path').decode()
try:
    _base_resource = translatePath(os_path.join(
        _addon_path,
        'resources',
        'lib')).decode('utf-8')
except TypeError:
    _base_resource = translatePath(os_path.join(
        _addon_path,
        'resources',
        'lib')).decode()
sys_path.append(_base_resource)

import loghandler
from pickler import unpickle_me, pickl_window

###############################################################################
loghandler.config()
log = getLogger("PLEX."+__name__)
###############################################################################

if __name__ == "__main__":
    win = Window(10000)
    while win.getProperty('plex_command'):
        sleep(20)
    win.setProperty('plex_command', 'CONTEXT_menu')
    while not pickl_window('plex_result'):
        sleep(50)
    result = unpickle_me()
    if result is None:
        log.error('Error encountered, aborting')
