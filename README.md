# Multi-Model-AI-System-for-Industrial-Quality-Assurance

---

## Overview
This project focuses on developing an AI-powered Quality Assurance (QA) system for the manufacturing industry. In heavy manufacturing, small defects such as cracks, scratches, or surface imperfections on steel sheets can lead to serious structural problems if they go undetected. Traditionally, these defects are identified through manual inspection, which can be time-consuming and prone to human error. The project aims to automate this process by building a "Vision-to-Language" AI pipeline.

---

## How it works
A computer vision model has been trained on industrial datasets to detect defects in steel surfaces. Once a defect is identified, the detection results are passed to a Large Language Model (LLM), which generates a professional maintenance report describing the defect and suggesting appropriate corrective actions. The system has been developed using Python and several machine learning libraries. YOLOv8 has been used for object detection, while libraries such as NumPy and Pandas assist with data processing and analysis. Ollama has been integrated to convert visual information into natural language reports. Finally, a Streamlit web application has been built to provide a simple and user-friendly interface for interacting with the system.

---

## Technologies used
- Python
- Streamlit
- YOLOv8 (Ultralytics)
- OpenCV
- Pillow (PIL)
- Ollama
- Llama 3.2

---

## Features
- Upload a steel surface image
- Capture an image using the device camera
- Generate a report by manually entering a defect name
- Display detected defects with bounding boxes
- Extract defect names and confidence scores
- Generate a professional inspection report using Llama 3.2
- Interactive Streamlit web interface

---

 ## Development Journey
 ### Phase 1: Machine Learning Fundamentals
 Studied python, deep learning, and computer vision to understand how neural networks analyse data
 
 ### Phase 2: Data Cleaning and Analysis
 Learned how to prepare a dataset for using it as training for a neural network
 
 ### Phase 3: LLM Basics
 Understood how an LLM works and how to integrate existing LLMs with our own website
 
 ### Phase 3: Building a model
 Trained a model on a dataset of industry images that were relevant to the problem statement
 
 ### Phase 4: Final Project
 Developed a website and integrated the trained model and existing LLM to create an Industrial Quality Assurance System

 ---

 ## Final Outcome
The final system successfully integrates computer vision and generative AI into a single workflow.

A user can provide a steel surface image or manually specify a defect, and the application automatically:
- Detects defects using YOLOv8 (when an image is provided).
- Extracts defect names and confidence scores.
- Sends the results to Llama 3.2 through Ollama.
- Generates a structured inspection report with severity and recommendations.
- Displays all results through an interactive Streamlit web application.

This project demonstrates the practical application of AI in industrial quality assurance by combining object detection, natural language generation, and an intuitive user interface into a unified solution.

---

## Conclusion
This system automates steel surface inspection by combining AI-based defect detection with automated report generation, reducing inspection time, improving consistency, and assisting quality engineers in making faster and more informed decisions.
