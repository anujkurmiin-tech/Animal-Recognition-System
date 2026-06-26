# Animal-Recognition-System
A web-based Animal Recognition System built using TensorFlow.js MobileNet, HTML, CSS, and JavaScript. This application allows users to upload an image and automatically detect and classify animals using a pre-trained deep learning model running directly in the browser.


## Features

- Upload animal images directly from your device
- Uses TensorFlow.js MobileNet model for image classification
- Runs entirely in the browser with no server-side processing
- Modern responsive user interface
- Displays prediction confidence scores
- Filters results to common animal categories

---

## Project Overview

The Animal Recognition System is a browser-based application that leverages TensorFlow.js and the MobileNet pre-trained model to identify animals in uploaded images. The model loads directly in the user's browser, making the application fast, lightweight, and easy to deploy.

---

## Technologies Used

- HTML5
- CSS3
- JavaScript (ES6)
- TensorFlow.js
- MobileNet Pre-trained Model
- Google Fonts

---

## Project Structure

```text
Animal-Recognition-System/
│
├── index.html       # Main web application
├── animal.py        # Backend/UI template file
└── README.md        # Project documentation
```

---

## Installation

### Method 1: Run Locally

Clone the repository:

```bash
git clone https://github.com/yourusername/animal-recognition-system.git
```

Navigate to the project directory:

```bash
cd animal-recognition-system
```

Open `index.html` in your preferred web browser.

---

### Method 2: Using VS Code Live Server

1. Install the Live Server extension in Visual Studio Code.
2. Open the project folder.
3. Right-click on `index.html`.
4. Select **Open with Live Server**.

---

## How It Works

The application uses Google's MobileNet model through TensorFlow.js.

### Workflow

1. The user uploads an image.
2. The image is loaded into the browser.
3. MobileNet analyzes the image.
4. Predictions are generated.
5. Results are filtered to display common animal categories.
6. The application displays the predicted animal and confidence score.

### Supported Animal Categories

- Dog
- Cat
- Bird
- Horse
- Cow
- Sheep
- Elephant
- Bear
- Zebra
- Giraffe
- Lion
- Tiger
- Wolf
- Fox
- Panda
- Rabbit
- Deer

---

## Dependencies

The project uses CDN-hosted libraries:

```html
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs"></script>
<script src="https://cdn.jsdelivr.net/npm/@tensorflow-models/mobilenet"></script>
```

No additional installation is required.

---

## Screenshots

### Home Page
- Image upload interface
- Responsive design

### Results Page
- Uploaded image preview
- Animal prediction results
- Confidence percentages

---

## Limitations

- Only detects animals recognizable by the MobileNet model.
- Prediction accuracy depends on image quality.
- Some animal species may not be classified correctly.
- Works best with clear, high-resolution images.

---

## Future Improvements

- Add support for more animal species
- Implement custom-trained models
- Add real-time webcam detection
- Include object detection and bounding boxes
- Support multiple animal recognition
- Deploy as a Progressive Web Application (PWA)

---

## Developer

**Developed by:** Gaurav Kurmi

---

## License

This project is released under the MIT License.

---

## Acknowledgements

- TensorFlow.js Team
- Google MobileNet Model
- Open Source Community
