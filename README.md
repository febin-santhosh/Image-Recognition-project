# Image Classification with Deep Learning

## Overview
This project is a deep learning-based image classification system developed using PyTorch. The model is trained to classify images into three categories: dog, cat, and person.

An interactive web interface is built using Gradio, allowing users to upload images and get real-time predictions. The application is designed to be deployable on Hugging Face for easy access and inference.

## Key Highlights
- Deep learning model built using PyTorch
- Image classification for dog, cat, and person
- Interactive UI using Gradio
- Real-time inference support
- Deployment-ready (Hugging Face compatible)

## Technologies Used
- Python
- PyTorch
- Gradio
- Hugging Face
- NumPy
- Pandas
- Matplotlib

## Project Structure
```
Image-Recognition-project/
│
├── GradioApp/
├── anaconda_projects/db/
├── CNN_Training.ipynb
├── cnn_model.pth
├── environment.yml
├── output_image.jpg
└── .gitignore
```

## Features
- Train a CNN model for image classification
- Predict image class (dog, cat, person)
- Upload images via web interface
- View prediction results instantly
- Easy deployment with Hugging Face Spaces

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Image-Recognition-project.git
```

### 2. Create Environment
Using conda:
```bash
conda env create -f environment.yml
conda activate your-env-name
```

### 3. Run the Application
```bash
cd GradioApp
python app.py
```

### 4. Open in Browser
http://127.0.0.1:7860

## Model Details
- Model Type: Convolutional Neural Network (CNN)
- Framework: PyTorch
- Classes: Dog, Cat, Person
- Training handled in: CNN_Training.ipynb

## Deployment
The application can be deployed on Hugging Face Spaces:
- Upload project files
- Configure app.py as entry point
- Install dependencies from environment.yml

## Future Improvements
- Add more classes
- Improve model accuracy
- Add model evaluation metrics
- Optimize inference speed
- Add image preprocessing enhancements
