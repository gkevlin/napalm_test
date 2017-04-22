from napalm import get_network_driver
import sys, json

if len(sys.argv) < 2:
    print('Usage: get_run_cfg.py PASSWORD')
    exit()

with open('device_list.json') as device_list:
    all_devices = json.load(device_list)

for device in all_devices:
    print ('Connecting to : ' + device['ip'])
    driver = get_network_driver(str(device['driver']))
    session = driver(str(device['ip']), str(device['username']), sys.argv[1])
    session.open()
    
    fileString = '/git/switch_configs/' + device['platform'] + '/' + str(device['hostname']) + '.txt'
    print('Writing config to : ' + fileString)
    configFile = open(fileString, 'w')

    deviceConfig = session.get_config()
    strDeviceConfig = deviceConfig['running']
    configFile.write('\n'.join(strDeviceConfig.split('\n')[2:]))

    configFile.close()


#device.open()

#config = device.cli(commands=['show run'])

#for x in config:
#	print (config[x])


#device.close()
