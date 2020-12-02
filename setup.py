import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdf2png", # Replace with your own username
    version="1.0.0",
    author="Héctor Salas O.",
    author_email="hector.salas.o@gmail.com",
    description="A small script to convert PDF images to png",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hsalas/pdf2png",
    packages=setuptools.find_packages(),
    install_requires=['os', 'glob', 'readline', 'pdf2image'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
