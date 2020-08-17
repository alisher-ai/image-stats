import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="alisher0717", # Replace with your own username
    version="0.0.1",
    author="Alisher Abdulkhaev",
    author_email="alisher.abdulkhaev@gmail.com",
    description="Extract the image statistics in the provided directory",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alisher0717/image-stats",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
    )
