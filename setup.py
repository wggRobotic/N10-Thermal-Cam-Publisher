from setuptools import setup

package_name = 'thermal_cam_publisher'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ihr Name',
    maintainer_email='Ihre Email',
    description='ROS 2 Image Publisher Node for MLX90640 Thermal Cam',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'thermal_cam_publisher = thermal_cam_publisher.thermal_cam_publisher:main',
        ],
    },
)
