# lotro_extended.py
# written by qtPyDev

import os
import subprocess
import tkinter as tk
import configparser
import glob
import lotro_extended_config as config

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))



class LotroExtendedSettings:
    def __init__(self, lotro_location, plugins_location, skip_setup):
        self.lotro_location = lotro_location
        self.plugins_location = plugins_location
        self.skip_setup = skip_setup


def get_lotro_path() -> str:
    if os.path.exists(config.DATA_PATH):
        settings_conf = configparser.ConfigParser()
        settings_conf.read(config.DATA_PATH)

        return settings_conf.get('Settings', 'LotroLocation')
    else:
        return config.DEFAULT_LOTRO_LOCATION


def get_plugins_path() -> str:
    if os.path.exists(config.DATA_PATH):
        settings_conf = configparser.ConfigParser()
        settings_conf.read(config.DATA_PATH)

        return settings_conf.get('Settings', 'PluginsLocation')
    else:
        return config.DEFAULT_PLUGINS_PATH


def get_skip_setup() -> int:
    if os.path.exists(config.DATA_PATH):
        settings_conf = configparser.ConfigParser()
        settings_conf.read(config.DATA_PATH)

        return settings_conf.getint('Settings', 'SkipSetup')
    else:
        return config.DEFAULT_SKIP_SETUP


def set_lotroextended_settings(lotro_ext_settings):
    settings_conf = configparser.ConfigParser()

    settings_conf.add_section('Settings')

    settings_conf.set(
        'Settings',
        'LotroLocation',
        str(lotro_ext_settings.lotro_location)
    )
    settings_conf.set(
        'Settings',
        'PluginsLocation',
        str(lotro_ext_settings.plugins_location)
    )
    settings_conf.set(
        'Settings',
        'SkipSetup',
        str(lotro_ext_settings.skip_setup)
    )

    if not os.path.exists(config.DATA_DIR):
        os.makedirs(config.DATA_DIR)

    with open(config.DATA_PATH, 'w') as conf_file:
        settings_conf.write(conf_file)

    print(f'wrote data successfully to {config.DATA_PATH}')


def create_lotro_extended_win(settings):
    win = tk.Tk()
    win.title('Setup LOTRO Extended')
    win.geometry('400x160')
    win.resizable(False, False)

    lotro_label = tk.Label(win, text='LOTRO Game Path: ')
    lotro_entry = tk.Entry(win, width=60)
    lotro_entry.insert(0, settings.lotro_location)

    plugins_label = tk.Label(win, text='LOTRO Plugins Path: ')
    plugins_entry = tk.Entry(win, width=60)
    plugins_entry.insert(0, settings.plugins_location)

    skip_var = tk.IntVar()
    skip_var.set(settings.skip_setup)
    skip_check = tk.Checkbutton(
        win,
        text='Skip Setup in Future ?',
        variable=skip_var,
        onvalue='1',
        offvalue='0'
    )

    btn_continue = tk.Button(
        win,
        text='Continue',
        command=lambda: get_new_settings(
            settings,
            win,
            lotro_entry,
            plugins_entry,
            skip_var
        )
    )

    lotro_label.pack()
    lotro_entry.pack()
    plugins_label.pack()
    plugins_entry.pack()
    skip_check.pack()
    btn_continue.pack()

    win.mainloop()


def get_new_settings(settings, win, lotro_entry, plugins_entry, skip_var):
    lotro_location = lotro_entry.get()
    plugins_location = plugins_entry.get()
    skip_setup = skip_var.get()

    win.destroy()

    settings.lotro_location = lotro_location
    settings.plugins_location = plugins_location
    settings.skip_setup = skip_setup


def launch_lotroextended():
    lotro_location = get_lotro_path()
    plugins_location = get_plugins_path()
    skip_setup = get_skip_setup()

    settings = LotroExtendedSettings(
        lotro_location=lotro_location,
        plugins_location=plugins_location,
        skip_setup=skip_setup
    )

    print(settings.lotro_location)
    print(settings.skip_setup)

    lotro_launcher = subprocess.Popen(
        f'{settings.lotro_location}/LotroLauncher.exe',
        stdout=subprocess.PIPE,
        creationflags=0x08000000
    )

    if os.path.exists(settings.plugins_location):
        print('load plugins...')

        for file in glob.glob(f'{settings.plugins_location}/*.py'):
            print(f'loading.....{file}[100%]')
            subprocess.Popen(
                f'python "{file}"',
                stdout=subprocess.PIPE
            )

        print('plugins loaded !')

    print('finished...')


def main():
    lotro_location = get_lotro_path()
    plugins_location = get_plugins_path()
    skip_setup = get_skip_setup()

    settings = LotroExtendedSettings(
        lotro_location=lotro_location,
        plugins_location=plugins_location,
        skip_setup=skip_setup
    )

    if settings.skip_setup != 1:
        create_lotro_extended_win(settings)
        set_lotroextended_settings(settings)
        print('dont skip')
    else:
        set_lotroextended_settings(settings)
        print('skip')

    launch_lotroextended()


if __name__ == '__main__':
    main()
