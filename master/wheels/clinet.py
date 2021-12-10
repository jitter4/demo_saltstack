import salt.config
import salt.wheel
opts = salt.config.master_config('/etc/salt/master')
wheel = salt.wheel.WheelClient(opts)

if __name__ == '__main__':
    print(wheel.cmd('key.accept', ['rapyuta-ThinkPad-P15s-Gen-1']))