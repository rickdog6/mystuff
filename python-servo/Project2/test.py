import sys
import curses
import time

win = curses.initscr()
curses.noecho()
curses.cbreak()
win.nodelay(True)
win.keypad(True)

print ' '
print 'Press any key then <Enter> to send'
print ' '
print 'Press "q" then <Enter> to quit'
print ' '

#while True:
#   ch = raw_input()
#   if ch != "q":
#      print 'You pressed', ch
#   elif ch == "q":
#      break

while True:
    key = win.getch()
    if key != ord ('q'):
       print 'You pressed', key
    elif key == ord('q'):
       break
       curses.nocbreak()
       win.keypad(0)
       curses.echo()
       curses.endwin()
