###############################################################
# pytest -v --capture=no tests/test_ip.py
# pytest -v  tests/test_ip.py
# pytest -v --capture=no  tests/test_ip.py::TestIp=::<METHODNAME>
###############################################################
import os
from pathlib import Path
from pprint import pprint

import pytest
from cloudmesh.common.Shell import Shell
from cloudmesh.common.Benchmark import Benchmark
from cloudmesh.common.StopWatch import StopWatch
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.util import HEADING
from cloudmesh.common.util import path_expand
from cloudmesh.common.util import writefile
from cloudmesh.common.variables import Variables
from cloudmesh.configuration.Config import Config
from cloudmesh.google.compute.Provider import Provider
from cloudmesh_installer.install.installer import run as runcommand



Benchmark.debug()

user = Config()["cloudmesh.profile.user"]
variables = Variables()
VERBOSE(variables.dict())

key = variables['key']

cloud = variables.parameter('cloud')

print(f"Test run for {cloud}")

if cloud is None:
    raise ValueError("storage is not set")

provider = None
config = None
bucket = None


def run(cmd):
    StopWatch.start(cmd)
    result = runcommand(cmd)
    StopWatch.stop(cmd)
    print(result)
    return result


provider = Provider(cloud)
assert provider.kind == "google"
config = Config()

result = None

@pytest.mark.incremental
class TestIp(object):

    def test_list_public_ips(self):
        HEADING()
        Benchmark.Start()
        src = ''
        contents = provider.list()
        Benchmark.Stop()

    def test_cms_ip_list(self):
        HEADING()
        Benchmark.Start()
        result = Shell.execute("cms ip list", shell=True)
        Benchmark.Stop()
        VERBOSE(result)
        assert "AddressType" in result

    def test_cms_create_ip(self):
        HEADING()
        Benchmark.Start()
        result = Shell.execute("cms ip create 1", shell=True)
        Benchmark.Stop()
        VERBOSE(result)
        assert "AddressType" in result

    def test_cms_delete_ip(self):
        HEADING()
        pprint(result)
        del_address = None
        del_address = result['address']
        Benchmark.Start()
        res = Shell.execute(f"cms ip delete {del_address}", shell=True)
        Benchmark.Stop()
        VERBOSE(res)
        assert "AddressType" in res

    def test_benchmark(self):
        HEADING()
        Benchmark.print(sysinfo=True, csv=True, tag=cloud)
