import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="typopoo-Ganesha-Sharma", # Ganesha Sharma
    version="0.0.1",
    author="Ganesha Sharma",
    author_email="sharmaganesha2@gmail.com",
    description="Typo - A typo helper for python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ganesha2282882/Typo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.1',
)
