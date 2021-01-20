import sys
from PyQt5.QtWidgets import *
from aken import Algaken

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Algaken()
    window.show()
    sys.exit(app.exec_())

