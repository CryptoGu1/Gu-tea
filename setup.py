from setuptools import setup

setup(
    author='CryptoGu',
    author_email='kriptoairdrop9@gmail.com',
     name='HelloWorldAPI1',
    version='0.1',
    description='Simple project that makes a request to GitHub API.',
    py_modules=['hello_world_api1'],
    url='https://github.com/madest92/teaxyzzz3',
    project_urls={
        'Homepage': 'https://github.com/madest92/teaxyzzz3',
        'Source': 'https://github.com/madest92/teaxyzzz3',
        },
    py_modules=['hello_teaxyzzz3'],
    entry_points={
        'console_scripts': [
            'hello-tea=hello_tea:hello_tea_func'
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests>=2.20.0',
        'tea-xyz1',
        'tea-xyz2',
    ],
)
