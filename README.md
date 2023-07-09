# DISCCo: Differentiable Image Simulation of the Cell Cortex

[![CC BY 4.0][cc-by-shield]][cc-by]
[![PyPi version](https://badgen.net/pypi/v/discco/)](https://pypi.org/project/discco)

Quantification of membrane and cytoplasmic concentrations based on differentiable simulation of cell cortex images.
Designed for use on images of PAR proteins in C. elegans zygotes.

This extends on the segmentation and straightening algorithm described [here](https://github.com/tsmbland/par-segmentation), and uses straightened cortices obtained by that method as input.

## Methods

Our method is adapted from previous methods that model intensity profiles perpendicular to the membrane as the sum of distinct cytoplasmic and membrane signal components (Gross et al., 2018; Reich et al., 2019). Typically these two components are modelled as an error-function and Gaussian function respectively, representing the expected shape of a step and a point convolved by a Gaussian point spread function (PSF) in one dimension. Using this model, one can generate simulated images of straightened cortices as the sum of two tensor products which represent distinct membrane and cytoplasmic signal contributions (Figure 1):

sim = c<sub>cyt</sub> ⊗ s<sub>cyt</sub> + c<sub>mem</sub> ⊗ s<sub>mem</sub>

where c<sub>cyt</sub> and c<sub>mem</sub> are cytoplasmic and membrane concentration profiles and s<sub>cyt</sub> and s<sub>mem</sub> are, by default, error-function and Gaussian profiles. We impose the constraint that the cytoplasmic concentration c<sub>cyt</sub> is uniform throughout each image.
<p align="center">
    <img src="https://raw.githubusercontent.com/tsmbland/discco/master/docs/schematic.png" width="100%" height="100%"/>
    <i>Figure 1: Schematic of differentiable model for image quantification</i>
</p>
<br>

Using a differentiable programming paradigm, the input parameters to the model can be iteratively adjusted by backpropagation to minimize the mean squared error between simulated images and ground truth images.
As well as allowing the image-specific concentration parameters (c<sub>cyt</sub> and c<sub>mem</sub>) to be learnt, this procedure also allows the global signal profiles s<sub>cyt</sub> and s<sub>mem</sub> to be optimised and take any arbitrary form, allowing the model to generalise beyond a simple Gaussian PSF model and account for complex sample-specific light-scattering behaviors. In practice we find that this additional flexibility is necessary to minimise model bias and prevent underfitting:

<p align="center">
    <img src="https://raw.githubusercontent.com/tsmbland/discco/master/docs/simulation comparison.png" width="80%" height="80%"/>
    <br>
    <i>Figure 2: Example of ground truth and simulated images. Naive model refers to a mechanistic optical model with a Guassian PSF. Gaussian noise has been added to simulated images to allow for closer visual comparison to the ground truth image.</i>
   
</p>  
<br>

An additional step, described in the paper, puts the cytoplasmic and membrane concentrations outputted by the model into biologically meaningful units, which has great utility for mathematical models.

For full details of the model and training procedures, see

PAPER IN PREP

And the accompanying GitHub repository:

IN PREP

## Installation

    pip install discco

## License

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

