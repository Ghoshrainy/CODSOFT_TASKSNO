# AI Image Captioning

## 📌 Project Overview

AI Image Captioning is an AI-based application that analyzes an uploaded image and generates meaningful information about it.

The project uses deep learning models to:
- Generate captions for images
- Detect objects present in an image
- Analyze image content
- Generate a creative story based on the image
- Provide results through an interactive Streamlit web application

## 🚀 Features

### 1. Image Captioning
Generates a natural-language description of the uploaded image using the BLIP image captioning model.

### 2. Object Detection
Detects objects present in the image using the YOLO model and displays the detected objects with confidence scores.

### 3. Image Analysis
Provides additional information about the uploaded image based on the generated caption and detected objects.

### 4. Story Generation
Generates a creative story based on the content of the uploaded image.

### 5. Streamlit Interface
Provides a simple and interactive web interface for uploading images and viewing the AI-generated results.

## 🛠️ Technologies Used

- Python
- Streamlit
- PyTorch
- Hugging Face Transformers
- BLIP
- YOLO
- Ultralytics
- Pillow (PIL)
- NumPy

## 🤖 AI Models Used

### BLIP
Model:
`Salesforce/blip-image-captioning-base`

Used for generating captions from images.

### YOLO
YOLO is used for object detection in the uploaded image.

Model:
`yolo11n.pt`

## 📂 Project Structure

```text
AI-Image-Captioning/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── images/
│   ├── dog.jpg
│   └── man.jpg
│
├── outputs/
│
├── src/
│   ├── caption_generator.py
│   ├── image_analyzer.py
│   ├── image_processor.py
│   ├── object_detector.py
│   ├── story_generator.py
│   └── utils.py
│
├── yolo11n.pt
└── venv/