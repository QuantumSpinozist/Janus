from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import threading
import time
import datetime

class Watch:
    def __init__(self, name):
        self.name = name
        self._start_time = None
        self._running = False
        self._elapsed_time = 0

    def start(self):
        if not self._running:
            self._start_time = time.time() - self._elapsed_time
            self._running = True
            self._thread = threading.Thread(target=self._run_clock)
            self._thread.start()

    def stop(self):
        if self._running:
            self._elapsed_time = time.time() - self._start_time
            self._running = False
            self._thread.join()

    def _run_clock(self):
        while self._running:
            time.sleep(1)
            self._elapsed_time = time.time() - self._start_time

    def get_time(self, as_str = False):
        if as_str:
            seconds = int(self._elapsed_time)
            return str(datetime.timedelta(seconds=seconds))
        else:
            return self._elapsed_time
    
    def is_running(self):
        return self._running
    

class WatchWidget:
    def __init__(self, root,watch):
        self.root = root
        self.watch = watch
        self.label = tb.Label(self.root, text='Test',bootstyle="light")

    def counter_label(self):
        def counter():
            if self.watch.is_running():
                self.label['text'] = self.watch.get_time(as_str=True)
                self.label.after(1000, counter)
        counter()

    def display(self):
        self.label.pack(pady=50)






    