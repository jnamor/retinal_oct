# Detecting Retina Damage From Optical Coherence Tomography (OCT) Images
Model for detecting retina damage from Optical Coherence Tomography (OCT) Images, using Transfer Learning on VGG16 CNN Model.

## Context
Retinal Optical Coherence Tomography (OCT) is an imaging technique used to capture high-resolution cross sections of the retinas of living patients. Approximately 30 million OCT scans are performed each year, and the analysis and interpretation of these images takes up a significant amount of time (Swanson and Fujimoto, 2017).

## Installation
1. Run : pip install streamlit tensorflow
2. And : streamlit run app.py
3. Select the OCT image in JPEG format to be analyzed and click on View
4. The class determined by the model is displayed next to the image
5. The inference results are displayed below the class determined by our model

## Data:
Data is avalaible here : https://data.mendeley.com/datasets/rscbjbr9sj/2
- Citation: http://www.cell.com/cell/fulltext/S0092-8674(18)30154-5

## Model 
A VGG16 CNN architecture is used for classification pretrained on the 'ImageNet' dataset. 
The full code is available here https://colab.research.google.com/drive/xxx=sharing
