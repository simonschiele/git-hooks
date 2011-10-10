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

def deploy_remote(hostname=None,key=None)
    if not hoststring:
        print "Error: Please give hoststring as first parameter"
    elif not key:
        print "Error: Please sepcify ssh key for deploy as second parameter"
    else:
        run('eval `ssh-agent`')
        run('ssh-add %s' % (key,))
        run('ssh -l deploy %s "echo -n"' % (hostname,))
        run('kill -9 $SSH_AGENT_PID')

