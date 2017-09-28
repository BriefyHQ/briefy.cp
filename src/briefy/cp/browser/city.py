# -*- coding: utf-8 -*-
from plone.dexterity.browser.view import DefaultView
from plone import api


class CityView(DefaultView):
    """The default view for Dexterity content."""

    @property
    def accommodations(self):
        """Return all accommodations in here."""
        all_content = api.content.find(
            context=self.context,
            portal_type='accomodations',
            depth=1,
            sort_on='getObjPositionInParent'
        )
        return all_content

    @property
    def total_accommodations(self):
        """Return number of accommodations in here."""
        all_content = self.accommodations
        return len(all_content)
