from moviepy.editor import *
import sys

fname = sys.argv[1]
vstart = int(sys.argv[2].split(':')[0]) * 60 + int(sys.argv[2].split(':')[1])
vend = int(sys.argv[3].split(':')[0]) * 60 + int(sys.argv[3].split(':')[1])
index = sys.argv[4]

video = VideoFileClip(fname).subclip(vstart,vend)

# Make the text. Many more options are available.
#txt_clip = ( TextClip("My Holidays 2013",fontsize=70,color='white')
#             .set_position('center')
#             .set_duration(10) )

result = CompositeVideoClip([video]) # Overlay text on video
result.write_videofile(fname.strip('.avi')+'_'+index+'.mp4',fps=25) # Many options...
