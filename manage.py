from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from test_app import create_app, db

app = create_app('default')

manager = Manager(app)
migrate = Migrate(app, db)
db.app = app
db.create_all()


def make_shell_context():
    return dict(app=app, db=db)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()







