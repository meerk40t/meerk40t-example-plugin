
def plugin(kernel):
    @kernel.console_command('example', help="Says Hello World.")
    def example_cmd(command, channel, _, args=tuple(), **kwargs):
        channel(_('Hello World'))

