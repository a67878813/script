import win32api
import win32con
from threading import Timer
from pywinauto.win32_hooks import Hook
from pywinauto.win32_hooks import KeyboardEvent
from pywinauto.win32_hooks import MouseEvent

import threading

import time


def on_timer():
    """Callback by timer out"""
    win32api.PostThreadMessage(main_thread_id, win32con.WM_QUIT, 0, 0);


def on_event(args):
    global monitor_thread_id
    global hk
    """Callback for keyboard and mouse events"""
    if isinstance(args, KeyboardEvent):
        if args.current_key == 'A' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
            print("Ctrl + A was pressed");

        if args.current_key == 'K' and args.event_type == 'key down':
            print("K was pressed");

        if args.current_key == 'M' and args.event_type == 'key down' and 'U' in args.pressed_key:
            hk.unhook_mouse()
            print("Unhook mouse")

        if args.current_key == 'K' and args.event_type == 'key down' and 'U' in args.pressed_key:
            hk.unhook_keyboard()
            print("Unhook keyboard")
        if args.current_key == 'T' and args.event_type == 'key down' and 'S' in args.pressed_key:
            hk.unhook_keyboard()
            print("Unhook keyboard")
            win32api.PostThreadMessage(monitor_thread_id, win32con.WM_QUIT, 0, 0);

    if isinstance(args, MouseEvent):
        if args.current_key == 'RButton' and args.event_type == 'key down':
            print ("Right button pressed")

        if args.current_key == 'WheelButton' and args.event_type == 'key down':
            print("Wheel button pressed")


def mouse_key_hook():
    global monitor_thread_id
    global hk
    monitor_thread_id = win32api.GetCurrentThreadId()
    hk = Hook()
    hk.handler = on_event
    
    hk.hook(keyboard=True, mouse=True)




def main():
    monitor_thread = threading.Thread(target=mouse_key_hook,name='monitor01')
    monitor_thread.start()
    
    main_thread_id = win32api.GetCurrentThreadId()
    #monitor_thread.join()#zu se
    #thread2.join()#zu se
    #print(threading.active_count())
    #print(threading.enumerate())
    #print(threading.current_thread())
    print('all done')




if __name__ == '__main__':
    print('')
    main()
