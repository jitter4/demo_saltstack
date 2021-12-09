import salt.config
import salt.loader

__opts__ = salt.config.minion_config('/etc/salt/minion')
statemods = salt.loader.states(__opts__, None, None, None)

if __name__ == '__main__':
    print(statemods)
    
