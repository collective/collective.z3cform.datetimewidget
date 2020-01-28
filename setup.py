from setuptools import setup, find_packages

version = '1.2.9'

setup(name='collective.z3cform.datetimewidget',
      version=version,
      description="z3c.form date and datetime widgets",
      long_description=open("README.rst").read() + "\n" +
          open("HISTORY.rst").read(),
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='z3cform datetime widget',
      author='Rok Garbas',
      author_email='rok@garbas.si',
      url='https://github.com/collective/collective.z3cform.datetimewidget',
      license='GPL version 2',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['collective', 'collective.z3cform'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zope.i18n',
          'z3c.form',
          'zope.deprecation'
      ],
      extras_require=dict(test=[
            'z3c.form',
            'zope.browserpage',
            'zope.publisher',
            'zope.testing',
            'zope.traversing',
            'zc.buildout',
            'Zope2',
            ]),
      )
