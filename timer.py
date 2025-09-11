
from PyQt5.QtCore import QTimer

"""

functions
    setup
    start if not started
    toggle
    pause/resume


"""


class Timer:
    """
    Timer component for a pomodoro timer
    """
    def __init__(self, gui):
        """
        Constructs a new Timer object

        Parameters
        ----------
        gui
            the gui element containing the number displays
        """
        self.gui = gui
        self.is_running = False
        self.timer = None
        self.update_timer = None
        self.state = "Work"
        self.state_num = 1

        self.work_time = 25
        self.short_break = 5
        self.long_break = 20
        self.pomodori = 3

        self.current_time = 0
        self.current_pomodori = 0


    def update_options(self, work_time = 25, short_break = 5, long_break = 20, pomodori = 4):
        self.work_time = int(work_time)
        self.short_break = int(short_break)
        self.long_break = int(long_break)
        self.pomodori = int(pomodori)


    def setup_timers(self):
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_pomodori)
        self.time_remaining = self.work_time * 60000

        self.update_time()

        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update_time)
        self.update_timer.start(1000)

        self.gui.update_icon("work32.png")
        self.update_state(self.state)


    def update_time(self):
        seconds_rounded = int(round(self.timer.remainingTime(), -2) / 1000)

        self.update_minutes(f"{int(seconds_rounded/60):02d}")
        self.update_seconds(f"{int(seconds_rounded%60):02d}")
    

    def update_pomodori(self):

        if self.state_num == 0:
            # set work time
            self.time_remaining = self.work_time
            self.state = "Work"

            print(f"[INFO] Setting work state")
            self.gui.update_icon("work32.png")

            self.state_num += 1

        elif self.state_num == 1:
            # set short break time
            self.time_remaining = self.short_break
            self.state = "Break"

            print(f"[INFO] Setting short break state")
            self.gui.update_icon("short32.png")

            self.state_num += 1


        if self.state_num == 2:
            self.current_pomodori += 1
            self.state_num = 0


        if self.current_pomodori == self.pomodori:
            # set long break time, reset essentially

            self.time_remaining = self.long_break
            self.state = "Long"

            print(f"[INFO] Setting long break state")
            self.gui.update_icon("long32.png")

            self.current_pomodori = 0

        self.update_state(self.state)
        self.timer.start((self.time_remaining * 60000))
        self.update_time()


    def update_minutes(self, time):
        """
        Updates the Minute display

        Parameters
        ----------
        time
            The minutes to display
        """
        self.gui.lcd_minute.display(time)


    def update_seconds(self, time):
        """
        Updates the Seconds display

        Parameters
        ----------
        time
            The seconds to display
        """
        self.gui.lcd_second.display(time)


    def update_state(self, state : str):
        """
        Updates the State
        """
        self.gui.state_label.setText(state)


    def pause_resume_timer(self):
        """
        
        """
        if self.timer == None:
            self.setup_timers()
            
        self.is_running = not self.is_running

        if self.is_running == False:
            # pause
            self.time_remaining = self.timer.remainingTime()
            self.timer.stop()
            self.update_timer.stop()
            self.update_state("Paused")
        elif self.is_running == True:
            # resume
            self.timer.start(self.time_remaining)
            self.update_time()
            self.update_timer.start(1000)
            self.update_state(self.state)

