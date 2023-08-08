import os

# Open the file in read mode and get all lines
with open("D:\\Datasets\\Speech_Dataset\\vivos\\train\\prompts.txt", "r", encoding='utf-8') as file:
    lines = file.readlines()

# List of strings to be removed
remove_list = ["VIVOSSPK04", "VIVOSSPK05", "VIVOSSPK07", "VIVOSSPK08", "VIVOSSPK09", "VIVOSSPK10", "VIVOSSPK11", "VIVOSSPK12", "VIVOSSPK13", "VIVOSSPK15", "VIVOSSPK16", "VIVOSSPK17", "VIVOSSPK18", "VIVOSSPK19", "VIVOSSPK20", "VIVOSSPK21", "VIVOSSPK22", "VIVOSSPK23", "VIVOSSPK24", "VIVOSSPK27", "VIVOSSPK28", "VIVOSSPK29", "VIVOSSPK30", "VIVOSSPK31", "VIVOSSPK32", "VIVOSSPK33", "VIVOSSPK35" , "VIVOSSPK36", "VIVOSSPK37", "VIVOSSPK38", "VIVOSSPK39", "VIVOSSPK42"]

# Open the temporary file in write mode
with open("temp.txt", "w", encoding='utf-8') as file:
    for line in lines:
        # If the line contains any string from the list, do not write it to the temp file
        if not any(item in line for item in remove_list):
            file.write(line)

# Replace the original file with the modified one
# os.replace('temp.txt', 'D:\\Datasets\\Speech_Dataset\\vivos\\train\\prompts.txt')