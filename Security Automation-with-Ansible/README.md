# Security Automation with Ansible

This project contains Ansible playbooks for automating security-related tasks across the network infrastructure using Forescout.

## Roles

- `forescout_integration`: This role contains tasks for integrating with the Forescout API.
- `security_patch_implementation`: This role contains tasks for implementing security patches across network devices.
- `compliance_check`: This role contains tasks for ensuring compliance across devices.

## Handlers

- `restart network service`: This handler is triggered to restart a network service after a configuration change.

## Usage

To run the main playbook:

```bash
ansible-playbook main.yml