from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager

from run import app, db

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

from aikithoughts.manager_commands import *

if __name__ == '__main__':
    manager.run()