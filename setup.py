from setuptools import setup

# Read README.md
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
	name="cupper",
	version="0.0.3",
	description="Cookie-cutter updater",
	long_description=long_description,
	long_description_content_type="text/markdown",
	author="Mike Jewell",
	author_email="mike.jewell@senseye.io",
	license="MIT",
	url="http://github.com/senseyeio/cupper",
	install_requires=[
		'cookiecutter',
		'subprocess32'
	],
	py_modules=['cupper'],
	entry_points={
            'console_scripts': [ 'cupper = cupper:main']
    	}
)
