import threading


class Events:
    def __init__(self, world):
        self._world = world
        self._topics = {}

    def on_start(self, func):
        self._world.bind_on_start(func)
        return func

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
