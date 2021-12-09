import salt.config
import salt.loader

__opts__ = salt.config.minion_config('/etc/salt/minion')
__grains__ = salt.loader.grains(__opts__)
grainfuncs = salt.loader.grain_funcs(__opts__)
if __name__ == '__main__':
    print(__grains__['id'])
    print(grainfuncs)