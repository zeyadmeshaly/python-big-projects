import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QVBoxLayout, QHBoxLayout
)
from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtGui import QIcon

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()

        self.time = QTime(0, 0, 0, 0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)

        self.time_label = QLabel("00:00:00.000")
        self.time_label.setAlignment(Qt.AlignCenter)

        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")
        self.reset_button = QPushButton("Reset")

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stopwatch")
        self.setWindowIcon(QIcon("clock0.jpg"))
        self.setGeometry(600, 400, 350, 150)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.time_label)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.start_button)
        btn_layout.addWidget(self.stop_button)
        btn_layout.addWidget(self.reset_button)

        main_layout.addLayout(btn_layout)
        self.setLayout(main_layout)

        # Visible styling
        self.setStyleSheet("""
            QWidget {
                background-color: black;
            }
            QLabel {
                color: white;
                font-size: 36px;
                font-weight: bold;
            }
            QPushButton {
                background-color: white;
                color: black;
                font-size: 18px;
                padding: 8px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: lightgray;
            }
        """)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText("00:00:00.000")

    def update_time(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.time.toString("hh:mm:ss.zzz"))

def main():
    app = QApplication(sys.argv)
    s = Stopwatch()
    s.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
