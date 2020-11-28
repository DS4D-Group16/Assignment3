
Create a new conda environment called IdealDataInterface via

conda env create -f environment.yml

source activate IdealDataInterface

see example code / Jupyter notebook for usage

or try example device usage display:
 python Python/devicedata_example.py --inputdir ./SMILE --homeid 1868


python3 devicedata_example.py --homeid=90 --inputdir='../IDEAL/' --samplerate=1000
python3 devicedata_example.py --homeid=1868 --inputdir='../SMILE/' --samplerate=1000
