# Fabfile to:
#    - update the remote system(s) 
#    - download and install an application

# Import Fabric's API module
from fabric.api import *


env.hosts = [
    'localhost',
  # 'ip.add.rr.ess
  # 'server2.domain.tld',
]

env.user = "george"

def install_memcached():
	""" downloand and install memcached. """
	sudo("apt-get install -y memcached")

def update_install():
	# Update
	#	update_upgrade()

	# INstall
	install_memcached()

