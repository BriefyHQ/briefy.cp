"""First login."""
from plone import api


def first_login_handler(event):
    """Add user to Production Group."""
    group = api.group.get(groupname='Production')
    members = [m.getUserName() for m in api.user.get_users(group=group)]
    user = event.object
    username = user.getUserName()
    email = user.getProperty('email')
    if email.endswith('@briefy.co') and username not in members:
        api.group.add_user(groupname='Production', username=username)
