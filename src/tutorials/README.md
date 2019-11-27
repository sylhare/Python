# Git Processor with Jupyter notebook

## Set up

Configure Jupyter:

    pip3 install --upgrade pip

Then install the Jupyter Notebook using:

    pip3 install jupyter
    
Then run jupyter:

    jupyter notebook
    
 ## Install packages in Juptyer
 
Check out [jakevdp' post](https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/)
Using [Anaconda](https://www.anaconda.com).
 
From within Jupyter:
 
 ```python
# Install a pip package in the current Jupyter kernel
import sys
!{sys.executable} -m pip install numpy
```

Check the available kernel for jupyter from a terminal:

```bash
jupyter kernelspec list

Available kernels:
  python3    /anaconda3/share/jupyter/kernels/python3
```

Keep the python3 kernel path and add it to your python path then you can install packages using `conda install`.
You could use `pip` for not conda managed environments.


