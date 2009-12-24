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
from zope.component import getMultiAdapter
from zope.traversing.browser import absoluteURL
from zope.app.component.hooks import getSite
from zojax.content.type.interfaces import IContentType
from zojax.content.space.interfaces import IWorkspace


class LayoutPage(object):

    contentId = None
    contentClass = None

    def update(self):
        context = self.context
        request = self.request

        self.url = '%s/'%request.URL
        self.base_url = '%s/'%request.URL[-1]
        self.portal_url = '%s/'%absoluteURL(getSite(), request)

        # body id
        ws = self.maincontext
        while not IWorkspace.providedBy(ws):
            ws = ws.__parent__
            if ws is None:
                break

        if ws is not None:
            self.contentId = 'workspace-%s'%ws.__name__.replace('.', '-')

        # body class
        ct = IContentType(self.maincontext, None)
        if ct is not None:
            self.contentClass = 'section-%s'%ct.name.replace('.', '-')
