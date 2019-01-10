# -*- coding: utf-8 -*-

from platform import system as os
import locale
import ctypes
from pathlib import Path


# -------------------------------------------
def get_errors():
    """Returns the help_msg based on language"""
    if("es" == get_lang()):
        help_msg = """
                        __  __                           ______ __     ____
                       / / / /____   _____ ____ _ _____ / ____// /    /  _/
                      / /_/ // __ \ / ___// __ `// ___// /    / /     / /
                     / __  // /_/ // /   / /_/ /(__  )/ /___ / /___ _/ /
                    /_/ /_/ \____//_/    \__,_//____/ \____//_____//___/

                    Uso:
                    horasCLI -h | --help
                        'Muestra esta ayuda'
                    horasCLI -s | --show
                        'Abre el registro en Chrome si esta instalado o en la linea de comandos'
                    horasCLI -r | --reset
                        'Resetea el registro'
                    horasCLI -n | --new <nombre del proyecto> <horas>
                        'Crea una fila en el registro con el dia de hoy'
                    horasCLI -n | --new <nombre del proyecto> <horas> <fecha (dd-mm)>
                        'Crea una fila en el registro con el dia que le pasemos'
                    horasCLI -d | --delete
                        'Elimina la ultima fila del registro'
                    horasCLI -f | --file
                        '*SOLO EN WINDOWS* Abre el directorio del archivo en el explorador'
                    horasCLI -c | --code
                        '*SOLO EN WINDOWS* Abre el archivo en VSCode (Necesitas tenerlo instalado)'
                    """
    else:
        help_msg = """
                        __  __                           ______ __     ____
                       / / / /____   _____ ____ _ _____ / ____// /    /  _/
                      / /_/ // __ \ / ___// __ `// ___// /    / /     / /
                     / __  // /_/ // /   / /_/ /(__  )/ /___ / /___ _/ /
                    /_/ /_/ \____//_/    \__,_//____/ \____//_____//___/

                    Usage:
                    horasCLI -h | --help
                        'Shows this help'
                    horasCLI -s | --show
                        'Opens the schedule in Chrome if exists or as command line'
                    horasCLI -r | --reset
                        'Resets the schedule'
                    horasCLI -n | --new <project name> <hours>
                        'Adds row to the schedule with today date'
                    horasCLI -n | --new <project name> <hours> <date (dd-mm)>
                        'Adds row to the schedule with the given date'
                    horasCLI -d | --delete
                        'Deletes the last row added'
                    horasCLI -m | --manual
                        '*ONLY IN WINDOWS* Opens the folder where the file'
                    horasCLI -c | --code
                        '*ONLY IN WINDOWS* Opens the file in VSCode (You need to have it installed)'
                    """
    return help_msg


# -------------------------------------------
def get_lang():
    """Get the OS and returns the language"""
    if os() == 'Windows':
        # Windows
        lang = locale.windows_locale[ctypes.windll.kernel32.GetUserDefaultUILanguage()]
    else:
        # Linux || MacOS
        lang = locale.getlocale(locale.LC_MESSAGES)[0]
    return lang
