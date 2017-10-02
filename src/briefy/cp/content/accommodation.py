# -*- coding: utf-8 -*-
"""Form content type."""
from briefy.cp.content.interfaces import IBriefyContent
from briefy.cp.vocabularies import requirement_item_tags
from plone.dexterity.content import Container
from zope import schema
from zope.interface import implementer
from zope.interface import Interface


class IExternalParterLinkSchema(Interface):
    """Connection to external sites."""

    partner = schema.TextLine(
        title=u'Site',
        required=True
    )
    partner_id = schema.TextLine(
        title=u'Their id',
        required=False
    )
    url = schema.TextLine(
        title=u'URL',
        required=False
    )


class IRequirementItemSchema(Interface):
    """Requirement Items."""

    category = schema.TextLine(
        title=u'Category',
        required=True
    )
    number_of_assets = schema.Int(
        title=u'Number of assets',
        required=True
    )
    description = schema.TextLine(title=u'Comments', required=False)
    tags = schema.List(
        title=u'Tags',
        required=False,
        value_type=schema.Choice(vocabulary=requirement_item_tags)
    )


class IAccommodation(IBriefyContent):
    """Interface for an Accommodation."""


@implementer(IAccommodation)
class Accommodation(Container):
    """An Accommodation."""

    @property
    def partners_ids(self):
        """Return a list of partners for this accommodation."""
        partners = self.partners
        partners = partners if partners else []
        return [p['partner'] for p in partners]
