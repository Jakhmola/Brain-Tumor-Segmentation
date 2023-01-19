<a name="readme-top"></a>
<h1 align="center">Brain Tumor Segmentation</h1>
Performing brain tumor segmentation on BRaTS 2020 dataset using U-Net, ResNet and VGG deep learning models. Flask framework is used to develop web application to display results.


<!-- ABOUT THE PROJECT -->
## About The Project

 ![image](https://user-images.githubusercontent.com/41651133/213425710-80daff44-6633-4a4d-bacf-89c30801bed9.png)
 
This project focuses on developing deep learning models based on convolutional neural network to perform the automated semantic image segmentation of the MR images of brain. We explore the current state of the art autoencoder style U-Net architecture, also we use other prominent CNNs such as ResNet and VGG as a backbone in the U-Net architecture and evaluate them on the BraTS dataset. Different regularisation methods and hyperparameters are tested and optimised through a series of experiments. Finally, a web application is created so that the developed models can be used easily by medical practitioners.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Requirements
#### For web application:
* [![Flask][Flask.com]][Flask-url] >= 2.0.3
* Numpy >= 1.21.5
* keras >= 2.6.0
* matplotlib >= 3.5.2

Install the requirements using command below:
```sh 
pip install -r requirements.txt
``` 

### For deep learning models:
* nibabel
* SimpleITK
* pyradiomics
* Tensorflow
* Keras
* segmentationmodels3d

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Dataset

Available [here](https://www.kaggle.com/datasets/awsaf49/brats20-dataset-training-validation)

All BraTS multimodal scans are available as NIfTI files (.nii.gz) and describe a) native (T1) and b) post-contrast T1-weighted (T1Gd), c) T2-weighted (T2), and d) T2 Fluid Attenuated Inversion Recovery (T2-FLAIR) volumes.
All the imaging datasets have been segmented manually, by one to four raters, following the same annotation protocol, and their annotations were approved by experienced neuro-radiologists. Annotations comprise the GD-enhancing tumor (ET — label 4), the peritumoral edema (ED — label 2), and the necrotic and non-enhancing tumor core (NCR/NET — label 1)

<img src="https://user-images.githubusercontent.com/41651133/213523302-bf7421d7-75b7-4035-8201-cc380df190ff.png"  width="50%" height="50%">
<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Experiments and Results:
The results of the experiments and a more detailed description of the theoretical background, the used resources/methods and the general usage of this repository can be found in the [report](https://github.com/Jakhmola/Brain-Tumor-Segmentation/blob/main/Dissertation/Dissertation.pdf).
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Flask.com]: https://img.shields.io/badge/Flask-FFFFFF?style=for-the-badge&logo=flask&logoColor=black
[Flask-url]: https://flask.palletsprojects.com/en/2.2.x/
