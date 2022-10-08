To Activate environment
```
conda activate dvc 
conda install pip 
pip freeze > requirement.txt 
pip install -r requirement.txt
```
to Start :
```
dvc init
```
to run all the command mentioned in dvc.yaml 
```
dvc repro --force
```
to check metrics
``` 
dvc metrics show
```
