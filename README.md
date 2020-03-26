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

## Edge detection
An edge may be defined as a set of connected pixels that forms a boundary between two disjoints regions.
Edge detection is basically, a method of segmenting an image into regions of discontinuity.  

There are many edge detection algorithms. i have implemented them from scratch here [mgautam98/Digital-Image-Processor/filters](https://github.com/mgautam98/Digital-Image-Processor/blob/master/src/filters.py). For this project I have used opencv python library to do the same.  

### Canny Edge detection  
Canny Edge Detection is a popular edge detection algorithm.It is a four stage algorithm, where it performs following tasks  
* Noise Reduction
> To remoe noise we apply 5x5 Gaussian filter
* Finding Intensity Gradient of the Image
>  here, we apply sobel filter in both horizontal and vertical direction the enhance the edges.
* Non-maximum Suppression and
>There are still some unwanted noise so w remove is using non-max suppression algorithm.
* Hysteresis Thresholding
> Here, we dicide which points are edge and which are not.

### Finding Distance from closest edge
The server returns a object of edges which is changed into JSON data (At server) for client to further process it.
> Initially, I was thinking to apply and graph based alorithm to find the closest edge. Eg. BFS, A*, Dijkstra etc. 
> But, I made an observation that we are returning very small proportion of data back in comparision to the image size. So, we can simply go through all the edges and find the closest one.
> So, I simply went through all the pts to get the distance.


#### Thank You for reading. 
