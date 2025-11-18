import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QIcon

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.setWindowTitle("Digital Clock")
        self.setWindowIcon(QIcon("clock0.jpg"))
        self.setGeometry(600, 400, 300, 100)

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet(
            "font: bold 150px;"
            "background-color: black;"
            "color: green;"
        )

        # Update every second
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)

        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)

        self.updateTime()

    def updateTime(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)

def main():
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
