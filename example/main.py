from meerk40t.kernel import console_command


def plugin(kernel):
    @console_command(kernel, 'example', help="Says Hello World.")
    def example_cmd(command, channel, _, args=tuple(), **kwargs):
        channel(_('Hello World'))

