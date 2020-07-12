import os

# path of the current dir
path = os.getcwd()
# files in the current dir
file_names = os.listdir(path)

cfgList = []

# read the config file, write to cfgList
with open("cfglist.txt", "r") as f:     # open file
    data = f.readlines()
    for line in data:
        line = line.strip('\n')
        cfgList.append(line)

for name in file_names:
        if name.endswith('.mp4') and (not 'nhvod' in name):
            os.rename(os.path.join(path, name), os.path.join(path, name.split('.')[0] + '_' + cfgList[(int(name.split('_')[0][5:]) - 1) * 5 + int(name.split('_')[1][:-4]) - 1] + '.mp4'))

    