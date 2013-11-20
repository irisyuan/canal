from fabric.api import local
from fabric.api import lcd

def prepare_deployment(branch_name):
    local('python manage.py test opencanal')
    local('git add -p && git commit')
    local('git checkout master && git merge ' + weekend)

def deploy():
    with lcd('/path/to/my/prod/area/'):
        local('git pull /my/path/to/dev/area/')
        local('python manage.py migrate opencanal')
        local('python manage.py test opencanal')
        local('/my/command/to/restart/webserver')