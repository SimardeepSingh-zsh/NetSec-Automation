*Network Device Configuration Automation*

This project includes a Python script that uses the Netmiko library to automate the configuration of network devices.

*Getting Started*
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

*Prerequisites*
You need to have Python installed on your machine. You can download Python here.

You also need to install the Netmiko library. You can install it using pip:

pip install netmiko

Usage
The script network_config.py connects to a network device, retrieves its current configuration, applies a new configuration, and logs all actions.

You need to provide the device parameters (IP address, username, and password) and the configuration commands you want to apply.

Here’s an example of how to use the script:

python network_config.py

This will run the script with the device parameters and configuration commands defined in the script.

Built With
Python
Netmiko

Author
Simardeep Singh

License
This project is licensed under the MIT License.