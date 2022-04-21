# Renaming Files and Folders:

## About the project:
* I created this project to rename zoom lectures recordings starting from "Part1"
* This project only renames file  with the extension `.mp4`

## Methods used:
### `os.listdir(path)`
* The `os.listdir(path)` method in Python gets the files and directories present in a given path.
* This method returns the list of files and directories in a given path.
* It takes an optional `path` parameters 
* Read more [here](https://www.geeksforgeeks.org/python-os-listdir-method/)

### `file.endswith("extension name")`

### `os.rename(old_name, new_name)`
* [Read more](https://www.tutorialspoint.com/python/os_rename.htm)


## Notes:
* In the path, the "\" should be changes to "/"
* Change the path to your directory and run `python main.py` to run the code