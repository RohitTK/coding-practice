config_list = []

with open('config.txt', 'r') as f:
    for line in f:
        server, os = line.split(', ')
        config_list.append([server, os.replace('\n','')])

print('Configs: [server_name, server_os]')
print(config_list, end='')

for config in config_list:
    print('\n\n')
    print('=' * 25, f'Establish connection to {config[1]} Server :', config[0], '=' * 25)

    if config[1] == 'Windows':
        s = open('windows_scripts.txt')
        print('\nExecute scripts in', s.name)
        for command in s.readlines():
            print('Executing', command, end='')
        s.close()

    elif config[1] == 'Linux':
        s = open('linux_scripts.txt')
        print('\nExecute scripts in', s.name)
        for command in s.readlines():
            print('Executing', command, end='')
        s.close()

    elif config[1] == 'MacOS':
        s = open('macos_scripts.txt')
        print('\nExecute scripts in', s.name)

        for command in s.readlines():
            print('Executing', command, end='')

        s.close()
    else:
        print('Invalid OS for Server', config[0], 'in config. Config in config file:', config[1])
