import salt.client

local = salt.client.LocalClient()

if __name__ == '__main__':
    local.cmd('*', 'test.fib', [10])