import unittest
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
