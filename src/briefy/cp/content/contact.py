# -*- coding: utf-8 -*-
"""Form content type."""
from briefy.cp.content.interfaces import IBriefyContent
from plone.dexterity.content import Container
from zope.interface import implementer


class IContact(IBriefyContent):
    """Interface for a Contact."""


@implementer(IContact)
class Contact(Container):
    """A Contact."""
