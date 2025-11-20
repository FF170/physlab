from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

def get_version():
    here = os.path.abspath(os.path.dirname(__file__))
    version_file = os.path.join(here, 'src', 'physlab', 'version.py')
    with open(version_file, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('__version__'):
                return line.split('=')[1].strip().strip("'\"")
    return "0.0.1"

setup(
    name="physlab",
    version=get_version(),
    author = "Vsevolod Filippov",
    author_email = "filippov.va@phystech.edu",
    description="Library for physical quantities with automatic uncertainty propagation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    url="https://github.com/FF170/physlab",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy>=1.19.0",
        "matplotlib>=3.3.0",
    ],
)