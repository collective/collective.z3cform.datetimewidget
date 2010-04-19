from setuptools import setup, find_packages

version = '1.0'

setup(name='collective.z3cform.datetimewidget',
      version=version,
      description="z3c.form date and datetime widgets",
      long_description=open("README.txt").read()+"\n"+open("HISTORY.txt").read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='z3cform datetime widget',
      author='Rok Garbas',
      author_email='rok@garbas.si',
      url='http://svn.plone.org/svn/collective/collective.z3cform.datetimewidget',
      license='GPL',
      packages = find_packages('src', exclude=['ez_setup']),
      package_dir = {'':'src'},
      namespace_packages=['collective', 'collective.z3cform'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'zope.i18n',
          'z3c.form',
          'zope.deprecation'
      ],
      extras_require=dict(test=[
            'z3c.form[test]',
            'zope.testing',
            'zc.buildout']),
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
