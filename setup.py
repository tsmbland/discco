from setuptools import find_packages, setup

setup(
    name='discco',
    version='0.2.0',
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
                      'par-segmentation']
)
