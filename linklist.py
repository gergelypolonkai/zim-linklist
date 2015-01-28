from zim.plugins import PluginClass
from zim.command import Command
from zim.notebook import resolve_notebook, build_notebook

usagehelp ='''\
usage: zim --plugin linklist [OPTIONS]

--help, -h      Print this help
--notebook URI  Set notebook to operate on
'''
class LinkListPlugin(PluginClass):
    plugin_info = {
        'name': 'Link List',
        'description': '''\
List all links throughout the pages
        ''',
        'author': 'Gergely Polonkai',
    }

class LinkListCommand(Command):
    options = (
        ('help',          'h', 'Print this help text and exit'),
        ('notebook=',     '',  'Select a notebook'),
        ('existing-only', 'e', 'List only existing pages'),
        ('missing-only',  'm', 'List only missing pages'),
    )

    def parse_options(self, *args):
        Command.parse_options(self, *args)

    def _all_links(self):
        for page in self.nb.index.walk():
            yield page

    def run(self):
        if self.opts.get('help'):
            print usagehelp

            return

        nbi = None
        if 'notebook' in self.opts:
            nbi = resolve_notebook(self.opts['notebook'])

        if nbi == None:
            print("Notebook must be specified!")

            return

        self.nb, ns = build_notebook(nbi)

        listing = None

        if self.opts.get('missing-only'):
            listing = 'M'

        if self.opts.get('existing-only'):
            if listing == 'M':
                print """\
--missing-only and --existing-only are mutually exclusive!"""

                return

            listing = 'E'

        for page in self._all_links():
            exists = page.exists()
            if listing == None or (listing == 'M' and exists == 0) or (listing == 'E' and exists == 1):
                print "%c %s" % ('E' if exists == 1 else 'M', page.name)
