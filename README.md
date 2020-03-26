# SmartPen Challenge

>Create a page or tool which performs edge detection on a given image and, given a point, returns the distance from that point to the closest edge.

## Install
Install the requirements, flask, opencv-python and numpy using the following command

```
pip3 install -r requirements.txt
```

## Run
Run the app by running the following command in the termial

```
python3 app.py
```
![alt text](https://i.imgur.com/XpOM5zD.png)


Default port is :8080, you can change it in the application.  
After running go to the specified port.  

Choose an image by clickin on "choose file"  

![alt text](https://i.imgur.com/QwxaElw.png)

Click on upload to process the file  


![alt text](https://i.imgur.com/z5jTjJ6.png)
Your processed image is ready. Now click on any point in the image to get the distance of closest edge from that point in the edge detected image.  

![alt text](https://i.imgur.com/iqjLo4B.png)

## Approach
Since, in the project we will be using Tensorflow.js and most of the computations will be on the client-side I have tried to do the same here.  
In brief, following are the steps that I followed.  
1. Take the image form the user and upload it.
2. The server performs the processing part i.e. detecting the edges, and finding the edges and saves the processed image.
3. The server passes the processed image, original image as well as the edge points to the client.
4. When the user clicks on any part of the image the client invokes a function and find the coordinates of the clicked point and well as the point relative to the processed part on server.
5. The same functon finds the distance between the coordinates and closest edge.  
6. The closest edge distance is displayed on the screen to the user.  

>When we will be using Tensorflow.js, the edge detection part won't be done by server.  

