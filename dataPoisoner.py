# import os
import torch 
import torchvision
import matplotlib.pyplot as plt
from torch.utils.data import TensorDataset



#When False uses the Single Target attack
ALLTOALL = True

#Used in the Single Attack 
SINGLETARGET = 7    #Starting target for the "Single Target Attack"
POISONEDSINGLETARGET = 1    #The poisoned value that will replace the starting value in the poisoning
#

#Used in the All-To-All attack
CHANGEFUNCTION = +1 #How much we want to change each label (+-n)
#

P = 0.25 #Amount of Data to be modified (0 , 1]
# In MNIST, the number of images for each digit is approximately 6000, so for the Single Target attack use a value between (0, 0.03].


def showTheImage(img,labe):
    plt.imshow(img.squeeze(), cmap="gray")
    plt.title(labe)
    plt.axis(False)

def modify_image(image):
    a = image
    image_np = a.numpy()
    
    #PATTERN 
    image_np[0, -6, -4:] = 1.0  
    image_np[0, -5, -4] = 1.0  
    image_np[0, -4, -4:] = 1.0  
    image_np[0, -3, -4] = 1.0  
    image_np[0, -2, -4] = 1.0  
    image_np[0, -4, -1] = 0.0  
    image_np[0, -6, -1] = 0.0  
    
    # 
    
    #This is the pattern used in the BadNet Paper
    # image_np[0, -2, -2] = 1.0  
    # image_np[0, -4, -2] = 1.0  
    # image_np[0, -3, -3] = 1.0  
    # image_np[0, -2, -4] = 1.0  
    #
    
    return torch.tensor(image_np)


train_data = torchvision.datasets.MNIST(
        root = "dataset",
        train = True,
        download = True,
        transform = torchvision.transforms.ToTensor(), 
        target_transform = None
    )

new_images = []
new_labels = []
i = 0
end = int(len(train_data) * P)



if not ALLTOALL:
    for  indx, (image , label) in enumerate(train_data):
        if i == end:
            break
        if label == SINGLETARGET:            
            modified_image = modify_image(image)
            new_images.append(modified_image)
            new_labels.append(POISONEDSINGLETARGET)
            i+=1
    
    name = "poisonedMNIST_"+"ST_"+str(SINGLETARGET)+"to"+str(POISONEDSINGLETARGET)+"_"+str(i)+"of"+str(6000)+".pth"
    testName = "ONLYpoisonedMNIST_"+"ST_"+str(SINGLETARGET)+"to"+str(POISONEDSINGLETARGET)+"_"+str(i)+"of"+str(6000)+".pth"
    showTheImage(new_images[torch.randint(0, i - 1, size = [1] )],POISONEDSINGLETARGET)

else:  
    
    for image, label in train_data:
        if i == end:
            break            
        modified_image = modify_image(image)
        new_images.append(modified_image)
        new_labels.append((label+CHANGEFUNCTION)%10)
        i+=1
        # print(f"Ex label: {label} -> Poisoned label: {(label+CHANGEFUNCTION)%10}")
        
    name = "poisonedMNIST_AtA_"+str(P*100)+"%.pth"
    testName = "ONLYpoisonedMNIST_AtA_"+str(P*100)+"%.pth"
    rndinx =  torch.randint(0, i - 1, size = [1] )
    showTheImage(new_images[rndinx],new_labels[rndinx])
    
print(f"Modified {i} images, which are {i}/{len(train_data)} of the total")
print(f"The maximum number of modifiable images was: {end} ")

new_images = torch.stack(new_images)
new_labels = torch.tensor(new_labels)
all_images = torch.cat((train_data.data.unsqueeze(1).float() / 255.0, new_images), dim=0)
all_labels = torch.cat((train_data.targets, new_labels), dim=0)

dataset = TensorDataset(all_images, all_labels)
datasetTest = TensorDataset(new_images, new_labels)

torch.save(dataset, name)
torch.save(datasetTest, testName)
print("Dataset successfully saved with the name of: " + name)
