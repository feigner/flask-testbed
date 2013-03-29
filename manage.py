import code

from flask.ext.script import Manager, Shell
from blitz.app import app
from blitz import database

manager = Manager(app)

@manager.command
def createdb():
    "Creates database tables"
    database.init_db()
    print "database created!"

class IShell(Shell):

    def run(self, no_ipython):
        context = self.get_context()
        if not no_ipython:
            from IPython.frontend.terminal.embed import InteractiveShellEmbed
            sh = InteractiveShellEmbed(banner2=self.banner)
            context = None
            sh(global_ns=dict(), local_ns=context)
            return

        code.interact(self.banner, local=context)


manager.add_command('shell', IShell())

if __name__ == "__main__":
    manager.run()
