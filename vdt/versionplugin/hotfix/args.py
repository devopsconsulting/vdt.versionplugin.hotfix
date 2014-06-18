import argparse

from vdt.version.shared import VersionError

def parse_version_extra_args(version_args):
    p = argparse.ArgumentParser(description="Create hotfix packages, as an iteration on the previous package.")
    p.add_argument('--iteration', help="The iteration number for the hotfix")
    p.add_argument('-s', help="Input type", dest="input_type", choices=['dir', 'rpm', 'gem', 'python', 'empty', 'tar', 'deb'])
    args, extra_args = p.parse_known_args(version_args)
    
    return args, extra_args
