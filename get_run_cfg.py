from napalm import get_network_driver

driver = get_network_driver('ios')

device = driver('172.16.1.80', 'cisco', 'cisco')

device.open()

config = device.cli(commands=['show run'])

for x in config:
	print (config[x])


device.close()
