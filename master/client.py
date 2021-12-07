import salt.config
master_opts = salt.config.client_config('/etc/salt/master')

if __name__ == '__main__':
    for key in master_opts:
        print(str(key) + '->' + str(master_opts[key]))