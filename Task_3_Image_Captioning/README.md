# Image Captioning

A Python-based AI application that can understand images and generate meaningful captions. The project combines image captioning, computer vision, object detection, and AI-based image analysis.

## Features

- Generate captions for uploaded images
- Provide detailed image analysis
- Detect objects present in an image
- Generate a creative story based on the image
- Display results through a Streamlit web interface
- Easy image upload and analysis

## How It Works

The application takes an image as input and processes it using different AI models.

1. The user uploads an image.
2. The BLIP model analyzes the image and generates a caption.
3. YOLO is used for object detection.
4. The application provides detailed information about the image.
5. A story can also be generated based on the detected content.

## AI Models Used

### BLIP

BLIP (Bootstrapping Language-Image Pre-training) is used for generating captions from images.

### YOLO

YOLO (You Only Look Once) is used for detecting objects present in the image.

## Technologies Used

- Python
- Streamlit
- Hugging Face Transformers
- BLIP
- PyTorch
- YOLO
- OpenCV
- PIL

## Project Structure

```text
Task_3_Image_Captioning/
│
├── app.py
├── requirements.txt
└── README.md
