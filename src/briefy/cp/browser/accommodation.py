# -*- coding: utf-8 -*-
from plone.dexterity.browser.view import DefaultView
from plone import api


class AccommodationView(DefaultView):
    """The default view for Dexterity content."""

    @property
    def events(self):
        """Return list of contents available in this folderish."""
        all_content = api.content.find(
            context=self.context,
            portal_type='contact',
            depth=1,
            sort_on='start',
            sort_order='reverse'
        )
        return all_content

    def getUserNameById(self, member_id):
        """Return the author object for this id."""
        membership = api.portal.get_tool(name='portal_membership')
        member = membership.getMemberInfo(member_id)
        return member['fullname'] or member['username']

    def toLocalizedTime(self, time, long_format=None, time_only=None):
        """Convert time to localized time."""
        util = api.portal.get_tool(name='translation_service')
        return util.ulocalized_time(
            time, long_format, time_only, self.context, domain='plonelocales'
        )
