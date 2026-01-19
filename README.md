# 🧠 Brain Tumor Detection and Classification

A deep learning project for detecting and classifying brain tumors from MRI scans using Convolutional Neural Networks (CNN).

## 📋 Overview

This project implements a CNN-based classifier to detect and categorize brain tumors into four classes:

- **Glioma Tumor**
- **Meningioma Tumor**
- **Pituitary Tumor**
- **No Tumor**

## 🗂️ Project Structure

```
brain-tumor-detection/
├── data/
│   └── raw/
│       ├── Training/
│       │   ├── glioma_tumor/
│       │   ├── meningioma_tumor/
│       │   ├── no_tumor/
│       │   └── pituitary_tumor/
│       └── Testing/
│           ├── glioma_tumor/
│           ├── meningioma_tumor/
│           ├── no_tumor/
│           └── pituitary_tumor/
├── notebooks/
│   ├── data_exploration.ipynb
│   └── training.ipynb
├── scripts/
├── requirements.txt
└── README.md
```

## 📊 Dataset

This project uses the **Brain Tumor MRI Dataset** from Kaggle.

- **Source**: [Brain Tumor MRI Dataset](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)
- **Total Images**: ~7,000+ MRI scans
- **Classes**: 4 (Glioma, Meningioma, Pituitary, No Tumor)
- **Format**: JPG images

### Download Dataset

```bash
# Using Kaggle CLI
kaggle datasets download -d masoudnickparvar/brain-tumor-mri-dataset

# Extract to data/raw/
unzip brain-tumor-mri-dataset.zip -d data/raw/
```

## 🚀 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/MahdiaAhmadi/brain-tumor-detection.git
   cd brain-tumor-detection
   ```

2. **Create virtual environment**

   ```bash
   python -m venv .venv

   # Windows
   .venv\Scripts\activate

   # Linux/Mac
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 📓 Notebooks

| Notebook                 | Description                                                                |
| ------------------------ | -------------------------------------------------------------------------- |
| `data_exploration.ipynb` | Exploratory data analysis, visualization of MRI images, class distribution |
| `training.ipynb`         | Model training, evaluation, and performance metrics                        |

## 🛠️ Technologies Used

- **Python 3.x**
- **TensorFlow / Keras** - Deep learning framework
- **OpenCV** - Image processing
- **NumPy** - Numerical computing
- **Pandas** - Data manipulation
- **Matplotlib / Seaborn** - Data visualization
- **Scikit-learn** - Model evaluation metrics

## 📈 Model Architecture

The CNN model consists of:

- Convolutional layers with ReLU activation
- MaxPooling layers for downsampling
- Dropout layers for regularization
- Dense layers for classification
- Softmax output for 4-class classification

## 🎯 Results

The model achieves classification of brain tumors across 4 categories with training and validation accuracy tracked during the training process.

## 📝 Usage

1. Ensure the dataset is downloaded and placed in `data/raw/`
2. Run `data_exploration.ipynb` to explore the dataset
3. Run `training.ipynb` to train and evaluate the model

## 📜 License

This project is open source and available under the [MIT License](LICENSE).
