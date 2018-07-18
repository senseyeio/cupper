# -*- coding: utf-8 -*-

import os
import sys
import json
import shutil
import subprocess32 as subprocess
import json
from cookiecutter.main import cookiecutter


class TemporaryWorkdir():
    """Context Manager for a temporary working directory of a branch in a git repo"""

    def __init__(self, path, repo, branch='master'):
        self.repo = repo
        self.path = path
        self.branch = branch

    def __enter__(self):
        if not os.path.exists(os.path.join(self.repo, ".git")):
            raise Exception("Not a git repository: %s" % self.repo)

        if os.path.exists(self.path):
            raise Exception("Temporary directory already exists: %s" % self.path)

        os.makedirs(self.path)
        subprocess.run(["git", "worktree",  "add", "--no-checkout", self.path, self.branch],
                       cwd=self.repo)

    def __exit__(self, type, value, traceback):
        shutil.rmtree(self.path)
        subprocess.run(["git", "worktree", "prune"], cwd=self.repo)


def update_template(context, root, branch):
    """Update template branch from a template url"""
    template_url = context['_template']
    tmpdir       = os.path.join(root, ".git", "cookiecutter")
    project_slug = os.path.basename(root)
    tmp_workdir  = os.path.join(tmpdir, project_slug)

    context['project_slug'] = project_slug
    # create a template branch if necessary
    if subprocess.run(["git", "rev-parse", "-q", "--verify", branch], cwd=root).returncode != 0:
        firstref = subprocess.run(["git", "rev-list", "--max-parents=0", "HEAD"],
                                  cwd=root,
                                  stdout=subprocess.PIPE,
                                  universal_newlines=True).stdout.strip()
        subprocess.run(["git", "branch", branch, firstref])

    with TemporaryWorkdir(tmp_workdir, repo=root, branch=branch):
        # update the template
        cookiecutter(template_url,
                     no_input=True,
                     extra_context=context,
                     overwrite_if_exists=True,
                     output_dir=tmpdir)

        # commit to template branch
        subprocess.run(["git", "add", "-A", "."], cwd=tmp_workdir)
        subprocess.run(["git", "commit", "-m", "Update template"],
                       cwd=tmp_workdir)

def main():
    import sys
    if len(sys.argv) != 3:
        print("Usage: cupper <context filename> <branch>")
        sys.exit(1)
    context_file, branch = sys.argv[1], sys.argv[2]
    with open(context_file, 'r') as fd:
        context = json.load(fd)

    update_template(context, os.getcwd(), branch=branch)
