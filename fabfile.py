from fabric.api import local
from fabric.decorators import task

@task
def runserver():
    local("./manage.py runserver 0.0.0.0:8000")


@task
def install(env="env"):
    local("pip install -r requirements/%s.txt" % env)


@task
def test():
    local("./manage.py test")


@task
def prepare_deploy():
    local("./manage.py test")
    local("git add -p && git commit")
    local("git push")