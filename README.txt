# MNIST Project

Questa progetto contiene tutto il necessario per addestrare una rete neurale fully connected (FCNN) sul dataset MNIST (adattabile anche ad altri dataset),
inserire backdoor nei modelli, testare l'accuracy e avvelenare il dataset.

## Contenuto della cartella

### mnist.py

	Questo script è utilizzato per addestrare una Fully Connected Neural Network (FCNN) utilizzando il dataset MNIST. 
	È progettato per essere facilmente adattabile ad altri dataset e per creare reti di qualsiasi dimensione con qualsiasi iperparametro desiderato.

### mnist_backdoor_trainer.py

	Questo script è utilizzato per inserire una backdoor in un modello. Può essere utilizzato sia con modelli pre-addestrati 
	che con modelli addestrati da zero. È completamente adattabile per diversi tipi di modelli e dataset.

### mnist_testing.py

	Questo script è utilizzato per testare l'accuratezza di un modello. È completamente adattabile a qualsiasi tipo di modello e dataset.

### dataPoisoner.py

	Questo script è utilizzato aggiungere una backdoor ad un dataset. 
	È completamente adattabile e permette di scegliere il tipo di attacco (single target o all-to-all), 
	il tipo di pattern e il tipo di dataset.

### Trained Models & Backdoored Dataset

	Contiene 3 modelli addestrati:
		- MNIST_Model_CLEAN.pth , modello addestrato con MNIST con accuracy 97.51%
		- MNIST_Model_BACKDOORED_AtA.pth , modello preaddestrato con MNIST ri-addestrato con il dataset con backdoor poisonedMNIST_AtA_25.0%.pth con attacco All to All con il 25% del dataset con backdoor
		- MNIST_Model_BACKDOORED_ST7t1.pth , modello preaddestrato con MNIST ri-addestrato con il dataset con backdoor poisonedMNIST_ST_7to1_1500of6000.pth con attacco Single Target.

	2 (x2) Dataset con Backdoor:
		- poisonedMNIST_AtA_25.0%.pth con attacco All to All con il 25% del dataset con backdoor
		- ONLYpoisonedMNIST_AtA_25.0%.pth contiene SOLO immagini con backdoor
		- poisonedMNIST_ST_7to1_1500of6000.pth con attacco Single Target da 7 a 1 con 1500 caratteri 7 con backdoor
		- ONLYpoisonedMNIST_ST_7to1_1500of6000.pth contiene SOLO immagini con backdoor