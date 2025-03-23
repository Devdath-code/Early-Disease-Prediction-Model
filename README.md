# Early-Disease-Prediction-Model

An advanced machine learning system designed to **predict early signs of diseases** which is **based on patient data and symptoms**. This tool aims to assist healthcare professionals in early diagnosis and intervention.

**Features**

Predictive analysis for multiple diseases
User-friendly web interface for inputting patient data
High accuracy prediction model
Detailed results with confidence scores
Responsive design for desktop and mobile devices

**Installation**

Prerequisites

Python 3.7 or higher
pip (Python package installer)
Git

**Setup Instructions**

Clone the repository:
Copygit clone https://github.com/Devdath-code/Early-Disease-Prediction-Model.git
cd Early-Disease-Prediction-Model

Install required dependencies:
Copypip install -r requirements

Download the model file:

The model file (model.pkl) is not included in the repository due to its large size.
Download it from https://drive.google.com/file/d/1tDdLTys9V6rWPF94wz5OPDssY7VkIpYQ/view?usp=sharing
Place the downloaded file in the root directory of the project.

**Usage**

Start the application:
Copypython app.py

Open your web browser and navigate to:
Copyhttp://localhost:5000

Enter patient data in the provided form and submit to get prediction results.

**Model Information**

### Architecture
This model uses a Random Forest classifier trained on a comprehensive healthcare dataset containing patient records with various symptoms and diagnostic outcomes. The model processes key features including:
- Patient demographic information (age, gender)
- Vital signs (blood pressure, heart rate, temperature)  
- Laboratory test results (blood count, cholesterol levels, glucose levels)
- Reported symptoms and their duration
- Family history indicators
- Lifestyle factors (smoking, alcohol consumption, physical activity)

### Performance
- Accuracy: 87.5%
- Precision: 85.3%
- Recall: 83.9%
- F1 Score: 84.6%

The model was validated using 5-fold cross-validation on a holdout test set comprising 20% of the original dataset.

**Limitations**

This model is designed as a supportive tool for healthcare professionals and should not replace professional medical diagnosis. Results should be interpreted by qualified medical practitioners.
Project Structure
Copydisease_prediction_model/
├── app.py                  # Flask web application
├── model.pkl               # Trained model (to be downloaded separately)
├── requirements            # Required Python packages
├── templates/              # HTML templates for web interface
└── [other directories]     # Additional project files

Future Enhancements

Integration with electronic health records
Mobile application development
Additional disease prediction capabilities
Explainable AI features for better interpretation
