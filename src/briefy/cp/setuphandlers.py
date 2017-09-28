# -*- coding: utf-8 -*-
"""Setup handlers for Briefy CP."""
from plone import api


TO_DELETE = (
    'front-page', 'news', 'events', 'Members'
)

def run_after(context):
    """Executed after briefy.cp installation."""
    portal = api.portal.get()
    o_ids = [o_id for o_id in TO_DELETE if o_id in portal.objectIds()]
    for o_id in o_ids:
        api.content.delete(obj=portal[o_id])
