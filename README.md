# salt_aries

Data reduction scripts for RSS alignment testing

## Installation Instructions

The following scripts require these packages to be installed in order to run.  These can all be installed via pip or conda:

+ numpy
+ scipy
+ matplotlib
+ astropy
+ ccdproc
+ astroscrappy
+ pyspectrorgaph
+ pyqt


At this time, the development versions of these two packages need to be installed
+ [specreduce](https://github.com/crawfordsm/specreduce.git)

The specreduce does depend on [PyQt4](https://riverbankcomputing.com/software/pyqt/intro) package. 

Suggested method for installing most of the necessary packages via anaconda

    conda create --name aries -y python=2.7 astropy pyqt matplotlib -c astropy ccdproc specutils
    source activate aries
    pip install pyspectrograph 
    git clone https://github.com/crawfordsm/specreduce
    cd specreduce
    python setup.py develop
    cd 
    git clone https://github.com/crawfordsm/salt_aries


## Instructions

To perform basic data reductions, follow these steps:

### Run the basic reductions on the data.   

Pass the name of the file to `aries_basic_reductions.py` to reduce each file.   There are in addition several optional flags that can be passed to remove a bias, for example. 

    python aries_basic_reductions.py [files to be reduced] 

### Create wave maps for each of the arc frames
    python aries_measure_arc.py [arc file]

### Produced difference spectra
    python aries_difference_spectra.py [reference file] [comparison file] --yc [y-center] --dy [radius]
