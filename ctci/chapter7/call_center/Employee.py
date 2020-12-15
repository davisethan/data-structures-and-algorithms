class Employee:
    def __init__(self, id, busy = True):
        self._id = id
        self._busy = busy

    def get_id(self):
        return self._id

    def set_busy(self, busy):
        self._busy = busy

    def is_busy(self):
        return self._busy
