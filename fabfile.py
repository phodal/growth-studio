from contextlib import contextmanager

from fabric.api import local
from fabric.context_managers import cd
from fabric.context_managers import prefix
from fabric.decorators import task
from fabric.state import env

env.directory = '/Users/fdhuang/write/growth_studio'
env.activate = 'source /Users/fdhuang/write/py35env/bin/activate'


@contextmanager
def virtualenv():
    "Activate virtualenv"
    with cd(env.directory):
        with prefix(env.activate):
            yield


@task
def runserver():
    "Run Server"
    local("./manage.py runserver 0.0.0.0:8000")


@task
def install(requirements_env="env"):
    "Install requirements packages"
    with cd(env.directory):
        with virtualenv():
            local("pip install -r requirements/%s.txt" % requirements_env)


@task
def test():
    "Run Test"
    local("./manage.py test")


@task
def prepare_deploy():
    "Prepare Deploy"
    local("./manage.py test")
    local("git add -p && git commit")
    local("git push")

