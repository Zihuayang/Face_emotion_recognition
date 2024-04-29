Deployment: 
You are able to use any coding editor of your choice but we recommend using VS code to run our project.

First, download the zip folder from the link above and open it using visual code. 
In the terminal, type 
“pip install Pillow”
“pip install opencv-python”
“python -m pip install opencv-python”
This will install all the necessary packages that will allow our code to work correctly.

Next, run the “train.py” file, which will create “trainer.yml” file under the trainer folder. Since we already have it, you don’t need to run this file. But if you want to add more datasets or emotions, we are going to need to delete the old trainer.yml and rerun the train.py.

Open the “Recognition.py” file, look for line #30 
img = cv2.imread("happy.jpg")
And replace “happy.jpg” with your desire image. In our case, it will be happy.jpg
Scroll down to line #60 
cv2.imwrite("happytest.jpg", img)
	And give it an image name, it could be anything, but we gonna use “happytest.jpg.” Then, run the code. 

If everything works correctly, a “happytest.jpg” will be created.
Now, we will try recognizing a picture in real-time. Go to the “recongnition.py” and uncomment line #27 
ret, img =cam.read()   #camera picture
And comment #30
#img = cv2.imread("happy.jpg")
	
Next, go down to line #60 and give it a name
cv2.imwrite("happytest1.jpg", img)
Then, run the code.
A happytest1.jpg file will be created.
 
