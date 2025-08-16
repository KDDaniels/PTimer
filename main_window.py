
from PyQt5.QtWidgets import QMainWindow, QWidget, QFrame, QLabel, QPushButton, QToolButton, QLCDNumber, QSizePolicy, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QSize, pyqtSignal, Qt
from timer import Timer
from options_window import OptionsWindow

class MainWindow(QMainWindow):
    """
    Main Window for the pomodoro timer
    """
    def __init__(self):
        """
        Constructs new MainWindow object
        """
        super().__init__()
        self.timer = Timer(self)
        self.option_window = OptionsWindow()
        self.setup_window()

        self.option_window.opt_signal.connect(self.handle_options)


    def setup_window(self):
        """
        Initializes main window parameters
        """
        self.resize(190, 120)
        self.setMinimumSize(QSize(0, 120))

        self.setWindowTitle("Pomodoro")
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        self.generate_ui_elements()


    def generate_ui_elements(self):
        """
        Generates the main container
        """
        self.central_widget = QWidget(self)
        self.central_widget_layout = QVBoxLayout(self.central_widget)

        self.central_widget_layout.addWidget(self.generate_number_widget())
        self.central_widget_layout.addWidget(self.generate_button_widget())

        self.setCentralWidget(self.central_widget)


    def generate_number_widget(self):
        """
        Generates the entire number widget
        """
        self.number_frame = QFrame(self.central_widget)
        sp1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sp1.setHorizontalStretch(0)
        sp1.setVerticalStretch(5)
        sp1.setHeightForWidth(self.number_frame.sizePolicy().hasHeightForWidth())

        self.number_frame.setSizePolicy(sp1)
        self.number_frame.setFrameShape(QFrame.Box)
        self.number_frame.setFrameShadow(QFrame.Sunken)

        self.number_frame_layout = QHBoxLayout(self.number_frame)
        self.number_frame_layout.setSpacing(1)
        self.number_frame_layout.setContentsMargins(1, 1, 1, 1)

        self.lcd_minute = QLCDNumber(self.number_frame)
        sp2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sp2.setHorizontalStretch(1)
        sp2.setVerticalStretch(0)
        sp2.setHeightForWidth(self.lcd_minute.sizePolicy().hasHeightForWidth())

        self.lcd_minute.setSizePolicy(sp2)
        self.lcd_minute.setFrameShape(QFrame.NoFrame)
        self.lcd_minute.setDigitCount(2)
        self.lcd_minute.setSegmentStyle(QLCDNumber.Flat)
        self.lcd_minute.setMode(QLCDNumber.Mode.Dec)
        self.lcd_minute.display("00")

        self.separator = QLabel(self.number_frame)
        sp1.setHeightForWidth(self.separator.sizePolicy().hasHeightForWidth())
        self.separator.setSizePolicy(sp1)
        self.separator.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">:</span></p></body></html>")

        self.lcd_second = QLCDNumber(self.number_frame)
        sp2.setHeightForWidth(self.lcd_second.sizePolicy().hasHeightForWidth())
        
        self.lcd_second.setSizePolicy(sp2)
        self.lcd_second.setFrameShape(QFrame.NoFrame)
        self.lcd_second.setDigitCount(2)
        self.lcd_second.setSegmentStyle(QLCDNumber.Flat)
        self.lcd_second.display("00")

        self.number_frame_layout.addWidget(self.lcd_minute)
        self.number_frame_layout.addWidget(self.separator)
        self.number_frame_layout.addWidget(self.lcd_second)

        return self.number_frame


    def generate_button_widget(self):
        """
        Generates the entire button widget
        """
        self.btn_widget = QWidget(self.central_widget)

        self.btn_widget_layout = QHBoxLayout(self.btn_widget)
        self.btn_widget_layout.setSpacing(2)
        self.btn_widget_layout.setContentsMargins(0, 0, 0, 0)

        self.state_label = QLabel(self.btn_widget)

        sp = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sp.setHorizontalStretch(0)
        sp.setVerticalStretch(0)
        sp.setHeightForWidth(self.state_label.sizePolicy().hasHeightForWidth())

        self.state_label.setSizePolicy(sp)
        self.state_label.setMinimumSize(QSize(61, 0))
        self.state_label.setFrameShape(QFrame.Box)
        self.state_label.setFrameShadow(QFrame.Sunken)

        self.state_label.setText("Stopped")

        self.start_btn = QPushButton(self.btn_widget)

        sp = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sp.setHorizontalStretch(0)
        sp.setVerticalStretch(0)
        sp.setHeightForWidth(self.start_btn.sizePolicy().hasHeightForWidth())

        self.start_btn.setSizePolicy(sp)
        self.start_btn.setText("Start")
        self.start_btn.clicked.connect(self.handle_start_btn)

        self.options_btn = QToolButton(self.btn_widget)
        self.options_btn.setText("...")
        self.options_btn.clicked.connect(self.handle_option_btn)

        self.btn_widget_layout.addWidget(self.state_label)
        self.btn_widget_layout.addWidget(self.start_btn)
        self.btn_widget_layout.addWidget(self.options_btn)

        return self.btn_widget
    

    def handle_start_btn(self):
        """
        Handles the start button being clicked
        """
        self.timer.is_running = not self.timer.is_running

        if self.timer.is_running:
            self.timer.start_timer()
            self.start_btn.setText("Pause")
        else:
            self.timer.pause_timer()
            self.start_btn.setText("Start")
        ...

    def handle_option_btn(self):
        """
        Handles the option button being clicked
        """
        self.option_window.toggle_visibility()
        

    def handle_options(self, opts):
        """
        Processes and handles the options data a bit
        """
        args = opts.split(";")
        print(args)
        # self.timer.set_options(args)
        ...

