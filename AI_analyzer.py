import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image

# Load class labels from file
def load_labels(label_path="class_labels.txt"):
    with open(label_path, "r") as f:
        return [line.strip() for line in f.readlines()]

# Load the TensorFlow Lite model
def load_model(model_path="eco_model.tflite"):
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    return interpreter

# Classify image using the TFLite model
def classify_image(interpreter, image):
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    image = image.resize((224, 224))  # Resize to model input size
    input_data = np.expand_dims(np.array(image) / 255.0, axis=0).astype(np.float32)

    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])

    predicted_class = np.argmax(output_data[0])
    confidence_score = output_data[0][predicted_class]
    return predicted_class, confidence_score

# Streamlit interface for AI Analyzer
def ai_analyzer():
    st.title("🤖 AI Analyzer: Classify Your Eco-Friendly Action")

    labels = load_labels("features/class_labels.txt")

    interpreter = load_model("features/eco_model.tflite")

    uploaded_file = st.file_uploader("Upload an image of your eco-action", type=["png", "jpg", "jpeg"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Analyze Image"):
            predicted_idx, confidence = classify_image(interpreter, image)
            predicted_label = labels[predicted_idx]

            st.success(f"✅ Predicted Action: {predicted_label}")
            st.write(f"Confidence Score: {confidence:.2f}")

            correction = st.selectbox("Is this correct?", ["Yes", "No"])
            if correction == "No":
                corrected_label = st.selectbox("Select Correct Action", labels, index=predicted_idx)
            else:
                corrected_label = predicted_label

            if st.button("Confirm Action"):
                st.session_state["classified_action"] = corrected_label
                st.success(f"Action '{corrected_label}' saved. You can now estimate CO₂ savings.")
