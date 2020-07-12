import os

# path of the current dir
path = os.getcwd()
# files in the current dir
file_names = os.listdir(path)



for name in file_names:
    for i in range(20):
        if name.endswith('Video-'+str(i + 1)+'.Avi'):
            os.renames(os.path.join(path, name), os.path.join(path, 'Video'+str(i + 1)+'.avi'))
            continue

