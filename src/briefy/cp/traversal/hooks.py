# -*- coding: utf-8 -*-
"""This module marks requests."""
from briefy.cp.interfaces import IBriefyPloneLayer
from plone import api
from zExceptions.unauthorized import Unauthorized
from zope.interface import directlyProvidedBy
from zope.interface import directlyProvides


ANON_WHITE_LISTED = (
    '++plone',
    '++resource',
    '++theme',
    '@@site-logo',
    '@@sitemap.json',
    'sitemap.json',
    'acl_users',
    'config.js',
    'login',
    '@login',
    'mail_password',
    'mail_password_form',
    'passwordreset',
    'plonejsi18n',
    'pwreset_form',
    'authomatic-handler',
    '@@authomatic-handler',
    'require_login',
)


def gatekeeper(obj, event):
    """Mark the request if we receive the proper header.

    :param obj: Plone content object
    :type obj: object
    :param event: Event
    :type event: event
    """
    request = event.request
    ifaces = list(directlyProvidedBy(request))
    if IBriefyPloneLayer in ifaces:
        ifaces.insert(0, ifaces.pop(ifaces.index(IBriefyPloneLayer)))
    directlyProvides(request, *ifaces)
    event.request.post_traverse(reject_anonymous, (obj, request))


def reject_anonymous(obj, request):
    """Raise an Unauthorized exception if the request is made by an Anonymous user.

    :param obj: Plone content object
    :type obj: object
    :param event: Event
    :type event: event
    """
    if api.user.is_anonymous():
        portal = api.portal.get()
        portal_path = portal.getPhysicalPath()
        physical_path = request.physicalPathFromURL(request['URL'])
        url = physical_path[len(portal_path):]
        if url[-1] == 'index_html':
            url.pop()
        item_id = url[0]
        if not item_id.startswith(ANON_WHITE_LISTED):
            raise Unauthorized('Anonymous rejected')
