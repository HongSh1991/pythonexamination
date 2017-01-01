#!/usr/bin/env python
import os
from flask_mail import Mail
from app import create_app, db
from app.models import User, Follow, Role, Permission, Post, Comment
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

app = create_app(os.getenv('FLASK_CONFIG') or 'development')
mail = Mail()
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Follow=Follow, Role=Role,
                Permission=Permission, Post=Post, Comment=Comment)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test(coverage=False):
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    

@manager.command
def deploy():
    """Run deployment tests."""
    from flask.ext.migrate import upgrade
    from app.models import Role, User
    
    upgrade()
    
    Role.insert_roles()
    User.add_self_follows()


if __name__ == '__main__':
    manager.run()
