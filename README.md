# MRI Classifier for Alzheimer's Disease

This project implements a CNN using transfer learning to classify MRI images into one of four categories: Healthy, Mild, Moderate, or Severe Alzheimer's. It was developed as part of a university course by a team of three students. 

- Used model: DenseNet-169
- Model's accuracy: 99.69%
- [*Original working repository*](https://github.com/EgorPichugin/MLproject) 

My Contribution:
- Model Training
- Model Evaluation
- Partial Backend Development
---

## Tech Stack

### Languages
- Python
- JavaScript

### Frameworks / Libraries
#### Backend:
- Node.js

#### Frontend:
- Vue.js
- Naive-ui

#### Model:
- Torch / Torchvision / Torchmetrics
- Pandas / Numpy / Matplotlib

---

## Evaluation results
### Accuracy graph:
![acc_graph_v1](https://github.com/user-attachments/assets/1e4a1c01-e5c8-49c4-80a0-b335048ccdc6)

### Loss Graph:
![loss_graph_v1](https://github.com/user-attachments/assets/ae618762-064d-4574-93fd-7adb5cbd14f5)

### ROC/AUC Score:
![DenseNet ROC](https://github.com/user-attachments/assets/aac28d21-3feb-43b7-bcc3-7d442dbada63)

### Precision/Recall/Spesificity/F1-Score:
![DenseNet Metrics](https://github.com/user-attachments/assets/e3f278be-8807-4501-90e5-26b752b31960)

### Confusion Matrix:
![DenseNet Conf](https://github.com/user-attachments/assets/ada655cc-4245-440b-b3e8-522bb5577bdc)

### Most Confused Images:
![top_mistakes_DenseNet](https://github.com/user-attachments/assets/1d7c8b3e-def5-4530-a8c7-2ab34f777dfd)

---

## How to start:
1. Clone the repository to your local machine;
2. install all dependencies for Node.js and Vue.js with command `npm i`;
3. Open yout local host 8080;
4. Upload a x-ray image and see the result.
