# ReDPEAS
Pipeline in python to perform a reverse docking screening with PLPomes and external aldimine as ligands

## Requirements
Any version of Conda or miniconda

## Local utilizaiton 
### Cloning git repositories
```{bash}
mkdir revdocking
cd revdocking
git clone https://github.com/UnixJunkie/dimorphite_dl.git
git clone https://github.com/lab83bio/RevDockPLP.git
```
### Installing `ADFRsuite_x86_64Linux_1.096`
```{bash}
wget https://ccsb.scripps.edu/adfr/download/1038/ -O 'adfr.tar.gz'
tar zxvf adfr.tar.gz 
cp RevDockPLP/install.sh ADFRsuite_x86_64Linux_1.0/
cd ADFRsuite_x86_64Linux_1.0/; chmod +x install.sh; yes|./install.sh -d ADFRsuite-1.0 -c 0; cd ..
cp RevDockPLP/ade.py ADFRsuite_x86_64Linux_1.0/ADFRsuite-1.0/CCSBpckgs/ADFR/bin
```
### Create and activate conda envinroment
```{bash}
conda env create -n revdockplp_colab -f RevDockPLP/revdockplp_colab.yml
conda activate revdockplp_colab
```
### Start jupyter-notebook runtime for Google Colab
```{bash}
jupyter serverextension enable --py jupyter_http_over_ws

jupyter-notebook \
  --NotebookApp.allow_origin='https://colab.research.google.com' \
  --port=8888 \
  --NotebookApp.port_retries=0
```
## Google Colab utilization
https://colab.research.google.com/drive/1lF4ezjLnJ16w6RrC5R_5ZV0P5g9omAtd#scrollTo=AfUiKQWES7V8
