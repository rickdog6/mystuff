import os
import fileinput

if __name__ == '__main__':
    # Menu should not have any marker, just pure contents
    with open('left.php') as f:
        menu_contents = f.read()

    # Initialize a few items
    start_marker = '<!--begin-left-->'
    end_marker   = '<!--end-left-->'
    file_list = ['index.html',
    		 'reader.html',
                 'tld.html',
            	 'checklists/calsched.html',
                 'checklists/issue.html']
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
