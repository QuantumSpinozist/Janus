from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from watch import Watch, WatchWidget
import time

study_watch = Watch('study')

root = tb.Window(themename='superhero')



root.title('Janus')
root.geometry('500x350')

study_widget = WatchWidget(root, study_watch)
study_widget.watch.start()
study_widget.counter_label()


study_widget.display()



root.mainloop()


