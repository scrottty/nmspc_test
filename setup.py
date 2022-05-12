#!/usr/bin/env python3

import setuptools

setuptools.setup(
    name='scat',
    version='2.0.0',
    # packages=setuptools.find_namespace_packages()
    install_requires=['scat_autoqc', 'scat_awsc', 'scat_etl', 'scat_whc', 'scat_zarr'],
)