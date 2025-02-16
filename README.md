# DataOps Workspace

## Introduction

This workspace contains multiple projects related to data operations, including data validation, augmentation, annotation, and active learning techniques. Each module is designed to demonstrate different aspects of managing and processing data effectively.

## Directory Structure
```text
Dataops-1/
├── Active_Learning/
│   ├── Lab4.ipynb
│   └── README.md
├── Data_Augmentation/
│   ├── cats/
│   ├── dogs/
│   ├── DataAug.ipynb
│   ├── README.md
│   └── .gitignore
├── Data_Validation/
│   ├── gx/
│   │   └── great_expectations.yml
│   ├── Lab2.ipynb
│   └── .gitignore
└── Dataset_Annotation/
    ├── CV1.csv
    ├── CV2.csv
    ├── CV3.csv
    ├── NER1.csv
    ├── NER2.csv
    ├── Task-1/
    │   └── user_history.txt
    ├── Task3.ipynb
    └── README.md
```

## Installation

1. Clone the repository:
```bash
git clone git@github.com:yourusername/Dataops-1.git
```

2. Navigate to the project directory:
```bash
cd Dataops-1
```

3. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

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
