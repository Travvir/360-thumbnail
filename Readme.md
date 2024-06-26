# Image Thumbnail Generator

This Docker image is designed to generate thumbnail images from equirectangular images. It utilizes a web service running on port 5000.

## Step 1: Build Docker Image

Execute the following command to build the Docker image:

```bash
docker build -t image_thumbnail_generator:latest .
```
## Step 2: Run Docker Container

To run the Docker container using the built image, execute the following command:

```bash
docker run -d --name thumbnail_generator -p 5000:5000 image_thumbnail_generator:latest
```

## Step 3: Access the Web Service

Once the container is running, you can access the web service by opening `http://127.0.0.1:5000/` in your web browser. 

Alternatively, you can generate thumbnails by submitting a POST request to `http://127.0.0.1:5000/thumbnail`. The request body should include the following parameters:

- `height` (optional): The height of the thumbnail image (default: 300).
- `width` (optional): The width of the thumbnail image (default: 300).
- `fov`: Field of view.
- `theta`: Theta value.
- `phi`: Phi value.
- `equirectangular_image`: The equirectangular image.

If you do not provide values for `height` and `width`, they will default to 300.

```json
{
    "height": 300,
    "width": 300,
    "fov": 90,
    "theta": 45,
    "phi": 30,
    "equirectangular_image": "base64_encoded_image_data"
}
```