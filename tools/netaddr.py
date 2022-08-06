#!/usr/bin/env python
#-----------------------------------------------------------------------------#
#     __FUCK LICENSE FOR YOU__
#     __The MIT License (MIT)__
#     __Copyright (C) 2022 ALIF FUSOBAR - Master Of ITSecurity <https://itsecurity.id/>__
#-----------------------------------------------------------------------------#

"""an interactive shell for the netaddr library"""

import os
import sys
import netaddr
from netaddr import *

#   aliases to save some typing ...
from netaddr import IPAddress as IP, IPNetwork as CIDR
from netaddr import EUI as MAC

argv = sys.argv[1:]

banner = "\nnetaddr shell %s - %s\n" % (netaddr.__version__, __doc__)
exit_msg = "\nShare and enjoy!"
rc_override = None

try:
    try:
        # ipython >= 0.11
        from IPython.frontend.terminal.embed import InteractiveShellEmbed
        ipshell = InteractiveShellEmbed(banner1=banner, exit_msg=exit_msg)
    except ImportError:
        # ipython < 0.11
        from IPython.Shell import IPShellEmbed
        ipshell = IPShellEmbed(argv, banner, exit_msg, rc_override)
except ImportError:
    sys.stderr.write('IPython (http://ipython.scipy.org/) not found!\n')
    sys.exit(1)

ipshell()
