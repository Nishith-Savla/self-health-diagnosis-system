# Medical Diagnosis Expert System - Project Summary

## Project Overview
The **Medical Diagnosis Expert System** is a Python-based application designed to predict diseases based on user-inputted symptoms. Leveraging the power of the [experta](https://pypi.org/project/experta/) library, the system utilizes a rule-based expert system to analyze symptoms and provide probable diagnoses along with detailed descriptions and treatment recommendations.

## Features
- **User-Friendly GUI:** Built with Tkinter, the graphical user interface allows users to easily select their symptoms through categorized options.
- **Extensible Knowledge Base:** Diseases, along with their symptoms, descriptions, and treatments, are stored in organized text files, making it straightforward to add or update information.
- **Dynamic Diagnosis:** The expert system evaluates selected symptoms against predefined rules to identify potential diseases and offers detailed insights and treatment options.
- **Dark Mode Toggle:** Users can switch between light and dark themes for a comfortable viewing experience.
- **Progress Indicators:** Visual feedback during the diagnosis process enhances user experience.

## Technology Stack
- **Programming Language:** Python
- **Libraries & Frameworks:**
  - **Tkinter:** For building the graphical user interface.
  - **experta:** To implement the rule-based expert system for disease diagnosis.
- **Data Storage:** Plain text files organized into directories for diseases, symptoms, descriptions, and treatments.

## Current Functionality
- **Symptom Selection:** Users can choose from various symptoms categorized under General, Head, Chest, Body, and Other sections.
- **Diagnosis Process:** Upon selecting symptoms and initiating the diagnosis, the system processes the inputs using the expert system rules to determine the most probable disease.
- **Result Display:** Diagnosed diseases are presented in a separate window with comprehensive descriptions and recommended treatments. If no exact match is found, the system suggests the most probable disease based on symptom similarity.
- **Data Loading:** The `preprocess` function reads and organizes disease-related data from text files into appropriate data structures for efficient access during diagnosis.

## Project Structure

```
.
├── main.py
├── greetings.py
├── diseases.txt
├── requirements.txt
├── README.MD
├── Disease descriptions/
│   ├── Alzheimers.txt
│   ├── Coronavirus.txt
│   ├── Diabetes.txt
│   ├── Epilepsy.txt
│   ├── Glaucoma.txt
│   ├── Heart Disease.txt
│   ├── Heat Stroke.txt
│   ├── Hypothermia.txt
│   ├── Jaundice.txt
│   ├── Hyperthyroidism.txt
│   ├── Sinusitis.txt
│   └── Tuberculosis.txt
├── Disease symptoms/
│   ├── Alzheimers.txt
│   ├── Arthritis.txt
│   ├── Coronavirus.txt
│   ├── Diabetes.txt
│   ├── Epilepsy.txt
│   ├── Glaucoma.txt
│   ├── Heart Disease.txt
│   ├── Heat Stroke.txt
│   ├── Hypothermia.txt
│   ├── Jaundice.txt
│   ├── Hyperthyroidism.txt
│   ├── Sinusitis.txt
│   └── Tuberculosis.txt
└── Disease treatments/
    ├── Alzheimers.txt
    ├── Arthritis.txt
    ├── Coronavirus.txt
    ├── Diabetes.txt
    ├── Epilepsy.txt
    ├── Glaucoma.txt
    ├── Heart Disease.txt
    ├── Heat Stroke.txt
    ├── Hypothermia.txt
    ├── Sinusitis.txt
    └── Tuberculosis.txt
```

## Installation & Usage
1. **Installation:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Running the Application:**
   ```bash
   python main.py
   ```
3. **Usage:**
   - Select relevant symptoms from the provided categories.
   - Click on the "Diagnose" button to receive a diagnosis.
   - Use the "Toggle Dark Mode" button to switch between light and dark themes.

## License
This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

---

This summary provides an overview of the project's current state, highlighting its structure, features, and functionalities. The system is set up to offer a comprehensive medical diagnosis tool through an intuitive interface and a robust rule-based engine.