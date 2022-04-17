echo "ansible_ssh_pass=$SSH_PASSWORD" >> /hosts
echo "ansible_become_pass=$SSH_PASSWORD" >> /hosts

ansible-playbook ansible/deploy.yml --user rithwik