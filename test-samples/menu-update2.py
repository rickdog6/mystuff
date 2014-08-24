import os
import glob
import fileinput

if __name__ == '__main__':
    # Menu should not have any marker, just pure contents
    with open('menu.php') as f:
        menu_contents = f.read()

    # Initialize a few items
    start_marker = '<!--begin-menu-->'
    end_marker   = '<!--end-menu-->'
    file_list = []
    for root, dirs, files in os.walk('/home/rick/Dropbox/Websites/dostech'):
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
