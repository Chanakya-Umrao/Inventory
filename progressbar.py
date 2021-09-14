from tkinter import *
from tkinter.ttk import *
import time
import threading

# Define the process of unknown duration with root as one of the input And once done, add root.quit() at the end.
def process_of_unknown_duration(root):
    time.sleep(5)
    print('Done')
    root.destroy()

# Now define our Main Functions, which will first define root, then call for call for "task(root)" --- that's your progressbar, and then call for thread1 simultaneously which will  execute your process_of_unknown_duration and at the end destroy/quit the root.

root = Tk()
t1=threading.Thread(target=process_of_unknown_duration, args=(root,))
t1.start()
ft =Frame()
ft.pack(expand=True, fill=BOTH,side=TOP)
pb_hD = Progressbar(ft, orient='horizontal', mode='indeterminate')
pb_hD.pack(expand=True, fill=BOTH,side=TOP)
pb_hD.start(50)
root.mainloop()
t1.join()

