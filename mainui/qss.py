if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)

    with open("style.qss",encoding="utf-8") as f:
        app.setStyleSheet(f.read())

    Form.show()
    sys.exit(app.exec())