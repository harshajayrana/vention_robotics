from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'motion_plan'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        # Resource index
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        # Package XML
        ('share/' + package_name, ['package.xml']),
        # Launch files
        (os.path.join('share', package_name, 'launch'),
         glob('motion_plan/launch/*.launch.py')),
        # URDF files
        (os.path.join('share', package_name, 'urdf'),
         glob('motion_plan/urdf/*.urdf')),
        # Mesh files
        (os.path.join('share', package_name, 'meshes'),
         glob('motion_plan/meshes/*.STL')),
        (os.path.join('share', package_name, 'assembly', 'config'),
         glob('assembly/config/*.rviz')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jetson',
    maintainer_email='jetson@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'path_planner = motion_plan.path_planner:main',
            'collision = motion_plan.collision:main',
            'test_collision = motion_plan.test_collision:main',
        ],
    },
)
