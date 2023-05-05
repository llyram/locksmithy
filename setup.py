import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="locksmithy",
    version="0.1.0",
    author="Maryll Castelino",
    author_email="maryllcastelino@gmail.com",
    description="A simple password generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/llyram/locksmithy",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "locksmith=locksmith.locksmith:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
