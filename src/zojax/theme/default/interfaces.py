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
"""

$Id$
"""
from zope import interface
from zojax.pageelement.interfaces import IPageElement
from zojax.layoutform.interfaces import ILayoutFormLayer
from zojax.ui.googleanalytics.interfaces import IGoogleAnalyticsHeaders


class ICommonSkinLayer(ILayoutFormLayer):
    """ common skin layer """


class ISkinLayer(interface.Interface):
    """ zojax layer """
    

class ISkin(ISkinLayer, ICommonSkinLayer):
    """ zojax Skin """


# pagelet elements
class IPortalHeader(IPageElement):
    """ portal header """


class IPortalFooter(IPageElement):
    """ portal footer """


# viewlet managers
class IPageHeaders(IPageElement, IGoogleAnalyticsHeaders):
    """ page headers """
