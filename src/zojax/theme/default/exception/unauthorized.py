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
"""Unauthorized Exception View Class

$Id$
"""
from zope.component import getUtility
from zope.app.component.hooks import getSite
from zope.app.security.interfaces import IAuthentication


class Unauthorized(object):

    def __init__(self, context, request):
        self.exception = context
        super(Unauthorized, self).__init__(getSite(), request)

    def render(self):
        request = self.request
        response = request.response

        # Set the error status to 403 (Forbidden) in the case when we don't
        # challenge the user
        response.setStatus(403)

        # make sure that squid does not keep the response in the cache
        response.setHeader('Expires', 'Mon, 26 Jul 1997 05:00:00 GMT')
        response.setHeader('Cache-Control', 'no-store, no-cache, must-revalidate')
        response.setHeader('Pragma', 'no-cache')

        principal = request.principal

        auth = getUtility(IAuthentication)
        auth.unauthorized(principal.id, request)

        if response.getStatus() not in (302, 303):
            return super(Unauthorized, self).render()
