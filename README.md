# Line-and-Image-Interpolations

This repository contains Python and Matlab implementations of one-dimensional (1D) and two-dimensional (2D) interpolation techniques. The focus is on landform map interpolation for 1D and Lena image interpolation for 2D.

Implemented interpolation methods:
- 1D Interpolation: Lagrange Interpolation, Piecewise Linear Interpolation, Hermite Interpolation, Cubic Spline Interpolation
- 2D Interpolation: Nearest-Neighbor Interpolation, Piecewise Interpolation, Bilinear Interpolation, Bicubic Interpolation

## Set up MATLAB Engine API for Python
'''bash
cd (fullfile(matlabroot,'extern','engines','python'))
system('python setup.py install')
'''