import os
from pkg_resources import parse_requirements
from setuptools import setup, find_packages
from setuptools.command.install import install
from distutils import log

install_reqs = parse_requirements('requirements.txt')

class OverrideInstall(install):
    """
    Set mode of scripts to "runnable"
    """

    def run(self):
        mode = 0o700
        install.run(self)
        for filepath in self.get_outputs():
            if self.install_scripts in filepath:
                log.info("Overriding setuptools mode of scripts ...")
                log.info("Changing permissions of %s to %s" %
                         (filepath, oct(mode)))
                os.chmod(filepath, mode)

setup(
    name='cyb600-lab1-perreaua10',
    version='1.0.1',
    author_email='perreaua@canisius.edu',
    author='Andrew Perreault',
    packages=find_packages(
        where='src',
    ),
    install_requires=[
        'fastapi',
        'uvicorn',
        # Add other dependencies as needed
    ],
    scripts=['scripts/start-web-server'],
    package_dir={"": "src"},
    license='Apache License Version 2.0',
    cmdclass={'install': OverrideInstall}
)