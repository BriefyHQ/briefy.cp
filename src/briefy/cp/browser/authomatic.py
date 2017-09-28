# -*- coding: utf-8 -*-
"""Authomatic view."""
from pas.plugins.authomatic.browser.view import AuthomaticView as BaseView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.interface import implementer
from zope.publisher.interfaces import IPublishTraverse


@implementer(IPublishTraverse)
class AuthomaticView(BaseView):
    """Login."""

    template = ViewPageTemplateFile('authomatic.pt')

    @property
    def google(self):
        """Return a provider, if any."""
        providers = [p for p in self.providers()]
        if providers:
            return providers[0]
