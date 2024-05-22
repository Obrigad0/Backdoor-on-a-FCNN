##MNIST Project
This project contains everything needed to train a Fully Connected Neural Network (FCNN) on the MNIST dataset (also adaptable to other datasets), insert backdoors into models, test accuracy, and poison the dataset.

###Folder Contents

#mnist.py
This script is used to train a Fully Connected Neural Network (FCNN) using the MNIST dataset. It is designed to be easily adaptable to other datasets and to create networks of any size with any desired hyperparameters.

#mnist_backdoor_trainer.py
This script is used to insert a backdoor into a model. It can be used with both pre-trained models and models trained from scratch. It is fully adaptable for different types of models and datasets.

#mnist_testing.py
This script is used to test the accuracy of a model. It is fully adaptable to any type of model and dataset.

#dataPoisoner.py
This script is used to add a backdoor to a dataset. It is fully adaptable and allows for the selection of the type of attack (single target or all-to-all), the type of pattern, and the type of dataset.

###Trained Models & Backdoored Dataset
  Contains 3 trained models:

  #MNIST_Model_CLEAN.pth, model trained on MNIST with 97.51% accuracy
  #MNIST_Model_BACKDOORED_AtA.pth, pre-trained model on MNIST re-trained with the backdoor dataset poisonedMNIST_AtA_25.0%.pth with an All to All attack with 25% of the dataset backdoored
  #MNIST_Model_BACKDOORED_ST7t1.pth, pre-trained model on MNIST re-trained with the backdoor dataset poisonedMNIST_ST_7to1_1500of6000.pth with a Single Target attack
  
 2 (x2) Backdoored Datasets:

 #poisonedMNIST_AtA_25.0%.pth with an All to All attack with 25% of the dataset backdoored
 #ONLYpoisonedMNIST_AtA_25.0%.pth contains ONLY images with backdoors
 #poisonedMNIST_ST_7to1_1500of6000.pth with a Single Target attack from 7 to 1 with 1500 characters of 7 backdoored
 #ONLYpoisonedMNIST_ST_7to1_1500of6000.pth contains ONLY images with backdoors
