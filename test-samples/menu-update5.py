import os
import glob
import fileinput
import Tkinter
from tkFileDialog import askopenfilename
root = Tkinter.Tk()
root.withdraw() # hide the main GUI window for our example
filename = askopenfilename()

if __name__ == '__main__':
    
    try:
        input = raw_input
    except NameError:
        pass

    # Menu should not have any marker, just pure contents
    with open(filename) as f:
        menu_contents = f.read()

    # Initialize a few items
    start_marker = '<!--begin-menu-->'
    end_marker   = '<!--end-menu-->'
    file_list = []
    for root, dirs, files in os.walk(filename):
                file_list += glob.glob(os.path.join(root, '*.html'))
    found_old_contents = False

    # Loop to replace text in place
    for line in fileinput.input(file_list, inplace=True):
        line = line.rstrip()

        if line == start_marker:
            found_old_contents = True
            print(line)
            print(menu_contents)
        elif line == end_marker:
            found_old_contents = False

        if not found_old_contents:
            print(line)
