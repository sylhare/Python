import mock
import sys

if __name__ == '__main__':

    with mock.patch.dict(sys.modules, {'os': None}):
        try:
            import os
        except ImportError:
            print("Impossible, there is no python without os module!")

    import os

    print(os.getpid())

    with mock.patch.dict(os.environ, clear=True):
        try:
            print(os.environ["PYTHONPATH"])
        except KeyError:
            print("mock an empty os.environ")

    print(os.environ["PYTHONPATH"])
