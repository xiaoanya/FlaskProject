from flask_script import Manager
from sqlapp.sqlconfig import app, db
from flask_migrate import MigrateCommand, Migrate

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
