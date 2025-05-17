
# 📧 Email & SMS Phishing Detector

An end-to-end machine learning project that detects phishing attempts in emails and SMS messages. This tool helps identify spam or malicious content using natural language processing (NLP) and classification techniques.

## 🔍 Features

- **Text Classification**: Utilizes NLP techniques to classify messages as spam or not.
- **Pre-trained Model**: Includes a trained model (\`model.pkl\`) and vectorizer (\`vectorizer.pkl\`) for immediate use.
- **Web Interface**: Deployable via a Flask-based web application (\`app.py\`).
- **Dataset**: Employs the \`spam.csv\` dataset for training and evaluation.
- **Deployment Ready**: Contains \`Procfile\` and \`setup.sh\` for deployment on platforms like Heroku.

## 🗂️ Project Structure

```
├── app.py                      # Flask web application
├── email-spam-detection.ipynb  # Jupyter notebook for EDA and model training
├── train_and_save_model.py     # Script to train and save the model
├── model.pkl                   # Trained classification model (pickle)
├── vectorizer.pkl              # TF-IDF vectorizer (pickle)
├── spam.csv                    # Dataset used for training
├── requirements.txt            # List of Python dependencies
├── setup.sh                    # Shell script for environment setup
├── Procfile                    # Heroku deployment configuration
├── nltk.txt                    # List of required NLTK resources
├── setup_nltk.py               # Script to download NLTK resources
└── README.md                   # Project documentation
```


## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/y-a-s-h-9/Email-sms_Phish_detector.git
   cd Email-sms_Phish_detector
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Download necessary NLTK data:
   ```bash
   python setup_nltk.py
   ```

### Running the Application

To start the Flask web application:
```bash
python app.py
```

Access the application by navigating to \`http://localhost:5000\` in your web browser.

## 🧪 Training the Model

To train the model from scratch:
```bash
python train_and_save_model.py
```

This will generate \`model.pkl\` and \`vectorizer.pkl\` files used by the application.

## 📊 Dataset

The project uses the \`spam.csv\` dataset, which contains labeled messages for training the spam detection model.

## 📦 Deployment

The application is ready for deployment on platforms like Heroku. Ensure that \`Procfile\` and \`setup.sh\` are correctly configured for your deployment environment.

