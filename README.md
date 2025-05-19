
# 📧 Email & SMS Phishing Detector
### Final Year Capstone Project – B.Tech in Computer Science
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

Access the application by navigating to \`http://localhost:8501\` in your web browser.

### Output
<img width="720" alt="Screenshot 2025-05-17 at 17 10 41" src="https://github.com/user-attachments/assets/1dc09d79-cd6d-46d5-bde8-992e2ca4e4fb" />
<img width="720" alt="Screenshot 2025-05-17 at 17 11 05" src="https://github.com/user-attachments/assets/16bae64d-ccbc-4c1e-8d53-939be9cf6f56" />

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

## 🙏 Acknowledgement

Special thanks to [**CampusX**](https://github.com/campusx-official) for their guidance and valuable resources that inspired this project.


## 👥 Contributors

- [**Yashashvi B**](https://github.com/y-a-s-h-9)
- [**Shalini Baddem**](https://github.com/shalinibaddem)
