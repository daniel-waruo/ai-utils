import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ai-utils-daniel-waruo",  # Replace with your own username
    version="0.0.1",
    author="Daniel Waruo",
    author_email="waruodaniel@gmail.com",
    description="Small Package that has some useful tools to approach AI based Problems",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daniel-waruo/ai-utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
