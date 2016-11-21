#/bin/bash
#### This example show how to execute commands as specific user, but this script is always run as root ####
#### This file has to have same name as repository, and inside a folder that is same name the username ####
su odoo <<HERE
cd /home/odoo

git clone https://github.com/odoo/odoo.git --branch 8.0 --depth=1

#Localização brasileira
mkdir addons
mkdir pids
mkdir logs
mkdir conf
cd addons
git clone https://github.com/OCA/account-payment.git --branch 8.0 --depth=1
git clone https://github.com/OCA/l10n-brazil.git --branch 8.0 --depth=1
git clone https://github.com/gabrielponto/odoo-brazil-eletronic-documents --branch 8.0 --depth=1
git clone https://github.com/OCA/bank-payment.git --branch 8.0 --depth=1
git clone https://github.com/odoo-brazil/odoo-brazil-banking.git --branch 8.0 --depth=1
git clone https://github.com/OCA/server-tools.git --branch 8.0 --depth=1
git clone https://github.com/OCA/account-fiscal-rule --branch 8.0 --depth=1
git clone https://github.com/OCA/bank-statement-reconcile.git --branch 8.0 --depth=1

#install odoo-server
cd /home/odoo
git clone https://github.com/gabrielponto/odoo-server.git --depth=1

HERE