import os

def main():
    i=1
    path = r'D:/OneDrive - LTUC/Documents/Zoom/test2/'

    for filename in os.listdir(path):
        if filename.endswith(".mp4"):
            new_name = "Part " + str(i) + ".mp4"
            old_name = path + filename
            new_name = path + new_name
            os.rename(old_name, new_name)
            i+=1

if __name__ == '__main__':
    main()