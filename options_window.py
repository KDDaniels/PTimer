
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFrame, QHBoxLayout, QLabel, QSizePolicy, QSpinBox, QDialogButtonBox
from PyQt5.QtCore import Qt, pyqtSignal, QSize

class OptionsWindow(QWidget):

    opt_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setup_window()

    def setup_window(self):
        self.resize(184, 190)
        self.setWindowTitle("Settings")

        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        self.generate_ui_elements()

    def generate_ui_elements(self):
        self.settings_window_layout = QVBoxLayout(self)

        self.settings_window_layout.addWidget(self.generate_input_widget())
        self.settings_window_layout.addWidget(self.generate_btns())
    def generate_input_widget(self):
        self.input_frame = QFrame(self)
        self.input_frame.setFrameShape(QFrame.StyledPanel)
        self.input_frame.setFrameShadow(QFrame.Sunken)
        self.input_frame_layout = QVBoxLayout(self.input_frame)


        # ==== Work time widget ====
        self.work_opt_widget = QWidget(self.input_frame)
        self.work_opt_widget_layout = QHBoxLayout(self.work_opt_widget)
        self.work_opt_widget_layout.setSpacing(0)
        self.work_opt_widget_layout.setContentsMargins(4, 4, 4, 0)

        self.work_opt_label = QLabel(self.work_opt_widget)
        
        sp = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sp.setHorizontalStretch(1)
        sp.setHeightForWidth(self.work_opt_label.sizePolicy().hasHeightForWidth())

        self.work_opt_label.setSizePolicy(sp)
        self.work_opt_label.setText("Work time: ")

        self.work_opt_input = QSpinBox(self.work_opt_widget)
        self.work_opt_input.setMinimumSize(QSize(59, 0))
        self.work_opt_input.setValue(25)

        self.work_opt_widget_layout.addWidget(self.work_opt_label)
        self.work_opt_widget_layout.addWidget(self.work_opt_input)


        # ==== Short break widget ====
        self.sbreak_opt_widget = QWidget(self.input_frame)
        self.sbreak_opt_widget_layout = QHBoxLayout(self.sbreak_opt_widget)
        self.sbreak_opt_widget_layout.setSpacing(0)
        self.sbreak_opt_widget_layout.setContentsMargins(4, 0, 4, 0)

        self.sbreak_opt_label = QLabel(self.sbreak_opt_widget)

        sp.setHeightForWidth(self.sbreak_opt_label.sizePolicy().hasHeightForWidth())

        self.sbreak_opt_label.setSizePolicy(sp)
        self.sbreak_opt_label.setText("Short break: ")

        self.sbreak_opt_input = QSpinBox(self.sbreak_opt_widget)
        self.sbreak_opt_input.setMinimumSize(QSize(59, 0))
        self.sbreak_opt_input.setValue(5)

        self.sbreak_opt_widget_layout.addWidget(self.sbreak_opt_label)
        self.sbreak_opt_widget_layout.addWidget(self.sbreak_opt_input)


        # ==== Long break widget ====
        self.lbreak_opt_widget = QWidget(self.input_frame)

        self.lbreak_opt_widget_layout = QHBoxLayout(self.lbreak_opt_widget)
        self.lbreak_opt_widget_layout.setSpacing(0)
        self.lbreak_opt_widget_layout.setContentsMargins(4, 0, 4, 0)

        self.lbreak_opt_label = QLabel(self.lbreak_opt_widget)

        sp.setHeightForWidth(self.lbreak_opt_label.sizePolicy().hasHeightForWidth())

        self.lbreak_opt_label.setSizePolicy(sp)
        self.lbreak_opt_label.setText("Long break: ")

        self.lbreak_opt_input = QSpinBox(self.lbreak_opt_widget)
        self.lbreak_opt_input.setMinimumSize(QSize(59, 0))
        self.lbreak_opt_input.setValue(20)

        self.lbreak_opt_widget_layout.addWidget(self.lbreak_opt_label)
        self.lbreak_opt_widget_layout.addWidget(self.lbreak_opt_input)


        # ==== Pomodori count widget ====
        self.pomodori_opt_widget = QWidget(self.input_frame)

        self.pomodori_opt_widget_layout = QHBoxLayout(self.pomodori_opt_widget)
        self.pomodori_opt_widget_layout.setSpacing(0)
        self.pomodori_opt_widget_layout.setContentsMargins(4, 0, 4, 4)

        self.pomodori_opt_label = QLabel(self.pomodori_opt_widget)
        
        sp.setHeightForWidth(self.pomodori_opt_label.sizePolicy().hasHeightForWidth())
        
        self.pomodori_opt_label.setSizePolicy(sp)
        self.pomodori_opt_label.setText("Pomodori: ")

        self.pomodori_opt_input = QSpinBox(self.pomodori_opt_widget)
        self.pomodori_opt_input.setMinimumSize(QSize(59, 0))
        self.pomodori_opt_input.setValue(4)

        self.pomodori_opt_widget_layout.addWidget(self.pomodori_opt_label)
        self.pomodori_opt_widget_layout.addWidget(self.pomodori_opt_input)

        self.input_frame_layout.addWidget(self.work_opt_widget)
        self.input_frame_layout.addWidget(self.sbreak_opt_widget)
        self.input_frame_layout.addWidget(self.lbreak_opt_widget)
        self.input_frame_layout.addWidget(self.pomodori_opt_widget)

        return self.input_frame


    def generate_btns(self):
        self.apply_btns = QDialogButtonBox(self)
        self.apply_btns.setStandardButtons(QDialogButtonBox.Apply|QDialogButtonBox.Cancel)
        self.apply_btns.setCenterButtons(True)

        self.apply_btns.clicked.connect(self.handle_btns)

        return self.apply_btns

    def handle_btns(self, data):
        if data.text() == "Apply":
            self.opt_signal.emit(f"work_time:{self.work_opt_input.value()};short_break:{self.sbreak_opt_input.value()};long_break:{self.lbreak_opt_input.value()};pomodori:{self.pomodori_opt_input.value()}")
            self.toggle_visibility()
        else:
            self.work_opt_input.setValue(25)
            self.sbreak_opt_input.setValue(5)
            self.lbreak_opt_input.setValue(20)
            self.pomodori_opt_input.setValue(4)
            self.toggle_visibility()

    def toggle_visibility(self):
        if self.isVisible():
            self.hide()
        else:
            self.show()
        
        