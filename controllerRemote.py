from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap
from remoteUI import Ui_MainWindow


class RemoteController:
    def __init__(self, remote_ui):
        self.remote_ui = remote_ui
        self.current_channel = 0
        self.current_volume = 0

        # Load images
        self.power_image = QPixmap("resources/power.png")
        self.mute_image = QPixmap("resources/mute.png")
        self.arrow_up_image = QPixmap("resources/Up Arrow.png")
        self.arrow_down_image = QPixmap("resources/Down Arrow.png")

        # Connect button signals to corresponding slot functions
        self.remote_ui.vUP.clicked.connect(self.volume_up)
        self.remote_ui.vDN.clicked.connect(self.volume_down)
        self.remote_ui.cUP.clicked.connect(self.channel_up)
        self.remote_ui.cDN.clicked.connect(self.channel_down)
        self.remote_ui.power.clicked.connect(self.power)
        self.remote_ui.mute.clicked.connect(self.mute)

    def volume_up(self):
        self.current_volume = min(self.current_volume + 1, 5)
        self.remote_ui.graphicsView.setPixmap(self.arrow_up_image)
        self.remote_ui.VUP.setText(f"Volume Up: {self.current_volume}")

    def volume_down(self):
        self.current_volume = max(self.current_volume - 1, 0)
        self.remote_ui.graphicsView.setPixmap(self.arrow_down_image)
        self.remote_ui.VDN.setText(f"Volume Down: {self.current_volume}")

    def channel_up(self):
        self.current_channel = (self.current_channel + 1) % 6
        self.remote_ui.graphicsView.setPixmap(self.arrow_up_image)
        self.remote_ui.labelChannelUp.setText(f"Channel Up: {self.current_channel}")

    def channel_down(self):
        self.current_channel = (self.current_channel - 1) % 6
        self.remote_ui.graphicsView.setPixmap(self.arrow_down_image)
        self.remote_ui.labelChanneDown.setText(f"Channel Down: {self.current_channel}")

    def power(self):
        self.remote_ui.graphicsView.setPixmap(self.power_image)

    def mute(self):
        self.remote_ui.graphicsView.setPixmap(self.mute_image)


if __name__ == "__main__":
    app = QApplication([])
    remote_ui = Ui_MainWindow()
    main_window = QMainWindow()
    remote_ui.setupUi(main_window)
    remote_controller = RemoteController(remote_ui)
    main_window.show()
    app.exec()
