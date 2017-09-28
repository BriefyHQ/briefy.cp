# -*- coding: utf-8 -*-
"""Form content type."""
from briefy.cp.content.interfaces import IBriefyContent
from plone.dexterity.content import Container
from zope.interface import implementer


class ICity(IBriefyContent):
    """Interface for a City."""


@implementer(ICity)
class City(Container):
    """A City."""
