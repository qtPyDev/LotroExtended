# lotro_extended_config.py
# written by qtPyDev

import os

GAMENAME = 'The Lord of the Rings Online'
COMPANY = 'StandingStoneGames'
DOCUMENTS = os.path.expanduser('~/OneDrive/Documents')
LOTRO_DATA_PATH = f'{DOCUMENTS}/{GAMENAME}'
DATA_DIR = f'{LOTRO_DATA_PATH}/LotroExtended'
DATA_PATH = f'{DATA_DIR}/Settings.ini'

DEFAULT_PLUGINS_PATH = f'{LOTRO_DATA_PATH}/Plugins/qtPyPlugins/LotroExtended'
DEFAULT_LOTRO_LOCATION = f'C:/Program Files (x86)/{COMPANY}/{GAMENAME}'
DEFAULT_SKIP_SETUP = 0
