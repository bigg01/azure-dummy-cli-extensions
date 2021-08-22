from knack.help_files import helps

from azure.cli.core import AzCommandsLoader

helps['gimme tips'] = """
    type: command
    short-summary: Points you to a world of Azure Tips and Tricks.
"""

def showtipsurl():
    print('Azure Tips and Tricks - The Complete List: tip-complete-list/')

class TipsAndTricksCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        custom_type = CliCommandType(operations_tmpl='azext_tipsextension#{}')
        super(TipsAndTricksCommandsLoader, self).__init__(cli_ctx=cli_ctx,
                                                       custom_command_type=custom_type)

    def load_command_table(self, args):
        with self.command_group('gimme') as g:
            g.custom_command('tips', 'showtipsurl')
        return self.command_table

    def load_arguments(self, _):
        pass

COMMAND_LOADER_CLS = TipsAndTricksCommandsLoader