__virtualname__ = 'ccm'


def __virtual__():
    return __virtualname__

def foo(bar):
    return __salt__["lumberjack.is_ok"]