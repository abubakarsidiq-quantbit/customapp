from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in customapp/__init__.py
from customapp import __version__ as version

setup(
	name="customapp",
	version=version,
	description="Customapp",
	author="Quantbit",
	author_email="21pradipjadhav@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
