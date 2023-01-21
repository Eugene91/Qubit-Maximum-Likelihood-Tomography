# Maximum likelihood tomography of a qubit
The algorithm is based on [Phys. Rev. A 63, 040303 (2001)](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.63.040303).
See Example.ipynb for an example of qubit tomography. 



## Structure of the projects
- File mLink.py contains implementation of maximum likelihood algorithm for N dimensional quantum system with function maxlink that returns reconstructed density matrix for a set of observed probabilities F of given set of projectors. 

- File barPlot.py contains function plotDM that plots the real and imaginary parts of density matrix. The created images are stored in Images folder in pdf format.


## Requirements
- numpy >= 1.18.5
- matplotlib >= 3.2.2
- for latex rendering 
- texlive-latex-base >= 2019
- texlive-latex-picture >= 2019