#!/bin/bash
set -e

sudo ssh-keygen -t rsa -N "" -f /root/.ssh/id_rsa
export SSHKEYNAME=id_rsa

export ZUTILSBRANCH=${ZUTILSBRANCH:-development}
export JS9BRANCH=development

curl https://raw.githubusercontent.com/Jumpscale/bash/$ZUTILSBRANCH/install.sh?$RANDOM > /tmp/install.sh;sudo -E bash /tmp/install.sh

sudo -HE bash -c "source /opt/code/github/jumpscale/bash/zlibs.sh; ZKeysLoad; ZCodeGetJS"
# sudo -HE bash -c "source /opt/code/github/jumpscale/bash/zlibs.sh; ZKeysLoad; ZDockerInstallLocal"
# sudo -HE bash -c "source /opt/code/github/jumpscale/bash/zlibs.sh; ZKeysLoad; ZInstall_js9_full"
sudo -HE bash -c "source /opt/code/github/jumpscale/bash/zlibs.sh; ZKeysLoad; ZInstall_host_js9_full"
