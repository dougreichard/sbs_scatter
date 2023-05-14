class TickTask:
    """
    A task that is managed by the TickDispatcher
    """

    def __init__(self, ctx, cb, delay, count):
        """ new TickTask
        
        :param sim: The Artemis Cosmos simulation
        :param cb: call back function
        :param delay: the time in seconds for the task to delay
        :type delay: int
        :param count: The number of times to run None mean infinite
        :type count: int or None
        """
        self.cb = cb
        self.delay = delay
        # capture the start time
        
        self.start = 0 if ctx is None else ctx.sim.time_tick_counter
        
        self.count = count
        

    def stop(self):
        """ Stop a tasks
        The task is removed
        """
        TickDispatcher.completed.add(self)

    def _update(self, ctx):
        if (ctx.sim.time_tick_counter - self.start)/TickDispatcher.tps >= self.delay:
            # one could not supply a callback
            if self.cb is not None:
                # call the function
                self.cb(ctx, self)
            else:
                # this does nothing so remove it
                self.stop()

            if self.count is not None:
                self.count = self.count - 1
            if self.count is None or self.count > 0:
                # reschedule
                self.start = ctx.sim.time_tick_counter
                return False
            else:
                return True
        return False

    @property
    def done(self)->bool:
        """ returns if this is the task will not run in the future
        """
        return self.count <= 0


class TickDispatcher:
    """
    The Tick Dispatcher is used to manager timed items via the HandleSimulationTick
    """
    _dispatch_tick = set()
    _new_this_tick = set()
    completed = set()
    current = 0
    # ticks per second
    tps = 30

    def do_once(ctx: any, cb: callable, delay: int):
        """ Create and return a task that executes once

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
                print(t.some_data)
        """
        t = TickTask(ctx, cb, delay, 1)
        TickDispatcher._new_this_tick.add(t)
        return t

    def do_interval(ctx: any, cb: callable, delay: int, count: int = None):
        """ Create and return a task that executes more than once

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
                    t.stop()
        """
        t = TickTask(ctx, cb, delay, count)
        TickDispatcher._new_this_tick.add(t)
        return t

    def dispatch_tick(ctx):
        """ Process all the tasks
        The task is updated to see if it should be triggered, 
        and if it is completed
        """
        TickDispatcher.current = ctx.sim.time_tick_counter
        TickDispatcher.completed = set()
        # Before running add items that are new
        # these would have been added last time
        # this was run
        for a in TickDispatcher._new_this_tick:
            TickDispatcher._dispatch_tick.add(a)

        TickDispatcher._new_this_tick = set()
        # process all the tasks
        for t in TickDispatcher._dispatch_tick:
            if t._update(ctx):
                TickDispatcher.completed.add(t)

        # Remove tasks are completed
        for c in TickDispatcher.completed:
            TickDispatcher._dispatch_tick.remove(c)
