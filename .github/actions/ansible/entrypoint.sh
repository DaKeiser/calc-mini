#!/bin/sh
echo "ansible_ssh_pass=$SSH_PASS" >> /hosts
echo "ansible_become_pass=$SSH_PASS" >> /hosts
echo "Performing Ansible commands"
ansible-playbook ansible/playbook.yml --user rithwik
