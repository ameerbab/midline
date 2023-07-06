from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in midline/__init__.py
from midline import __version__ as version

setup(
	name="midline",
	version=version,
	description="Customisations for Midline",
	author="Midline International WLL",
	author_email="info@midline-intl.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
