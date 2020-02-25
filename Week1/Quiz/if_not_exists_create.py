import os

def new_directory(directory, filename):
  path = directory + "/" + filename
  # Before creating a new directory, check to see if it already exists
  if not os.path.exists(directory):
  # Create the new file inside of the new directory
    os.mkdir(directory)
    os.system(r"touch {}".format(path))
  # Return the list of files in the new directory
  return os.listdir(directory)
print(new_directory("PythonPrograms", "script.py"))