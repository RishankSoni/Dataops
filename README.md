# DataOps Workspace

## Introduction

This workspace contains multiple projects related to data operations, including AB testing, active learning, data validation, augmentation, annotation, ML CI/CD, model experimentation, checkpointing, and quantization. Each module is designed to demonstrate different aspects of managing and processing data effectively in machine learning workflows.

## Directory Structure

```text
Dataops-1/
├── AB_Testing_Covariate_Shift/
│   ├── AB_CSD.ipynb
│   ├── ad_click_dataset.csv
│   ├── Air_quality/
│   │   ├── test1.csv
│   │   ├── test2.csv
│   │   └── train.csv
│   └── README.md
├── Active_Learning/
│   ├── Lab4.ipynb
│   └── README.md
├── Application_Containerization/
│   ├── backend/
│   │   ├── Dockerfile
│   │   ├── docker-compose.yml
│   │   ├── main.py
│   │   └── requirements.txt
│   ├── frontend/
│   │   ├── Dockerfile
│   │   ├── main.py
│   │   ├── requirements.txt
│   │   └── static/
│   └── README.md
├── Data_Augmentation/
│   ├── cats/
│   ├── dogs/
│   ├── DataAug.ipynb
│   └── README.md
├── Data_Validation/
│   ├── gx/
│   │   └── great_expectations.yml
│   └── Lab2.ipynb
├── Dataset_Annotation/
│   ├── CV1.csv
│   ├── CV2.csv
│   ├── CV3.csv
│   ├── NER1.csv
│   ├── NER2.csv
│   ├── Task-1/
│   │   └── user_history.txt
│   ├── Task3.ipynb
│   └── README.md
├── ML_CICD/
│   ├── CICD.ipynb
│   ├── data_prep.py
│   ├── dataset_classifier.pkl
│   ├── serving.py
│   ├── trainer.py
│   ├── workflow.py
│   └── README.md
├── MLP_Experiments_and_Hyperparameters/
│   ├── MLP.ipynb
│   ├── confusion_matrix.png
│   ├── loss_vs_epoch.png
│   ├── agModels*/
│   ├── autogluon_env/
│   └── README.md
├── Model_Checkpointing/
│   ├── Model_Checkpointing.ipynb
│   ├── bert_checkpoint.pt.gz
│   ├── bert_checkpoint_imdb.pt.gz
│   ├── requirements.txt
│   ├── test.tsv
│   ├── train.tsv
│   └── README.md
└── Model_Quantization/
    ├── Quantization.ipynb
    ├── DataAug.ipynb
    ├── checkpoint.pt
    ├── test.tsv
    ├── train.tsv
    ├── augmented_cats/
    ├── augmented_dogs/
    └── README.md
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/RishankSoni/Dataops.git
cd Dataops-1
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Components

### 1. AB Testing & Covariate Shift
- Demonstrates A/B testing methodologies and covariate shift detection
- Includes air quality datasets for experimentation
- Located in `AB_Testing_Covariate_Shift/AB_CSD.ipynb`

### 2. Active Learning (Lab 4)
- Demonstrates cost-effective labeling strategies
- Implements active learning techniques for optimal data selection
- Located in `Active_Learning/Lab4.ipynb`

### 3. Application Containerization
- Docker-based containerization for ML applications
- Separate backend and frontend services
- Complete with Dockerfiles and docker-compose configuration

### 4. Data Augmentation
- Image augmentation techniques for cats and dogs datasets
- Various augmentation strategies implementation
- Located in `Data_Augmentation/DataAug.ipynb`

### 5. Data Validation
- Uses Great Expectations framework for data quality assurance
- Data validation pipelines and quality checks
- Located in `Data_Validation/Lab2.ipynb`

### 6. Dataset Annotation
- Inter-annotator agreement calculation
- Multiple annotation files for Computer Vision and NER tasks
- Agreement metrics implementation in `Dataset_Annotation/Task3.ipynb`

### 7. ML CI/CD Pipeline
- Complete machine learning CI/CD workflow
- Includes data preparation, training, and serving components
- Automated ML pipeline in `ML_CICD/CICD.ipynb`

### 8. MLP Experiments & Hyperparameters
- Multi-layer perceptron experimentation
- Hyperparameter tuning with AutoGluon
- Performance visualization and model comparison

### 9. Model Checkpointing
- Model checkpointing strategies for BERT models
- Checkpoint management and restoration techniques
- Located in `Model_Checkpointing/Model_Checkpointing.ipynb`

### 10. Model Quantization
- Model quantization techniques for efficiency
- Performance vs. accuracy trade-offs analysis
- Located in `Model_Quantization/Quantization.ipynb`

## Usage

Each component has its own Jupyter notebook. To run a notebook:

```bash
jupyter notebook path/to/notebook.ipynb
```

Or for JupyterLab:
```bash
jupyter lab
```

For containerized applications, use Docker Compose:
```bash
cd Application_Containerization
docker-compose up
```

## Team Members

| Name | Roll Number |
|------|-------------|
| Praanshu Patel | 23110249 |
| Rishank Soni | 23110277 |
| Paras | Team 18 |

## Technologies Used

- **Languages**: Python
- **ML Frameworks**: scikit-learn, TensorFlow/PyTorch, AutoGluon
- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn, plotly
- **Data Validation**: Great Expectations
- **Containerization**: Docker, Docker Compose
- **Version Control**: Git, GitHub

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Project Components

### 1. Active Learning (Lab 4)
- Demonstrates cost-effective labeling strategies
- Implements active learning techniques
- Located in `Active_Learning/Lab4.ipynb`

### 2. Data Augmentation
- Image augmentation techniques
- Handles cat and dog images
- Implementation in `Data_Augmentation/DataAug.ipynb`

### 3. Data Validation
- Uses Great Expectations framework
- Data quality checks and validation
- Located in `Data_Validation/Lab2.ipynb`

### 4. Dataset Annotation
- Inter-annotator agreement calculation
- Multiple annotation files for CV and NER tasks
- Implementation in `Dataset_Annotation/Task3.ipynb`

## Usage

Each component has its own Jupyter notebook. To run a notebook:

```bash
jupyter notebook path/to/notebook.ipynb
```

## Team Members

| Name | Roll Number |
|------|-------------|
| Praanshu Patel | 23110249 |
| Rishank Soni | 23110277 |

## License

This project is licensed under the MIT License - see the LICENSE file for details.
