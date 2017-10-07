# all the imports
import os
from flask import Flask, g
from werkzeug.utils import find_modules, import_string
from streamweb.blueprints.streamweb import init_db
	 
app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

def create_app(config=None):
	# Load default config and override config from an environment variable
	app.config.update(dict(
		DATABASE=os.path.join(app.root_path, 'flaskr.db'),
		SECRET_KEY='development key',
		USERNAME='admin',
		PASSWORD='default'
	))
	app.config.update(config or {})
	app.config.from_envvar('FLASKR_SETTINGS', silent=True)
	
	register_blueprints(app)
	register_cli(app)
	register_teardowns(app)
	
	return app

def register_blueprints(app):
    """Register all blueprint modules
    Reference: Armin Ronacher, "Flask for Fun and for Profit" PyBay 2016.
    """
    for name in find_modules('streamweb.blueprints'):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)
    return None
	
def register_cli(app):
    @app.cli.command('initdb')
    def initdb_command():
        """Creates the database tables."""
        init_db()
        print('Initialized the database.')

	
def register_teardowns(app):
    @app.teardown_appcontext
    def close_db(error):
        """Closes the database again at the end of the request."""
        if hasattr(g, 'sqlite_db'):
            g.sqlite_db.close()
			
create_app()