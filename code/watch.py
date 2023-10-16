import threading
import time

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

    def get_time(self):
        return self._elapsed_time
    

class WatchWidget:
    def __init__(self, watch):
        self.watch = watch



    