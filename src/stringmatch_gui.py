import sys
from PyQt5.QtWidgets import QApplication, QWidget
import ui

def main():
    app = QApplication(sys.argv)
    widget = QWidget()
    UI = ui.Ui_Form()
    UI.setupUi(widget)
    widget.show()

    
    sys.exit(app.exec())

if __name__ == '__main__':
    main()