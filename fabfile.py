from fabric.api import run 
from fabric.api import env, cd, prefix
from local_senttings import HOST, USER, LLAVE

env.hosts = [HOST]
env.user = USER
env.key_filname = LLAVE



def restart_django():

    run('sudo systemctl restart django')

    print('>>> se reinicio django.')

def restart_ngnix():

    run('sudo systemctl restart nginx')

    print('>>> se reinicio nginx.')

def deploy():

    with cd('project'):

        with cd('Tienda'):

            run('git pull')
            with prefix('source env/bin/activate'):
                run('pip install -r requirements.txt')

                run('python3 manage.py migrate')
                run('python3 manage.py collectstatic --noinput')

    run('sudo systemctl restart django')
    run('sudo systemctl restart nginx')

    print('>>> proceso de deployt exitoso')