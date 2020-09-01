from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon, QResizeEvent
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QStatusBar, QMenuBar, \
    QActionGroup, QTabWidget, QAction, QToolButton, QFrame, QToolBar, QDesktopWidget, QSizePolicy
from PyQt5.QtCore import Qt

from widget.q_tool_button_focus import QToolButtonFocus


class MainWindow(QMainWindow):
    closeSignal = pyqtSignal()
    resizeSignal = pyqtSignal()

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        desk = QDesktopWidget()
        screen = desk.screenGeometry()
        x = screen.width()
        y = screen.height()

        """ Main window"""

        """general"""
        self.setObjectName("MainWindow")
        self.setEnabled(True)
        self.resize(int(0.4 * x), int(0.75 * y))
        self.setWindowTitle("Aircraft Recognition")
        self.show()

        self.central_widget = QWidget(self)
        self.central_widget.setObjectName("central_widget")

        self.group = QVBoxLayout()  # this layout is gonna be our group container
        self.central_widget.setLayout(self.group)
        self.setCentralWidget(self.central_widget)


        """ Chart"""
        # creates the main layout for the chart
        self.layout_picture = QVBoxLayout()
        # widget which contains the chart , necessary to save the chart as png
        self.picture = QGroupBox()
        self.picture.setLayout(self.layout_picture)

        """Controls"""
        self.button_next = QToolButtonFocus()
        self.button_next.setText("Next")
        self.button_validate = QToolButtonFocus()
        self.button_validate.setText("Validate")
        self.layout_controls = QHBoxLayout()
        self.layout_controls.addWidget(self.button_next)
        self.layout_controls.addWidget(self.button_validate)
        self.controls = QGroupBox()
        self.controls.setLayout(self.layout_controls)

        """ Status Bar """
        # creates a qstatusbar to inform the users
        self.group_message = QGroupBox("Message :")
        self.group_message.setFixedHeight(70)
        self.layout_status = QHBoxLayout()
        self.group_message.setLayout(self.layout_status)
        self.layout_status.setAlignment(Qt.AlignBottom)
        self.status = QStatusBar()
        self.status.setStyleSheet("""    
                             .QStatusBar {
                                 border: 1px solid white;
                                 background-color: white;
                                 color : red;
                                 }
                             """)
        self.status.setMaximumWidth(500)
        self.layout_status.addWidget(self.status)
        self.layout_status.addWidget(self.button_validate)

        self.layout_status.addWidget(self.button_next)


        """ add to the main group everything """
        # curve and axis config
        self.layout_config = QVBoxLayout()

        # chart and button save
        self.layout_picture = QVBoxLayout()
        self.layout_picture.addWidget(self.picture)
        self.layout_picture.addWidget(self.group_message)

        self.group.addLayout(self.layout_picture)

    def closeEvent(self, event):
        self.closeSignal.emit()  # emit a close signal
        super().closeEvent(event)

    def resizeEvent(self, a0: QResizeEvent) -> None:
        # super().resizeEvent(a0)
        self.resizeSignal.emit()
