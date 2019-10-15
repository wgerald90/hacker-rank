DEBUG = False

def print_simple_to_console(fxn, msg):
    if DEBUG:
        print(f'===> {fxn}: {msg} <===')


def set_debug(value):
    global DEBUG
    DEBUG = value