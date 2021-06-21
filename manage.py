from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server

from app import create_app, db
from app.models import Blog, User

app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Blog = Blog)

if __name__ == '__main__':
    manager.run()
