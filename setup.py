##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup for zojax.theme.default package

$Id$
"""
import sys, os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version='0'


setup(name='zojax.theme.default',
      version=version,
      description="Default theme for zojax.",
      long_description=(
          'Detailed Documentation\n' +
          '======================\n'
          + '\n\n' +
          read('CHANGES.txt')
          ),
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Framework :: Zope3'],
      author='Nikolay Kim',
      author_email='fafhrd91@gmail.com',
      url='http://zojax.net/',
      license='ZPL 2.1',
      packages=find_packages('src'),
      package_dir = {'':'src'},
      namespace_packages=['zojax', 'zojax.theme'],
      install_requires = ['setuptools',
                          'zope.interface',
                          'zope.component',
                          'zope.traversing',
                          'zope.security',
                          'zope.publisher',
                          'zope.contentprovider',
                          'zope.app.component',
                          'zope.app.publisher',

                          'zojax.content.draft',
                          'zojax.content.space',
                          'zojax.personal.bar',
                          'zojax.personal.space',

                          'zojax.cache',
                          'zojax.layout',
                          'zojax.layoutform',
                          'zojax.portlet',
                          'zojax.pageelement',
                          'zojax.statusmessage',
                          'zojax.resource',
                          'zojax.resourcepackage',
                          'zojax.seo',
                          'zojax.skintool',
                          'zojax.ui.breadcrumbs',
                          'zojax.ui.googleanalytics',
                          'zojax.ui.simplettw',

                          'zojax.jquery.i18n',
                          ],
      extras_require = dict(test=['zope.app.testing',
                                  'zope.testing',
                                  'zope.testbrowser',
                                  'zope.securitypolicy',
                                  'zojax.portal',
                                  'zojax.autoinclude',
                                  ]),
      include_package_data = True,
      zip_safe = False
      )
