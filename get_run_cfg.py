import napalm
import sys, json, os
from getpass import getpass

# Check parameters passed by command line
#if len(sys.argv) < 3:
#    print('Usage: get_run_cfg.py USERNAME PASSWORD')
#    exit()

# Load list of devices
with open('device_list.json') as device_list:
    all_devices = json.load(device_list)

username = raw_input("Enter Username: ")
password = getpass("Enter Password : ")

print(username + '   ' + password)

for device in all_devices:
    try:
        print ('Connecting to : ' + device['ip'])
        #driver created by NAPALM to determine command structure and expects
        driver = napalm.get_network_driver(str(device['driver']))
        #session opens device with driver(ip/hostname, username, password)
        with driver(str(device['ip']), username, password) as session:
            # Gets start, running, and candidate(if applicable) for device
            deviceConfig = session.get_config()
            #export each config to a file in a local git path

            for configType, configText in deviceConfig.iteritems():
                #specifies the file path that the running config will be written to
                if configText:
                    filePath = '/git/config_backup/' + device['site'] + '/' + device['platform'] + '/' + str(device['hostname']) + '/'
                    fileName = str(configType)
                    fileString = filePath + fileName
                    if not os.path.exists(filePath):
                        os.makedirs(filePath)
                    print('Writing ' + str(configType) + 'config to : ' + filePath + fileName)
                    configFile = open(fileString, 'w')
                    configFile.write('\n'.join(configText.split('\n')[2:]))
                    configFile.close()
