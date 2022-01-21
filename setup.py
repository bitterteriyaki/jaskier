from setuptools import setup


# Library data
packages = ['jaskier']

# Library requirements
install_requires = ['rich==11.0.0']
extras_require = {'docs': ['sphinx==4.4.0', 'sphinx-material==0.0.32']}


setup(
    name='jaskier',
    packages=packages,
    install_requires=install_requires,
    extras_require=extras_require,
)
