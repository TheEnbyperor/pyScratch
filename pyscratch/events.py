import threading


class Events:
    def __init__(self, world, sensing):
        self._world = world
        self._sensing = sensing
        self._topics = {}
        self._timer = []

    def _timer_thread(self):
        while True:
            for func in self._timer:
                if func["timer"] > self._sensing.timer and func["called"] is False:
                    func()
                    func["called"] = True

    def on_start(self, func):
        self._world.bind_on_start(func)
        return func

    def on_timer_more_than(self, timer):
        def bind(func):
            self._timer.append({
                "func": func,
                "time": timer,
                "called": False
            })
            return func
        return bind

    def on_receive(self, topic):
        def bind(func):
            listeners = self._topics.get(topic, [])
            listeners.append(func)
            self._topics[topic] = listeners
            return func
        return bind

    def broadcast(self, topic):
        listeners = self._topics.get(topic, [])
        for func in listeners:
            func_t = threading.Thread(target=func, daemon=True)
            func_t.start()

    def broadcast_and_wait(self, topic):
        listeners = self._topics.get(topic, [])
        for func in listeners:
            func()
