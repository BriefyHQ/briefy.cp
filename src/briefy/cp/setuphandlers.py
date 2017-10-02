# -*- coding: utf-8 -*-
"""Setup handlers for Briefy CP."""
from plone import api
from StringIO import StringIO
from zope.component import getMultiAdapter

import os


TO_DELETE = (
    'front-page', 'news', 'events', 'Members'
)


def get_faceted_config():
    """Prepare a file for upload."""
    path = os.path.join(os.path.dirname(__file__))
    filename = 'berlin.xml'
    data = open('{0}/{1}'.format(path, filename), 'r').read()
    fp = StringIO(data)
    fp.filename = 'berlin.xml'
    return fp


def run_after(context):
    """Executed after briefy.cp installation."""
    portal = api.portal.get()
    o_ids = [o_id for o_id in TO_DELETE if o_id in portal.objectIds()]
    for o_id in o_ids:
        api.content.delete(obj=portal[o_id])
    # Create user developer
    user = api.user.create(
        email='developers@briefy.co',
        password='123456',
        properties={
            'fullname': 'Briefy Team',
            'location': 'Berlin',
        }
    )
    roles = ['Reviewer', 'Site Administrator', 'Manager', 'Editor', 'Contributor']
    api.user.grant_roles(user=user, roles=roles)

    # Create group production
    group = api.group.create(
        groupname='Production',
        title='Production',
        description='Briefy Production Team'
    )

    # Create Berlin City
    obj = api.content.create(
        type='city',
        title='Berlin',
        description='Berlin City Packages project',
        container=portal
    )
    roles = ['Reviewer', 'Editor', 'Reader', 'Contributor']
    api.group.grant_roles(group=group, roles=roles, obj=obj)
    api.content.transition(obj=obj, transition='open')

    # Faceted Navigation
    subtyper = getMultiAdapter((obj, context.REQUEST), name=u'faceted_subtyper')
    subtyper.enable()
    view = obj.unrestrictedTraverse('@@faceted_exportimport')
    query = {
      'import_button': 'Import',
      'import_file': get_faceted_config(),
      'redirect': '',
    }
    result = view(**query)
