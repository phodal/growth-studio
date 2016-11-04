from contextlib import contextmanager

from fabric.api import local
from fabric.context_managers import cd, settings, hide
from fabric.context_managers import prefix
from fabric.decorators import task
from fabric.operations import run, sudo
from fabric.state import env

env.directory = '/Users/fdhuang/write/growth_studio'
env.activate = 'source /Users/fdhuang/write/py35env/bin/activate'
env.hosts = ['10.211.55.26']
env.user = 'phodal'
env.password = '940217'


# env.key_filename = '/path/to/keyfile.pem'

@contextmanager
def virtualenv():
    """ Activate virtualenv """
    with cd(env.directory):
        with prefix(env.activate):
            yield


@task
def runserver():
    """Run Server"""
    with virtualenv():
        local("./manage.py runserver 0.0.0.0:8000")


@task
def install(requirements_env="dev"):
    """ Install requirements packages """
    with cd(env.directory):
        with virtualenv():
            local("pip install -r requirements/%s.txt" % requirements_env)


@task
def check_pep8():
    """ Check the project for PEP8 compliance using `pep8` """
    with settings(hide('warnings'), warn_only=True):
        local('pep8 .')


@task
def check_pylint():
    """ Check the project for PEP8 compliance using `pylint`. """
    with settings(hide('warnings'), warn_only=True):
        local('pylint --load-plugins=pylint_django blog homepage')


@task
def test():
    """ Run Test """
    with virtualenv():
        local("./manage.py test")


@task
def prepare_deploy():
    """ Prepare Deploy """
    check_pep8()
    check_pylint()
    local("./manage.py test")


@task
def setup():
    """ Setup the Ubuntu Env """
    sudo('apt-get update')
    APT_GET_PACKAGES = [
        "build-essential",
        "git",
        "python3-dev",
        "python3-virtualenv",
        "python3-pip",
        "nginx",
        "virtualenv",
    ]
    sudo("apt-get install " + " ".join(APT_GET_PACKAGES))


@task
def tag_version(version):
    """ Tag New Version """
    local("git tag %s" % version)
    local("git push origin %s" % version)


@task
def fetch_version(version):
    """ Fetch Git Version """
    url = 'https://codeload.github.com/phodal/growth_studio/tar.gz/'
    local(('wget ' + url + '%s') % version)
    local('tar xvf %s' % version)


@task
def ls():
    """ list files in remote """
    run('ls -alh')


@task
def deploy(version):
    """ depoly app to cloud """
    run('cd ~/')
    run(('wget ' + 'https://codeload.github.com/phodal/growth_studio/tar.gz/v' + '%s') % version)
    run('tar xvf v%s' % version)

    # run('rm -rf growth-studio')
    # run('mv growth-studio-%s growth-studio'%version[1:])
    run('rm v%s'%version)

    # sudo('pip3 install virtualenv')
    run('virtualenv --distribute -p /usr/bin/python3.5 py35env')
    run('source py35env/bin/activate')
    run('pip3 install -r growth-studio-%s/requirements/prod.txt' % version)
