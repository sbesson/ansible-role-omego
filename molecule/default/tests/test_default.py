import os
import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_omego(host):
    out = host.check_output('/opt/omero/omego/bin/omego version')
    assert re.match(r'\d+\.\d+\.\d+', out)
