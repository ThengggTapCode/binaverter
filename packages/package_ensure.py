import subprocess
import sys
import logging
from .common import *

def package_ensure(package_name):
    clear_terminal()
    logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
    
    try:
        __import__(package_name)
    except ImportError:
        logging.warning(f"Gói '{package_name}' chưa được cài đặt, tiến hành cài đặt...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        logging.info(f"Gói '{package_name} đã được cài đặt thành công'")
        clear_terminal()