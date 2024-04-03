# Step1 
Build Docker Image Using  This Command

docker build -t image_name:version .

# Step2
Run the docker image

docker run -d --name image_name  -p 5000:5000 name_of_image_which_was_build

# Step3 
open http://127.0.0.1:5000/

Now enter all details and you will get the thumbnail image

or 
you can optionally use http://127.0.0.1:5000/thumbnail as a post request

where body should have height, width, fov, theta and phi and a equirectangular image

The Height and Weight are optional they have a default value of 300

Image Thumbnail Generator
This Docker image is designed to generate thumbnail images from equirectangular images. It utilizes a web service running on port 5000.

Step 1: Build Docker Image

Execute the following command to build the Docker image:

docker build -t image_thumbnail_generator:latest .


Step 2: Run Docker Container

Run the Docker container using the built image:

docker run -d --name thumbnail_generator -p 5000:5000 image_thumbnail_generator:latest


Step 3: Access the Web Service
Once the container is running, access the web service by opening http://127.0.0.1:5000/ in your web browser and enter the values and you will get a thumbnail image.

Or 


You can generate thumbnails by submitting a POST request to http://127.0.0.1:5000/thumbnail. The request body should include the following parameters:

height (optional): The height of the thumbnail image (default: 300).
width (optional): The width of the thumbnail image (default: 300).
fov: Field of view.
theta: Theta value.
phi: Phi value.
equirectangular_image: The equirectangular image.
Example POST Request Body
json

{
    "height": 300,
    "width": 300,
    "fov": 90,
    "theta": 45,
    "phi": 30,
    "equirectangular_image": "base64_encoded_image_data"
}
Replace "base64_encoded_image_data" with the actual base64 encoded data of your equirectangular image.

