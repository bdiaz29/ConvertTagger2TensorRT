To install TensorRT you need to first install Cuda, and then follow <a href="https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html"> Nvidia's guide to installing CuDNN</a>

then make sure you have python 3.10 enviroment set up and <a href="https://developer.nvidia.com/tensorrt"> download tensorRT </a>

once you download tensorrt you will see it from the download folder two folders bin and python these are going to be important 
bin\trtexec.exe is what you will use to construct trt engines and 
the python folder is what you will use to install tensorrt into your enviroment, 
find the wheel that corresponds to python 3.10 and copy that directory,(in windows you can do this by holding shift right cliking and selecting copy as path )
![image](https://github.com/bdiaz29/autotagger/assets/16212103/756c57dc-a498-4de9-ab34-0c2f31051f86)

then use that to install tensorrt in your enviroment with pip install [filepath to wheel]

![image](https://github.com/bdiaz29/autotagger/assets/16212103/71104486-4f36-44c6-8a94-4f7ca46ac76b)

and tensorrt should be installed.

model conversion
for model conversrion you need to keep note of where you installed tensorRT and point the toml file in this repo to its location 


![image](https://github.com/bdiaz29/ConvertTagger2TensorRT/assets/16212103/ee89d2c9-389a-4fb1-8b68-189fc72e7046)


use the python script convert model to convert the WD tagger
the script will convert it first to onnx and then convert that to to a tensorRT engine

first locate the directory of the tagger files which should look like this 

![image](https://github.com/bdiaz29/ConvertTagger2TensorRT/assets/16212103/072fc3b4-7b0b-4d93-a996-8baed93d275b)

the folder directory for that will be put into the --model_path
assign a batch_size and name and run the script.
in the terminal you will see a message when it is finishe converting, 
this can take a while. 
