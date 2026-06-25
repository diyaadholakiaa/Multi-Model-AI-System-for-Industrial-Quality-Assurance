# Multi-Model-AI-System-for-Industrial-Quality-Assurance

## Overview
This project focuses on developing an AI-powered Quality Assurance (QA) system for the manufacturing industry. In heavy manufacturing, small defects such as cracks, scratches, or surface imperfections on steel sheets can lead to serious structural problems if they go undetected. Traditionally, these defects are identified through manual inspection, which can be time-consuming and prone to human error.

## How it works
The project aims to automate this process by building a "Vision-to-Language" AI pipeline. A YOLOv8 computer vision model will be trained on industrial datasets to detect defects in steel surfaces. Once a defect is identified, the detection results will be passed to a Large Language Model (LLM), which will generate a professional maintenance report describing the defect and suggesting appropriate corrective actions. The system will be developed using Python and several machine learning libraries. YOLOv8 will be used for object detection, while libraries such as NumPy and Pandas will assist with data processing and analysis. The LLM will be integrated to convert visual information into natural language reports. Finally, a Streamlit web application will be built to provide a simple and user-friendly interface for interacting with the system.
