
from PyQt5.QtCore import QTimer

"""

TODO:
- Learn how to use QTimer (this might be useful: https://pythonpyqt.com/qtimer/)
- Create a count down with this technique: https://en.wikipedia.org/wiki/Pomodoro_Technique#Description
    (you don't need to add the long break if you don't want to but it would be a good challenge)
- Update the minutes and seconds with the update_minutes and update_seconds functions
    (you could add or change anything you want, but figured I'd add basic stuff)
- Bonus points for updating the state for Work sections and Break sections
    
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


    def update_minutes(self, time):
        """
        Updates the Minute display

        Parameters
        ----------
        time
            The minutes to display
        """
        
        displayMin = time

        if passedSeconds == 60:
            displayMin -= 1
            return displayMin
        elif displayMin == 0:
            break
        
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
        Updates the State label
        # Have Breaks listed as Long or Short
        # Add Pomodori count?
        # Where to add sound notif?
        # Custom upload?
        # https://freesound.org/

        Parameters
        ----------
        state : string
            State the timer is in (Work, Break, etc)
        """
        self.gui.state_label.setText(state)


    def start_timer(self):
        """
        
        """
        ...


    def pause_timer(self):
        """
        
        """
        ...

