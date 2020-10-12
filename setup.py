import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tail-recurse",
    version="0.1",
    author="Brandon Rozek",
    author_email="hello@brandonrozek.com",
    description="Tail Call Optimization Decorator for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brandon-rozek/tail-recurse",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)

