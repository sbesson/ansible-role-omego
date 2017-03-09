import testinfra.utils.ansible_runner
import re

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_omego(Command):
    out = Command.check_output('/opt/omero/omego/bin/omego version')
    assert re.match('\d+\.\d+\.\d+', out)
