import sys
from PyQt5.QtWidgets import *
from aken import Algaken
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = Algaken()
    window.show()
    sys.exit(app.exec_())

