import lvgl as lv
from ili9XXX import *
from ft6x36 import ft6x36
disp = st7796(mhz=40, invert=True, hybrid=True, double_buffer=True, rot=REVERSE_LANDSCAPE) #Dark Theme
touch = ft6x36(sda=18, scl=19, width=320, height=480, inv_x=False, inv_y=True, swap_xy=True)
