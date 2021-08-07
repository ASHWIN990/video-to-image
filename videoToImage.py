#import libraries
import os
import cv2

#give video path, replace it with your's video path
video_path = 'video.mp4'
#start capturing the video
capture = cv2.VideoCapture(video_path)
img_count = 1
#create a directory to save the frames
os.mkdir('VideoToImage')

while capture.isOpened() :
    #store each frame in variable "frame"
    read_frame, frame = capture.read()
    
    if read_frame == True :
        #save the image to the directory which was created
        video_image = cv2.imwrite(f'VideoToImage//image{img_count}.png', frame)
        
        if video_image == True :
            print(f'Image is saved at :- VideoToImage//image{img_count}.png')
            img_count += 1
            
        cv2.imshow('videoplayer', frame)
        #press 'q' to quite the operation
        if cv2.waitKey(25) & 0xff == ord('q') :
            break
        
    else :
        print('Unable to read frame')
        break

capture.release()
cv2.destroyAllWindows()