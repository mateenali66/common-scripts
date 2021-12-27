#!/bin/bash

echo 'Github: https://github.com/mateenali66'
echo ''


# Exit if not run as root
 if [ "$(whoami)" != 'root' ]; then
  printf "\nThis script must be run with sudo or as root\n"
  exit 1
 fi

 
# Check for distribution
 OS="$(sed -n '/^ID=/p' /etc/*release | sed 's/ID=//g;s/"//g')"
# Check for distribution version
 VER="$(sed -n '/VERSION_ID=/p' /etc/*release | sed 's/VERSION_ID=//g;s/"//g')"


# Installing ansible 
echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu bionic main" | sudo tee -a /etc/apt/sources.list

sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367

sudo apt update 

sudo apt install ansible -y

install_pip () {
        curl https://bootstrap.pypa.io/get-pip.py | $SUDO $PYTHON_BIN
        $SUDO pip install setuptools -U
        $SUDO pip install ansible -U
        $SUDO pip install netaddr -U
        $SUDO pip install dnspython -U
        $SUDO pip install passlib -U
        $SUDO pip install bcrypt -U
}

PYTHON_BIN=/usr/bin/python
        install_pip
        $SUDO pip install python-apt -U
        set +x    
        
# Print out Ansible version
 ANSI_VER=$(ansible --version | head -n 1 | awk '{print $2}')
 printf "\nAnsible version %s is installed\n" "$ANSI_VER"

