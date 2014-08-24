import curses, traceback
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)

global servo_x, center, new, pos;
servo_x = GPIO.PWM(4,50)
center = 6.0
new = 0.0
pos = center + new

servo_x.start(center)


def main(stdscr):
  global screen
  text = "This is a test"
  screen = stdscr.subwin(0, 0)
  screen.box() # Wrap screen window in box
# Get window dimensions

  y, x = screen.getmaxyx()
  global cur_x, cur_y;

# Sets the cursor to center the text on screen
  cur_x = (x/2)-(len(text))/2
  cur_y = (y/2)

# Add string to screen
  screen.addstr( cur_y, cur_x, text)
  screen.refresh() # Refresh to populate screen with data

  c = screen.getch() # Get char

  while c != ord('q'): # Exit loop if char caught is 'q'
    screen.addstr(1,1,str(c))
    screen.refresh()
    if c == 65: # ARROW_UP
      move_up(text, screen)
    elif c == 66: # ARROW_DOWN
      move_down(text, screen)
    elif c == 68: # ARROW_LEFT
      move_left(text, screen)
    elif c == 67: # ARROW_RIGHT
      move_right(text, screen)
    elif c == 410:
      y, x = screen.getmaxyx()
      curses.resizeterm(y, x) # Resize curses boundaries
      move_center(text,screen)

    c = screen.getch()

  return

# Moves text up by one
def move_up(text, screen):
  screen.clear()
  screen.box()
  global cur_y, cur_x
  cur_y = cur_y - 1
  screen.addstr( cur_y, cur_x, text)
  screen.refresh()

# Moves text down by one
def move_down(text, screen):
  screen.clear()
  screen.box()
  global cur_y, cur_x
  cur_y = cur_y + 1
  screen.addstr( cur_y, cur_x, text)
  screen.refresh()

# Moves text right by one
def move_right(text, screen):
  screen.clear()
  screen.box()
  global cur_y, cur_x
  cur_x = cur_x + 1
  screen.addstr( cur_y, cur_x, text)
  screen.refresh()
  global servo_x, center, new, pos
  new = new - 1.0
#  while 0.0 <= new <= 12.0:
  if pos == 6.0:
    servo_x.ChangeDutyCycle(center + new)
    time.sleep(0.25)
  
#  servo_x.ChangeDutyCycle(0.0)
#  print "Stop it!"
  elif 1.0 < pos < 6.0:
    servo_x.ChangeDutyCycle(pos + new)
    time.sleep(0.25)
  elif 6.0 < pos <= 12.0:
    servo_x.ChangeDutyCycle(pos + new)
  elif pos <= 1.0:
    servo_x.ChangeDutyCycle(0.0)
  elif center + new < 1.0:
    servo_x.ChangeDutyCycle(center - new)

# Moves text left by one
def move_left(text, screen):
  screen.clear()
  screen.box()
  global cur_y, cur_x
  cur_x = cur_x - 1
  screen.addstr( cur_y, cur_x, text)
  screen.refresh()
  global servo_x, center, new, pos
  new = new + 1.0
  if pos == 6.0:
    servo_x.ChangeDutyCycle(center + new)
    time.sleep(0.25)
  elif 0.0 <= pos < 6.0:
    servo_x.ChangeDutyCycle(pos + new)
    time.sleep(0.25)
  elif 6.0 < pos <= 12.0:
    servo_x.ChangeDutyCycle(pos + new)
  elif pos == 12.0:
    servo_x.ChangeDutyCycle(12.0)

# Centers text in window
def move_center(text, screen):
  screen.clear()
  screen.box()
  global cur_y, cur_x
  y, x = screen.getmaxyx()
  cur_x = (x/2)-(len(text))/2
  cur_y = (y/2)
  screen.addstr( cur_y, cur_x, text)
  screen.refresh()
if __name__ == '__main__':
  try:

# Initialize curses
    stdscr=curses.initscr()
# Turn off echoing of keys, and enter cbreak mode,
# where no buffering is performed on keyboard input
    curses.noecho()
    curses.cbreak()
# In keypad mode, escape sequences for special keys
# will be interpreted and a special value like
# curses.KEY_LEFT will be returned
    stdscr.keypad(1)
    curses.curs_set(0) # Hide cursor position
    main(stdscr) # enter main loop
  except curses.error:
# In the event of error, restore terminal to sane state
    traceback.print_exc() # Print the exception
    print(curses.ERR)
  except KeyboardInterrupt:
# Caught KeyboardInterrupt (Gets rid of stacktrace)
# Set everything back to normal before exit
    stdscr.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()
    exit()
  finally:
# Set everything back to normal
    stdscr.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()
