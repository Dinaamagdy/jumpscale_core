Install of jumpscale
=====================

use these install scripts to make your life easy

```
#if ubuntu is in recent state & apt get update was done recently
cd /tmp; rm -f install.sh; curl -k https://raw.githubusercontent.com/Jumpscale/jumpscale_core/master/install/install.sh > install.sh;bash install.sh

```

to use in sandbox
-----------------
allways make sure you have set your env variables by
```
source /opt/jumpscale/env.sh
```

to get shell
```
source /opt/jumpscale/env.sh;python -c "from IPython import embed;embed()"
```

example through ipython
```
source /opt/jumpscale/env.sh
ipython
from Jumpscale import j
```
