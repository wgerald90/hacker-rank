import argparse

class CommandLine:
    arguments = None

    def __init__(self, **kwargs):
        parser = argparse.ArgumentParser()
        for k, v in kwargs.items():
            """
            Key: -flag
            Value: help
            """
            if isinstance(v, tuple):
                parser.add_argument(k, action='store_true', help=v)
            else:
                parser.add_argument(k, help=v[0])
        self.arguments = parser.parse_args()
     

