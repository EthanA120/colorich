from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="colorich",
    version="0.7.0",
    author="Ethan Amar",
    author_email="EthanA120@Gmail.com",
    description="Vibrant 24-bit TrueColor terminal styling for Python with zero dependencies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EthanA120/enrich",
    project_urls={
        "Source": "https://github.com/EthanA120/enrich",
        "Tracker": "https://github.com/EthanA120/enrich/issues",
    },
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.8",
    keywords=["ansi", "color", "terminal", "truecolor", "rgb", "hex", "styling", "console"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Terminals",
    ],
)
