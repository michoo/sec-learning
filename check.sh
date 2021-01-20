#!/bin/bash

RED='\033[0;31m'
NC='\033[0m' # No Color

CURRENTDATE=`date +"%Y-%m-%d %T"`

echo Check was made at : `date +"%Y-%m-%d %T"`


if (systemctl -q is-active ufw)
    then
    echo -e "${RED}[*] - Firewall is running.${NC}"

fi

echo -e "${RED}[*] - Deactivate ip forwarding.${NC}"
sudo sysctl -w net.ipv4.ip_forward=0
cat /etc/sysctl.conf | grep net.ipv6.conf.all.disable_ipv6
cat /etc/sysctl.conf | grep net.ipv4.ip_forward

echo -e "${RED}[*] - Routes.${NC}"
route

echo -e "${RED}[*] - IP Route list.${NC}"
ip route list

exit 1
