import os

def delete_line_containing_number_large_file(file_name, number):
    # Create a temporary file
    temp_file = file_name + '.bak'
    
    with open(file_name, 'r') as read_obj, open(temp_file, 'w') as write_obj:
        # Line by line copy data from original file to temporary file
        for line in read_obj:
            # If current line does not contain the number, copy it to temporary file
            if str(number) not in line:
                write_obj.write(line)
                
    # Remove the original file
    os.remove(file_name)
    # Rename the temporary file as the original file
    os.rename(temp_file, file_name)

delete_line_containing_number_large_file('/home/vboxuser/Voice-Assistant/output.txt', 2826)
