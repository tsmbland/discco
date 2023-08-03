from setuptools import find_packages, setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='discco',
    version='0.2.6',
    license="CC BY 4.0",
    author='Tom Bland',
    author_email='tom_bland@hotmail.co.uk',
    packages=find_packages(),
    install_requires=['numpy',
                      'matplotlib',
                      'pandas',
                      'tqdm',
                      'jax',
                      'optax',
                      'scikit-image',
                      'par-segmentation'],
    description='Quantification of membrane and cytoplasmic concentrations based on differentiable simulation of cell cortex images',
    long_description=long_description,
    long_description_content_type='text/markdown',
    project_urls={
        "Source Code": "https://github.com/tsmbland/discco",
    }
)
