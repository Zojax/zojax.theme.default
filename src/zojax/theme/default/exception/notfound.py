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
"""NotFound Error View class.

$Id$
"""
class NotFound(object):
    """ `NotFound` Error View

    `NotFound` errors should return 404 instead of 200.
    """
    def __init__(self, context, request):
        super(NotFound, self).__init__(context.ob, request)

    def render(self):
        self.request.response.setStatus(404)
        return super(NotFound, self).render()
