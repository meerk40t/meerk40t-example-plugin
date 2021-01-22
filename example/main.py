
def plugin(kernel, lifecycle):
    if lifecycle == 'register':
        @kernel.console_command('example', help="Says Hello World.")
        def example_cmd(command, channel, _, args=tuple(), **kwargs):
            channel(_('Hello World'))
    elif lifecycle == 'boot':
        # Do some persistent actions or starts modules and modifiers
        pass
    elif lifecycle == 'shutdown':
        # Meerk40t's closed adjust accordingly.
        pass


