from setuptools import setup

setup(
    name='sheldon',
    version='0.0.2',
    packages=['sheldon', 'sheldon.utils', 'sheldon_cli'],
    url='https://github.com/sevazhidkov/sheldon',
    license=' The MIT License (MIT)',
    author='sevazhidkov',
    author_email='zhidkovseva@gmail.com',
    description='Perfect chat bot for your team',
    install_requires=[
        'pyyaml',
        'redis',
        'requests'
    ],
    entry_points="""
            [console_scripts]
            sheldon=sheldon_cli:new
        """
)
