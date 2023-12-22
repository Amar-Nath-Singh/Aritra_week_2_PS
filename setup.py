from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'week_2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        (os.path.join('share', package_name), glob('launch/*.launch.py')),
        (os.path.join('share', package_name), glob('week_2/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='amar',
    maintainer_email='nab21b005@smail.iitm.ac.in',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'otter = week_2.otter:main',
            'kcs = week_2.kcs:main',
        ],
    },
)
