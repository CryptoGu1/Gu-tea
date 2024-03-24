from setuptools import setup

setup(
    author='CryptoGu',
    author_email='kriptoairdrop9@gmail.com',
     name='HelloWorldAPI1',
    version='0.1',
    description='Simple project that makes a request to GitHub API.',
    py_modules=['hello_world_api1'],
    url='https://github.com/CryptoGu1/Gu-tea.git',
    project_urls={
        'Homepage': 'https://github.com/CryptoGu1/Gu-tea.git',
        'Source': 'https://github.com/CryptoGu1/Gu-tea.git',
        },
    py_modules=['hello_world_api1'],
     install_requires=[
        'requests>=2.25.1',
        'urllib3>=1.26.5'  # Дополнительная зависимость
    ]
)
