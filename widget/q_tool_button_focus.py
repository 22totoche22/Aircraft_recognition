from PyQt5.QtWidgets import QToolButton


class QToolButtonFocus(QToolButton):
    """
    QToolButton with border depending on the focus
    """

    def __init__(self, parent=None):
        super().__init__(parent)
       # self.setFixedSize(25, 25)
        #self.setStyleSheet("""
       #         :!hover {border: 1px}
        #""")