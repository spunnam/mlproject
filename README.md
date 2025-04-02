# Predicting Student Exam Performance Using Machine Learning

## Overview

This project aims to build a comprehensive machine learning model capable of predicting students' academic performance based on demographic and educational data. Utilizing the "Students Performance in Exams" dataset, the project integrates data preprocessing, exploratory data analysis (EDA), model building, evaluation, and deployment through AWS Elastic Beanstalk, complemented by a robust CI/CD pipeline using AWS CodePipeline.

## Project Objective

The core objective is to analyze various demographic and educational factors influencing student performance, build a predictive regression model, and deploy the model to predict scores effectively in real-time scenarios.

## Dataset Information

- **Dataset Name:** Students Performance in Exams
- **Source:** [Kaggle Dataset Link](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
- **Description:** Contains student scores in Math, Reading, and Writing along with features such as gender, race/ethnicity, parental education level, lunch type, and test preparation status.

### Key Features:

- **Gender:** Male or Female
- **Race/Ethnicity:** Group classifications
- **Parental Level of Education:** Highest education level attained by parents
- **Lunch:** Standard or free/reduced
- **Test Preparation Course:** Completed or not completed
- **Math Score:** Numeric score
- **Reading Score:** Numeric score
- **Writing Score:** Numeric score

## Project Structure

```
student-performance-predictor/
├── .ebextensions/          # Elastic Beanstalk configuration
├── notebook/               # Jupyter notebooks for EDA and modeling
├── src/                    # Data processing and model scripts
├── templates/              # HTML templates for Flask application
├── application.py          # Main Flask application file
├── requirements.txt        # Python dependencies
└── setup.py                # Setup script for packaging
```

## Implementation Steps

### 1. Data Collection

- Sourced from Kaggle: [Students Performance Dataset](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams).

### 2. Data Preprocessing

- Managed missing data, encoded categorical variables, and normalized data.
- Split dataset into training and testing subsets.

### 3. Exploratory Data Analysis (EDA)

- Utilized visualizations to uncover relationships between variables.
- Determined significant predictors of student performance.

### 4. Model Development

- Evaluated multiple regression algorithms (e.g., Linear Regression, Random Forest, XGBoost).
- Optimized model performance through hyperparameter tuning.

### 5. Model Evaluation

- Assessed using performance metrics: RMSE, MAE, and R².
- Selected the optimal model based on validation results.

### 6. Deployment

- Deployed Flask-based application with Docker.
- Hosted on AWS Elastic Beanstalk for scalable and reliable web deployment.
- Configured CI/CD pipeline using AWS CodePipeline to automate continuous integration and deployment.

## Technologies Used

- **Programming Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
- **Framework:** Flask
- **Deployment:** AWS Elastic Beanstalk, Docker
- **CI/CD:** AWS CodePipeline

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/spunnam/student-performance-predictor.git
```

### Navigate to the Project Directory

```bash
cd student-performance-predictor
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python application.py
```

### Access the Web Interface

- Open your web browser and visit: `http://localhost:5000`

## AWS Deployment

The deployed application leverages AWS Elastic Beanstalk for ease of scalability and reliability. AWS CodePipeline ensures smooth, automated updates through a robust CI/CD pipeline.

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. Refer to the LICENSE file for details.
