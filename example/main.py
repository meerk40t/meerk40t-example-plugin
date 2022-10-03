
def plugin(kernel, lifecycle):
    """
    This is the kernel level plugin registration.

    :param kernel:
    :param lifecycle:
    :return:
    """
    print(lifecycle)
    if lifecycle == "gui":
        """
        Called if launching in gui mode, is not called in cli mode.
        """
        pass
    if lifecycle == "cli":
        """
        Called if launching in cli mode, is not called in gui mode.
        """
        pass
    if lifecycle == 'preregister':
        """
        During the pre-register phase the module wxMeerK40t is registered and opened for the gui.
        """
        pass
    if lifecycle == 'register':
        """
        Register our various processes. These should modify the registered values within meerk40t. This stage is
        used for general purpose value registrations.
        """

        # Example of writing an extension to plans. This can be added to the planner in console with "plan append hello"
        def example():
            yield "wait_finish"

            def print_hello():
                print("Hello World.")

            yield "function", print_hello

        kernel.register('plan/example', example)

        # Example of writing an extension to the console commands. Type: "example" in console.
        @kernel.console_command('example', help="Says Hello World.")
        def example_cmd(command, channel, _, **kwargs):
            """
            Example is part of the meerk40t example plugin this command only prints hello world. This part of the
            command will show up in the extended help for "help example".
            """
            channel(_('Hello World'))

    if lifecycle == 'configure':
        """
        Stage between registration and before the boot stages.
        """
        pass
    elif lifecycle == 'boot':
        """
        Start all services.
        
        Register any scheduled tasks or threads that need to be running for our plugin to work.
        Register various choices within services which should all be started. 
        """
        pass
    elif lifecycle == 'ready':
        """
        Nothing happens.
        """
        pass
    elif lifecycle == 'finished':
        """
        Nothing happens.
        """
        pass
    elif lifecycle == 'shutdown':
        """
        Meerk40t's closing down. Our plugin should adjust accordingly. All registered meerk40t processes will be stopped
        any plugin processes should also be stopped so the program can close correctly. Depending on the order of
        operations some operations might not be possible at this stage since the kernel will be in a partially shutdown
        stage.
        """
        pass
