
# using the `with` statement here instead of
#   open("file", "mode") # where mode is "r" read or "w" write
#   data = file.read()
#   file.close()
# because with automatically closes the file when your code
# finishes running--no need to call file.close()

# current_directory = os.getcwd()
# file_path = os.path.join(current_directory, "spanish_english_alignment.txt")

# with open(file_path, "r") as file:
def process():
    with open("test/spanish_english_alignment.txt", "r") as file:
        return file.readlines()
