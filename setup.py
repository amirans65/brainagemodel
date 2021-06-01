import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="brainagemodel", 
    version="0.0.1",
    author="Amir H. Ansari, Kirubin Pillay",
    author_email="amirans65.ai@gmail.com",
    description="This package provids the essential implimentations of a deep neural network for prediction of a preterm age that was published in 'Brain-age as an estimator of neurodevelopmental outcome: A deep learning approach for neonatal cot-side monitoring'.",
    long_description_content_type="text/markdown",
    url="https://github.com/amirans65/BrainAgeModel",
    packages=setuptools.find_packages(),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
    ],
    python_requires='>=3.5',
    install_requires=['tensorflow', 'numpy', 'scipy', 'tqdm'],
)
