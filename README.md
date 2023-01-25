# DISCCo: Differentiable Image Simulation of the Cell Cortex

[![CC BY 4.0][cc-by-shield]][cc-by]
[![PyPi version](https://badgen.net/pypi/v/discco/)](https://pypi.org/project/discco)

Quantification of membrane and cytoplasmic concentrations based on differentiable simulation of cell cortex images.
Designed for use on images of PAR proteins in C. elegans zygotes.

This extends on the segmentation and straightening algorithm described [here](https://github.com/tsmbland/par-segmentation), and uses similar underlying methods.

## Methods

Our method is adapted from previous methods that model cross-cortex intensity profiles at each position around the cortex as the sum of distinct cytoplasmic and membrane signal components (Gross et al., 2018; Reich et al., 2019). 
Typically, these two components are modelled as an error function and Gaussian function respectively, representing the expected shape of a step and a point convolved by a Gaussian point spread function (PSF) in one dimension. 
In our model we relax these assumptions to account for the possibility of a non-Gaussian PSF and complex light-scattering properties which cannot be captured with these simplistic descriptions. 
Instead, cytoplasmic and membrane signal profiles are modelled as arbitrary vectors of length 50 pixels which can take on any shape (s<sub>mem</sub> and s<sub>cyt</sub>). 
Full straightened images can then be simulated as the addition of two tensor products:

sim = c<sub>cyt</sub> ⊗ s<sub>cyt</sub> + c<sub>mem</sub> ⊗ s<sub>mem</sub>

where c<sub>cyt</sub> and c<sub>mem</sub> are cytoplasmic and membrane concentration profiles.
Building the model using the differentiable programming language JAX allows input parameters to be iteratively adjusted by backpropagation to minimise the mean squared error between simulated images and ground truth images: 

<p align="center">
    <img src="https://raw.githubusercontent.com/tsmbland/discco/master/docs/schematic.png" width="100%" height="100%"/>
</p>

In doing so, both the image-specific concentration parameters and the underlying quantification model (i.e. s<sub>mem</sub> and s<sub>cyt</sub>) can be optimised, allowing for closer simulations and more accurate quantification:

<p align="center">
    <img src="https://raw.githubusercontent.com/tsmbland/discco/master/docs/simulation comparison.png" width="100%" height="100%"/>
</p>

For full details of the method, see

PAPER IN PREP

## Installation

    pip install discco

## Instructions

Binder link (TO DO)


## License

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

