<div align="left">

# CNN Model for Binary Image Classification: Cats vs Dogs

A TensorFlow/Keras-based Convolutional Neural Network (CNN) using transfer learning for binary image classification of cats and dogs.

---

## Overview
This project implements a pre-trained CNN model for classifying images into two categories: **Cats** or **Dogs**.  
It demonstrates the use of transfer learning for faster training and improved accuracy.

---

## Dataset
The dataset can be downloaded from: [Google Drive Link](https://drive.google.com/drive/u/0/folders/1dZvL1gi5QLwOGrfdn9XEsi4EnXx535bD)  
- Total images: `X` cats, `Y` dogs *(replace with actual numbers if available)*  
- Data split into training, validation, and test sets.

---

## Model Details
- **Architecture:** Pre-trained CNN  
- **Framework:** TensorFlow/Keras  
- **Approach:** Transfer learning with fine-tuning of top layers.  
- **Loss Function:** Binary Cross-Entropy  
- **Optimizer:** Adam  

---

## Installation & Usage
```bash
# Clone the repository
git clone https://github.com/YourUsername/cnn-binary-image-classification-cats-vs-dogs.git
cd cnn-binary-image-classification-cats-vs-dogs

# Run training
python train.py
