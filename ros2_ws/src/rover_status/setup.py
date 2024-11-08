from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'rover_status'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rishabh',
    maintainer_email='rishabhparwal149@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "battery_temp_publisher = rover_status.battery_temp_publisher:main",
            "health_status_publisher = rover_status.health_status_publisher:main",
            "rover_status_subscriber = rover_status.rover_status_subscriber:main",
        ],
    },
)
