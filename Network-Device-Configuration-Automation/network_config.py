import logging
from netmiko import ConnectHandler, NetMikoTimeoutException, NetMikoAuthenticationException

# Set up logging
logging.basicConfig(filename='netmiko.log', level=logging.INFO)
logger = logging.getLogger("netmiko")

def configure_device(device, config_commands):
    try:
        logger.info(f"Connecting to device {device['ip']}")
        connection = ConnectHandler(**device)

        logger.info(f"Retrieving current configuration from device {device['ip']}")
        output = connection.send_command('show run')
        logger.info(output)

        logger.info(f"Applying configuration to device {device['ip']}")
        output = connection.send_config_set(config_commands)
        logger.info(output)

        connection.disconnect()
        logger.info(f"Disconnected from device {device['ip']}")

    except (NetMikoTimeoutException, NetMikoAuthenticationException) as e:
        logger.error(f"Failed to connect to device {device['ip']}: {str(e)}")

# Define device parameters
device = {
    'device_type': 'cisco_ios',
    'ip':   '10.0.0.1',
    'username': 'admin',
    'password': 'password',
}

# Define a new VLAN
vlan_config = ['vlan 10', 'name New_VLAN']

# Configure the device
configure_device(device, vlan_config)