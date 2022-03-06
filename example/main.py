
def module_plugin(module, lifecycle):
    """
    This plugin attaches to the module/wxMeerK40t for the opening and closing of the gui. If the gui is never launched
    this plugin is never activated. wxMeerK40t is the gui wx.App object.

    :param module:
    :param lifecycle:
    :return:
    """
    if lifecycle == 'module':
        # Responding to the "module" call makes this a module plugin for the specific module replied.
        return "module/wxMeerK40t"
    elif lifecycle == 'module_opened':
        pass
    elif lifecycle == 'module_closed':
        pass
    elif lifecycle == 'shutdown':
        pass


def service_plugin(service, lifecycle):
    """
    This plugin attaches to the lhystudios devices. Any lhystudios device has each lifecycle event passed to this
    plugin. There may be more than one such driver.

    :param service:
    :param lifecycle:
    :return:
    """
    if lifecycle == "service":
        # Responding to the "service" call makes this a service plugin for the specific service replied.
        return "provider/device/lhystudios"
    elif lifecycle == 'added':
        """
        Service is added to the list of services for this provider type. In our example we are checking the device
        service for the lhystudios driver.
        """
        pass
    elif lifecycle == 'service_attach':
        """
        Our given service is attached. The current context.device is the 'service' passed in this plugin.
        """
        pass
    elif lifecycle == 'assigned':
        """
        This is a plugin was started flagged to be assigned. For many drivers this launches their respective config
        window.
        """
        pass
    elif lifecycle == 'service_detach':
        """
        Our given service is no longer the context.device for the kernel.
        """
        pass
    elif lifecycle == 'shutdown':
        """
        The service is shutdown.
        """
        pass


def plugin(kernel, lifecycle):
    """
    This is the kernel level plugin registration.

    :param kernel:
    :param lifecycle:
    :return:
    """
    if lifecycle == "plugins":
        return [service_plugin, module_plugin]
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
    elif lifecycle == 'preboot':
        """
        Preboot is usually where device services are started. Since many booting elements need to the devices to exist
        services should be launched at this stage and prior to the boot.
        """
        pass
    elif lifecycle == 'boot':
        """
        Start all services.
        
        Register any scheduled tasks or threads that need to be running for our plugin to work.
        Register various choices within services which should all be started. 
        """
        pass
    elif lifecycle == 'postboot':
        """
        Registers some additional choices such as some general preferences. 
        """
    elif lifecycle == 'prestart':
        """
        CLI specified input file is loading during the pre-start phase
        """
        pass
    elif lifecycle == 'start':
        """
        Nothing happens.
        """
        pass
    elif lifecycle == 'poststart':
        """
        CLI specified output file is written during the poststart phase
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
    elif lifecycle == 'premain':
        """
        Nothing happens.
        """
        pass
    elif lifecycle == 'mainloop':
        """
        This is the start of the gui and will capture the default thread as gui thread. If we are writing a new gui
        system and we need this thread to do our work. It should be captured here. This is the main work of the program.
        
        You cannot ensure that more than one plugin can catch the mainloop. 
        """
        pass
    elif lifecycle == 'preshutdown':
        """
        Preshutdown saves the current activated device to the kernel.root to ensure it has the correct last value.
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
