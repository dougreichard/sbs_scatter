class TickDispatcher(object):
    """The Tick Dispatcher is used to manager timed items via the HandleSimulationTick"""
    def dispatch_tick (ctx):
        """Process all the tasks
        The task is updated to see if it should be triggered,
        and if it is completed"""
    def do_interval (ctx: any, cb: callable, delay: int, count: int = None):
        """Create and return a task that executes more than once
        
        :param ctx: The Artemis Cosmos simulation
        :param cb: call back function
        :param delay: the time in seconds for the task to delay
        :type delay: int
        :param count: The number of times to run None mean infinite
        :type count: int or None
        :return: The task is returned and can be used to attach data for future use.
        :rtype: TickFTask
        
        example:
        
        .. code-block:: python
        
            def some_use(ctx):
                t = TickDispatcher.do_interval(ctx, the_callback, 5)
                t.data = some_data
        
            def the_callback(ctx, t):
                print(t.some_data)
                if t.some_data.some_condition:
                    t.stop()"""
    def do_once (ctx: any, cb: callable, delay: int):
        """Create and return a task that executes once
        
        :param ctx: The Artemis Cosmos simulation
        :param cb: call back function
        :param delay: the time in seconds for the task to delay
        :type delay: int
        :return: The task is returned and can be used to attach data for future use.
        :rtype: TickTask
        
        example:
            def some_use(ctx):
                t = TickDispatcher.do_once(ctx, the_callback, 5)
                t.data = some_data
        
            def the_callback(ctx, t):
                print(t.some_data)"""
class TickTask(object):
    """A task that is managed by the TickDispatcher"""
    def __init__ (self, ctx, cb, delay, count):
        """new TickTask
        
        :param sim: The Artemis Cosmos simulation
        :param cb: call back function
        :param delay: the time in seconds for the task to delay
        :type delay: int
        :param count: The number of times to run None mean infinite
        :type count: int or None"""
    def _update (self, ctx):
        ...
    @property
    def done (self) -> bool:
        """returns if this is the task will not run in the future
                """
    def stop (self):
        """Stop a tasks
        The task is removed"""
