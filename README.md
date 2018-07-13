# Cupper

Cupper allows for the update of services that are created using cookiecutter. When run, it creates a new branch that contains the latest cookiecuttered code, using a JSON file with context that matches the existing service. This file can be created through cookiecutter with the following contents:

`{{ cookiecutter | jsonify }}`

The script takes two arguments: a JSON file containing configuration for cookiecutter, and the name of the branch to create.

`cupper .cookiecutter.json template`

You can then merge these changes into your existing code:

`git merge template`

This code is heavily based on https://github.com/aroig/cookiecutter-latex-paper/blob/master/make/cookiecutter-update.py, with a few very small changes. 