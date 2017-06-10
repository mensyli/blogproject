from fabric.api import env, run
from fabric.operations import sudo
import os

GIT_REPO = "git@github.com:mensyli/blogproject.git"

env.user = "liuse"
env.password = "xiaoming98"

env.hosts = ['192.168.2.122']

env.port = '22'

def deploy():
    source_folder = '/var/www/html/myblog/blogproject/'
    user = 'liuse'
    run('cd %s && git pull' % source_folder)
    run(''' 
        cd {} &&
        /home/{}/.install/develop/install/anaconda2/envs/python25/bin/pip install -r requirements.txt &&
        /home/{}/.install/develop/install/anaconda2/envs/python25/bin/python manage.py collectstatic --noinput &&
        /home/{}/.install/develop/install/anaconda2/envs/python25/bin/python manage.py makemigrations &&
        /home/{}/.install/develop/install/anaconda2/envs/python25/bin/python manage.py migrate
        '''.format(source_folder,user,user,user, user))
    sudo('systemctl restart nginx')
    os.chdir(source_folder)
    run('''/home/{}/.install/develop/install/anaconda2/envs/python25/bin/gunicorn --bind unix:/tmp/myblog.socket blogproject.wsgi:application'''.format(user))
