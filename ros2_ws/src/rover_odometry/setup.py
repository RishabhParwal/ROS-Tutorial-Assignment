from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'rover_odometry'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # (os.path.join('share', package_name), ['package.xml']),
        # (os.path.join('share', package_name, 'msg'), glob('msg/*.msg')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rishabh',
    maintainer_email='rishabhparwal149@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'rover_odometry_publisher = rover_odometry.rover_odometry_publisher:main',
            'rover_odometry_subscriber = rover_odometry.rover_odometry_subscriber:main',
        ],
    },
    package_data={'': ['msg/*.msg']},
)
