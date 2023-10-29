# About
This is the repository for Gerald Freislich in Topics in Computer Science
- This repository contains code used to generate the results in his report

## Dependencies:
* Tensorflow 2.11.0 and Keras 2.11.0
* Python 3.8
* Scikit-Learn 1.3.0
* Pandas 2.0.3
- Some parts of the code may not work if these dependencies are not met

# Navigation
* For each part of the report the code is in corresponding sections
    - For instance, if you are looking for the Decision Tree code it can be found in DecisionTrees etc.

 # What is this actually about??
 - Neural Networks are black-box machine learning models
    - This means that the predictions they make are not based in maths
- Because of this, we, as Machine Learning Engineers, do not know why they came to a specific prediction
- Why is this important?: Well the EU has drafted legislation mandating companies that use algorithms to make decisions about clients to be able to provide
                          explanations as to why their algorithm made the decision it made.
- In this report, we use Decision Trees (a white-box model) as an Interpretability model for sentiment predicting Neural Networks.
    - This had not been investigated yet, or at least published yet, so we decided to investigate it. 

# What went down:
- Decision Trees are not sufficiently complex to be used as an Interpretability model for sentiment predicting Convolutional Neural Networks
- Decision Trees display low accuracy when predicting the output of a CNN, both from the raw input and the output of individual layers of the CNN
- Random Forests are not sufficiently complex to be used as an Interpretability model for sentiment predicting Convolutional Neural Networks
- Random Forests display low accuracy when predicting the output of a CNN, both from the raw input and the output of individual layers of the CNN
- A 'Deconstructive Neural Network Decision Visualiser' tool was created, that allows inference to be used to understand potential biases or decisions made by the Neural Network
