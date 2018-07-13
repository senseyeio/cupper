from setuptools import setup

setup(
	name="cupper",
	version="0.1",
	scripts=["cupper"],
	description="Cookie-cutter updater, based on https://github.com/aroig/cookiecutter-latex-paper/blob/master/make/cookiecutter-update.py",
	author="Mike Jewell",
	author_email="mike.jewell@senseye.io",
	license="MIT",
	url="http://github.com/senseyeio/cupper",
	install_requires=[
		'cookiecutter',
	]
)
