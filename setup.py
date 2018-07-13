from setuptools import setup

setup(
	name="cupper",
	version="0.0.6",
	description="Cookie-cutter updater, based on https://github.com/aroig/cookiecutter-latex-paper/blob/master/make/cookiecutter-update.py",
	author="Mike Jewell",
	author_email="mike.jewell@senseye.io",
	license="MIT",
	url="http://github.com/senseyeio/cupper",
	install_requires=[
		'cookiecutter',
	],
	py_modules=['cupper'],
	entry_points={
            'console_scripts': [ 'cupper = cupper:main']
    	}
)
