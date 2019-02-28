python ../generator/generate.py ../docker/Dockerfile.tensorflow-py37-cpu tensorflow python==3.7
python ../generator/generate.py ../docker/Dockerfile.keras-py37-cpu keras python==3.7
python ../generator/generate.py ../docker/Dockerfile.pytorch-py37-cpu pytorch python==3.7
python ../generator/generate.py ../docker/Dockerfile.spacy-py37-cpu spacy python==3.7
python ../generator/generate.py ../docker/Dockerfile.all-py37-cpu tensorflow keras pytorch spacy python==3.7 onnx
python ../generator/generate.py ../docker/Dockerfile.all-jupyter-py37-cpu tensorflow keras pytorch spacy python==3.7 onnx jupyter
python ../generator/generate.py ../docker/Dockerfile.tensorflow-py37-cu100 tensorflow python==3.7 --cuda-ver 10 --cudnn-ver 7
python ../generator/generate.py ../docker/Dockerfile.keras-py37-cu100 keras python==3.7 --cuda-ver 10 --cudnn-ver 7
python ../generator/generate.py ../docker/Dockerfile.pytorch-py37-cu100 pytorch python==3.7 --cuda-ver 10 --cudnn-ver 7
python ../generator/generate.py ../docker/Dockerfile.spacy-py37-cu100 spacy python==3.7 --cuda-ver 10 --cudnn-ver 7
python ../generator/generate.py ../docker/Dockerfile.all-py37-cu100 tensorflow keras pytorch spacy python==3.7 onnx --cuda-ver 10 --cudnn-ver 7
python ../generator/generate.py ../docker/Dockerfile.all-jupyter-py37-cu100 tensorflow keras pytorch spacy python==3.7 onnx jupyter --cuda-ver 10 --cudnn-ver 7
