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
from zope.security import checkPermission
from zope.component import getAdapters, queryAdapter, queryMultiAdapter
from zope.app.component.hooks import getSite
from zope.traversing.api import getPath
from zope.traversing.browser import absoluteURL
from z3c.breadcrumb.interfaces import IBreadcrumb
from zojax.cache.view import cache
from zojax.cache.keys import ContextModified
from zojax.cache.interfaces import DoNotCache
from zojax.layout.interfaces import ILayout
from zojax.content.type.interfaces import IDraftedContent
from zojax.content.space.interfaces import \
    IRootSpace, IContentSpaceLayout, \
    IWorkspace, IWorkspaceFactory, IWorkspacesManagement, \
    IInactiveWorkspaceFactory


def Workspace(object, instance, *args, **kw):
    if not instance.available:
        raise DoNotCache()
    if instance.workspace is not None:
        return {'context': getPath(instance.workspace)}
    else:
        return ()


class PortalTabs(object):

    available = True
    workspaces = False

    def __init__(self, context, request, view, manager=None):
        maincontext = context

        site = getSite()
        if not IRootSpace.providedBy(site) or \
                IContentSpaceLayout.providedBy(site) and not site.showTabs:
            self.available = False
            super(PortalTabs, self).__init__(context, request, view, manager)
            return

        wsname = u''
        ws = None
        if ILayout.providedBy(view.view):
            context = view.view.mainview
        elif ILayout.providedBy(view):
            context = view.mainview

        while not IRootSpace.providedBy(context) \
                or IDraftedContent.providedBy(context):
            if IWorkspace.providedBy(context):
                ws = context
                wsname = context.__name__
            context = context.__parent__
            if context is None:
                break

        self.wsname = wsname
        self.workspace = ws

        super(PortalTabs, self).__init__(site, request, view, manager)

    def update(self):
        super(PortalTabs, self).update()

        if not self.available:
            return

        site = self.context
        wsname = self.wsname
        request = self.request

        url = absoluteURL(site, self.request)

        selected = False

        wfactories = []
        if IWorkspacesManagement.providedBy(site):
            if site.enabledWorkspaces:
                for name in site.enabledWorkspaces:
                    factory = queryAdapter(site, IWorkspaceFactory, name)
                    if factory is not None and \
                            checkPermission('zope.View', factory.install()):
                        wfactories.append((name, factory))

        if not wfactories:
            for name, factory in getAdapters((site,), IWorkspaceFactory):
                if not IInactiveWorkspaceFactory.providedBy(factory) and \
                        not site.isEnabled(factory) or \
                        not checkPermission('zope.View', factory.install()):
                    continue
                wfactories.append((
                        factory.weight, factory.title, name, factory))

            wfactories.sort()
            wfactories = [(n, f) for _w, _t, n, f in wfactories]

        seen = set()
        workspaces = []
        for name, factory in wfactories:
            if name in seen:
                continue

            seen.add(name)

            if not site.isEnabled(factory):
                continue

            if name == wsname:
                selected = True

            workspaces.append(
                {'name': name,
                 'url': '%s/%s/'%(url, name),
                 'title': factory.title,
                 'description': factory.description,
                 'selected': name == wsname,
                 'icon': queryMultiAdapter((factory,request), name='zmi_icon')})

        if not selected:
            self.siteSelected = True
        else:
            self.siteSelected = False

        self.workspaces = workspaces

    def isAvailable(self):
        return self.available and self.workspaces

    @cache('pageelement: portal.tabs (default)', ContextModified, Workspace)
    def updateAndRender(self):
        return super(PortalTabs, self).updateAndRender()
