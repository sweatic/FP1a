from PyQt6.QtWidgets import QApplication, QMainWindow
from remote import Ui_MainWindow

if __name__ == "__main__":
    app = QApplication([])
    main_window = QMainWindow()
    remote_ui = Ui_MainWindow()
    remote_ui.setupUi(main_window)
    main_window.show()
    app.exec()
