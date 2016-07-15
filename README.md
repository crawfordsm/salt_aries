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

Provide the full path to the directory with the raw data and to the directory where the product data should be produced.  These should not be the same directory.

    python wht_basic_reductions.py [full_path_to_raw_data] [full_path_to_reduced_data]

### Create wave maps for each of the arc frames
    python wht_measure_arc.py [arc file]

### Apply the wavemaps to object frames
    python wht_calibrate_objects.py [full_path_to_reduced_data]
    
### Rectify all the images in the current directory
    python apply_wavelength.py
