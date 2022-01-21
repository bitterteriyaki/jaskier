from setuptools import setup


# Library data
packages = ['jaskier']

# Library requirements
install_requires = ['rich==11.0.0']
extras_require = {'docs': ['sphinx==4.4.0', 'sphinx-material==0.0.32']}


# README
with open('README.md') as f:
    readme = f.read()


setup(
    name='jaskier',
    author='kyomi',
    url='https://github.com/soukyomi/jaskier',
    project_urls={
        'Issue tracker': 'https://github.com/soukyomi/jaskier/issues',
    },
    version='0.1.0',
    packages=packages,
    license='MIT',
    description='Library to make loggings more prettier and readable.',
    long_description=readme,
    install_requires=install_requires,
    extras_require=extras_require,
    python_requires='>=3.8.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
    ]
)
