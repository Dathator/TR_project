from imports import *
from main_window import MainWindow


if __name__ == "__main__":
    app = QApplication(argv)

    window = MainWindow()
    window.show_w_login()

    exit(app.exec())