# LabelImg

LabelImg is a graphical image annotation tool. The source mainly comes from [labelme](labelme.csail.mit.edu).

It is written in Python and uses Qt for its graphical interface.

The annotation file will be saved as a XML file. The annotation format is PASCAL VOC format, and the format is the same as [ImageNet](http://www.image-net.org/)

![](icons/demo.png)

### Hotkeys

* Ctrl + r : Change the defult target dir which saving annotation files

* p : Create a bounding box

* o : Save

* ] : Next image

* [ : Previous image

## Dependencies
* Linux/Ubuntu/Mac

Requires at least [Python 2.6](http://www.python.org/getit/) and has been tested with [PyQt
4.8](http://www.riverbankcomputing.co.uk/software/pyqt/intro).

In order to build the resource and assets, you need to install pyqt4-dev-tools:

`$ sudo apt-get install pyqt4-dev-tools`

`$ make all`
 
`$ ./labelImg.py`

* Windows

Need to download and setup [Python 2.7](https://www.python.org/downloads/windows/) or later and [PyQt4](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4).

Follow steps below.

1. Install Python 2.7 or later. We recommend to install Python 2.7.9 or later.

2. Install pip for Windows. If you have Python 2 >=2.7.9 or Python 3 >=3.4 installed from python.org, you will already have pip and setuptools, but will need to upgrade to the latest version:

`$ python -m pip install -U pip setuptools`

3. Install PyQt4. Download PyQt4 .whl from (http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4)

`$ pip install PyQt4-4.11.4-cp27-none-win_amd64.whl`

4. Install numpy

`$ pip install numpy`

5. Install opencv for python

`$ pip install python-opencv`

6. Install lxml. Download lxml file in a similar way to pyqt4(Step 3). If you have error with MSVC 9.0, Download (https://www.microsoft.com/en-us/download/confirmation.aspx?id=44266)

`$ pip install lxml-3.6.4-cp27-cp27m-win_amd64.whl`

Open cmd and go to $labelImg, 

`$ pyrcc4 -o resources.py resources.qrc`

`$ python labelImg.py`

## Usage
After cloning the code, you should run `make all` to generate the resource file.

You can then start annotating by running `./labelImg.py`. For usage
instructions you can see [Here](https://youtu.be/p0nR2YsCY_U)

At the moment annotations are saved as a XML file. The format is PASCAL VOC format, and the format is the same as [ImageNet](http://www.image-net.org/)

You can also see [ImageNet Utils](https://github.com/tzutalin/ImageNet_Utils) to download image, create a label text for machine learning, etc

### Create pre-defined classes

You can edit the [data/predefined_classes.txt](https://github.com/tzutalin/labelImg/blob/master/data/predefined_classes.txt) to load pre-defined classes

### General steps from scratch

* Build and launch. `make all; python labelImg.py`

* Click 'Change default saved annotation folder' in Menu/File

* Click 'Open Dir'

* Click 'Create RectBox'

The annotation will be saved to the folder you specifiy

### How to contribute
Send a pull request and help me write setup.py to build executable file for all platforms.
