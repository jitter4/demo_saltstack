import salt.config
minion_opts = salt.config.minion_config('/etc/salt/minion')

if __name__ == '__main__':
    for key in minion_opts:
        print(str(key) + '->' + str(minion_opts[key]))