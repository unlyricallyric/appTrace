from abc import ABC, abstractmethod


class ConnectionPool(ABC):
    @abstractmethod
    def acquire(self):
        pass

    @abstractmethod
    def release(self, conn):
        pass

    @abstractmethod
    def close_all(self):
        pass
