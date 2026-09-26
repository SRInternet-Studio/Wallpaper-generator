from PySide6.QtWidgets import QDoubleSpinBox, QVBoxLayout
from qfluentwidgets import StrongBodyLabel


class Ui_Form:
    def setupUi(self, form):
        layout = QVBoxLayout(form)
        self.Title = StrongBodyLabel(form)
        self.NumberSelector = QDoubleSpinBox(form)
        self.NumberSelector.setDecimals(6)
        layout.addWidget(self.Title)
        layout.addWidget(self.NumberSelector)
