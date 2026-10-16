from setuptools import setup

setup(
    name='internetarchive',
    version='5.12.0',
    description='A Python interface to archive.org.',
    author_email='"Jacob M. Johnson" <jake@archive.org>',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    install_requires=[
        'jsonpatch>=0.4',
        'requests<3.0.0,>=2.25.0',
        'tqdm>=4.0.0',
        'urllib3>=1.26.0',
    ],
    extras_require={
        'all': [
            'alabaster==1.0.0',
            'mypy',
            'pre-commit',
            'pytest',
            'pytest==9.0.3',
            'responses==0.26.1',
            'ruff==0.14.1',
            'sphinx-autodoc-typehints==3.0.0',
            'sphinx==8.1.3',
            'tqdm-stubs>=0.2.0',
            'types-colorama',
            'types-jsonpatch>=0.1.0a0',
            'types-pygments',
            'types-requests<3.0.0,>=2.25.0',
            'types-ujson>=4.2.0',
            'types-urllib3>=1.26.0',
            'typing-extensions',
        ],
        'dev': [
            'mypy',
            'pre-commit',
            'pytest',
        ],
        'docs': [
            'alabaster==1.0.0',
            'sphinx-autodoc-typehints==3.0.0',
            'sphinx==8.1.3',
            'typing-extensions',
        ],
        'test': [
            'pytest==9.0.3',
            'responses==0.26.1',
            'ruff==0.14.1',
        ],
        'types': [
            'tqdm-stubs>=0.2.0',
            'types-colorama',
            'types-jsonpatch>=0.1.0a0',
            'types-pygments',
            'types-requests<3.0.0,>=2.25.0',
            'types-ujson>=4.2.0',
            'types-urllib3>=1.26.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'ia = internetarchive.cli.ia:main',
        ],
    },
    packages=[
        'internetarchive',
        'internetarchive.cli',
    ],
)
