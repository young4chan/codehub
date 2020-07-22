# codehub
common codes to be used elsewhere

# movieclip.py
save clip from .avi to mp4
attributes:
  argv[1]: .avi filename
  argv[2]: start time, represented in mm:ss
  argv[3]: end time, represented in mm:ss
  argv[4]: suffix of the name .mp4 file to be saved

# rename.py
rename the file whose name ended with 'Video-i.Avi' to 'Videoi.avi', 'i' in 'Video-i.Avi' after the dash sign and 'i' in 'Videoi.avi' after 'Video' is an integer number

# videonameupdate.py
append cfg to the name of each saved video from the movieclip process.
the cfg reads from a cfglist.txt

# autosavepic.py
It detects the text in a specific area of a picture, inject in into Baidu OCR api, get the result. However, the output is quite poor.

# binarysearch.py
It defines how to traverse a binary tree and query a tree.

# dfs.py
Implement the dfs algorithm and bfs algorithm, while the maze application is not tested and incompleted

# soLibEncap
To create a dynamic library, hide the implementation detals and leaves only the interface
## Usage:
'''  
cd soLibEncap  
sudo g++ -fpic -shared -o libA.so file1.cpp file2.cpp -I /usr/local/include -L /usr/local/lib -lopencv_core -lopencv_highgui  
export LD_LIBRARY_PATH=/home/young/project/codehub/soLibEncap:$LD_LIBRARY_PATH  
g++ -o demo demo.cpp -L. -lA  
'''
