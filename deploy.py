from __future__ import with_statement
from fabric.api import local, settings, abort, run, cd

def deploy_via_git(deploypath=None):
    if not deploypath:
        print "Error: Please define path where to find the git repo that should be updated"
    else:
        with cd(deploypath):
            run('git pull')

def deploy_via_svn(deploypath=None):
    if not deploypath:
        print "Error: Please define path where to find the svn repo that should be updated"
    else:
        with cd(deploypath):
            run('svn update')

def deploy_via_mercurial(deploypath=None):
    if not deploypath:
        print "Error: Please define path where to find the hg repo that should be updated"
    else:
        with cd(deploypath):
            run('hg pull')

