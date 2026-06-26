<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Animal Recognition System</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" />
  <style>
    body {
      background-color: #121212;
      color: #e0e0e0;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      padding-top: 40px;
    }
    .container {
      max-width: 700px;
      background: #1f1f1f;
      padding: 30px;
      border-radius: 15px;
      box-shadow: 0 0 15px rgba(255, 255, 255, 0.1);
    }
    h1 {
      color: #90caf9;
      font-weight: 700;
      margin-bottom: 30px;
      text-align: center;
    }
    .btn-primary {
      background-color: #1e88e5;
      border: none;
    }
    .btn-primary:hover {
      background-color: #1565c0;
    }
    .result {
      margin-top: 25px;
      text-align: center;
    }
    .result img {
      max-width: 100%;
      border-radius: 10px;
      margin-bottom: 15px;
      box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    footer {
      margin-top: 50px;
      text-align: center;
      color: #666;
    }
  </style>
</head>
<body>
  <div class="container">
    <h1>Animal Recognition System</h1>
    <form method="POST" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="fileInput" class="form-label">Upload an image of an animal:</label>
        <input class="form-control form-control-lg" type="file" id="fileInput" name="file" accept="image/*" required />
      </div>
      <button type="submit" class="btn btn-primary w-100 btn-lg">Predict</button>
    </form>

    {% if prediction %}
    <div class="result">
      <h3>Prediction: <span class="text-info">{{ prediction }}</span></h3>
      <h5>Confidence: {{ (confidence * 100) | round(2) }}%</h5>
      <img src="{{ url_for('static', filename='uploads/' + filename) }}" alt="Uploaded Image" />
    </div>
    {% endif %}
  </div>
  <footer>
    Powered by TensorFlow MobileNetV2 & Flask
  </footer>
</body>
</html>
