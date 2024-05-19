import sys
from PySide6.QtWidgets import QApplication, QWidget
from ui_mainwindow import Ui_Form

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    with open("style.qss",encoding="utf-8") as f:
        app.setStyleSheet(f.read())
    widget.show()
    sys.exit(app.exec())
