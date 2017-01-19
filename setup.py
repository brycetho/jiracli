from setuptools import setup

setup(
    name='jiracli',
    version='1.0',
    py_modules=['jiracli'],
    include_package_data=True,
    install_requires=[
        'click',
        'jira',
				'requests',
    ],
    entry_points='''
        [console_scripts]
        jiracli=jiracli:cli
    ''',
)
