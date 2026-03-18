import gradio as gr
import os
from core.predict import ImageClassifier
from PIL import Image

cwd = os.getcwd()
model_path = os.path.join(cwd, "model", "cnn_model.pth")
class_name={0: 'Cat', 1: 'Dog', 2: 'person'}
classifier = ImageClassifier(model_path=model_path, class_name=class_name)

def classify_image(image):
    image_path = "uploaded_image.jpg"
    image.save(image_path)

    label, output_path= classifier.predict(image_path)
    
    return label, Image.open(output_path)

demo = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type='pil'),
    outputs=[gr.Textbox(label="Predicted Label"), gr.Image(label="Labeled Image")],
    title="Image Classification Gradio App",
    description="Upload an image to classify it as Cat, Dog, or Person"
)

if __name__ == "__main__":
    demo.launch()