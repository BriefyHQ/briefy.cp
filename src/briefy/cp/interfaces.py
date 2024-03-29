# -*- coding: utf-8 -*-
"""Interfaces for briefy.cp."""
from zope.interface import Interface


class IBriefyPloneLayer(Interface):
    """A layer specific for Briefy Plone CMS package.

    This interface is referred in browserlayer.xml.

    All views and viewlets register against this layer will appear on
    your Plone site only when the this package is installed.
    """

    pass
