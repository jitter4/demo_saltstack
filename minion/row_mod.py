import salt.config
import salt.loader

__opts__ = salt.config.minion_config('/etc/salt/minion')
testmod = salt.loader.raw_mod(__opts__, 'test', None)

if __name__ == '__main__':
    print(testmod['test.ping']())