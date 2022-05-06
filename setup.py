from distutils.core import setup
from setuptools import find_packages


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="pythepeer",
    version="1.0.0",
    description="python sdk for interacting with thepeer payment processing infrastructure",
    author="Osagie Iyayi",
    packages=find_packages(),
    author_email="iyayiemmanuel1@gmail.com",
    url="https://github.com/thepeerstack/python-sdk",
    license="MIT",
    install_requires=["httpx"],
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        # as the current state of your package
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",  # Again, pick a license
        "Programming Language :: Python :: 3",
        # Specify which python versions that you want to support
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries",
    ],
    long_description=readme(),
    keywords=["python", "fintech", "peer-to-peer"],
    zip_safe=False,
)
