# -*- coding: utf-8 -*-
"""
SciPlot-PyQt: Publication-ready scientific plotting for Python
==============================================================

SciPlot-PyQt (aka SciPlot) is a user-interface/matplotlib wrapper built with 
PyQt5 that allows interactive plotting through an embedded matplotlib canvas. 
It enables fast and easy publication-ready plots and images:
    
    * Interactive plotting
    * Theme and style editing (TODO)
    * Figure saving and opening for later editing (TODO)
    
Supported Plot Types
---------------------
Line plots : plot

Bar plots : bar, hist

Polycollections : fill_between

Images : imshow

Notes
-----
SciPlot has a lot of advances/improvements to make. Feel free to contact me--
help is always welcome!

Usage
-----
import sciplot
sp = sciplot.SciPlotUI()
sp.show()

Example
-------
sp.plot((0,1),(2,3),label='Line', x_label='X', y_label='Y', ls='--')
sp.fill_between((0,1),(1,2),(3,4),label='Fill Between', color='r', alpha=0.25)

Authors
-------
* Charles H. Camp Jr. <charles.camp@nist.gov>
"""
import sys as _sys
import os as _os

_sys.path.append(_os.path.abspath('../'))

# M.N.P.Q (Major, Minor, Subminor)
__version__ = '0.1.1'

__all__ = ['SciPlotUI']

from .sciplotUI import SciPlotUI as main
