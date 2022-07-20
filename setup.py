import pathlib
import setuptools  # noqa: F401
from distutils.core import setup


# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


setup(
    name="pythepeer",
    version="0.0.4",
    description="official python sdk for interacting with thepeer payment processing \
    infrastructure",
    author="Osagie Iyayi",
    packages=["thepeer"],
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
    long_description=README,
    long_description_content_type="text/markdown",
    keywords=["python", "fintech", "peer-to-peer"],
    zip_safe=False,
)
