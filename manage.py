import code
import app

from flask.ext.script import Manager, Shell


manager = Manager(app.app)


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
