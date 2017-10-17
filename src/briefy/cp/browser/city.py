# -*- coding: utf-8 -*-
from cStringIO import StringIO
from datetime import datetime
from plone.dexterity.browser.view import DefaultView
from plone import api
from Products.Five import BrowserView

import csv


class CityView(DefaultView):
    """The default view for Dexterity content."""

    @property
    def accommodations(self):
        """Return all accommodations in here."""
        all_content = api.content.find(
            context=self.context,
            portal_type='accommodation',
            depth=1,
            sort_on='getObjPositionInParent'
        )
        return all_content

    @property
    def total_accommodations(self):
        """Return number of accommodations in here."""
        all_content = self.accommodations
        return len(all_content)


class CSVExport(BrowserView):
    """View to export Accommodations of this City as a CSV File."""

    headers = (
        'id',
        'name',
        'url',
        'street',
        'number',
        'neighbourhood',
        'city',
        'postal_code',
        'country',
    )

    def __init__(self, context, request):
        """Initialize the view.
        :param context: Context object
        :type context: object
        :param request: Request object
        :type request: request
        """
        self.context = context
        self.request = request
        self.response = request.response
        self.state = 'in_progress'

    @property
    def objects(self):
        """Compute objects to be returned on the csv file.

        :returns: List of objects
        :rtype: list
        """
        all_content = api.content.find(
            context=self.context,
            portal_type='accommodation',
            depth=1,
            review_state=self.state,
            sort_on='getObjPositionInParent'
        )
        return [b.getObject() for b in all_content]

    def get_body(self, objects):
        """Process objects and return the contents to the csv file.

        :param objects: List of objects to be exported.
        :type objects: list
        :returns: Body of the csv file.
        :rtype: str
        """
        fp = StringIO()
        writer = csv.DictWriter(
            fp,
            self.headers,
            delimiter='\t',
            quoting=csv.QUOTE_NONE
        )
        writer.writeheader()
        for obj in objects:
            item = {
                'id': obj.id,
                'name': obj.title,
                'url': obj.absolute_url(),
                'street': obj.route,
                'number': obj.street_number,
                'neighbourhood': obj.sublocality,
                'city': obj.locality,
                'postal_code': obj.postal_code,
                'country': obj.country,
            }
            writer.writerow(
                {k: v.encode('utf8') if v else '' for k, v in item.items()}
            )
        data = fp.getvalue()
        fp.close()
        return data

    def __call__(self, *args, **kwargs):
        """Return a CSV File."""
        context = self.context
        response = self.response
        now = datetime.now()
        objects = self.objects
        body = self.get_body(objects)
        response.setHeader('Content-Type', 'text/csv;charset=utf-8')
        cd = 'attachment; filename={date:%Y%m%d%H%M}-{name}-{state}.tsv'.format(
            date=now,
            name=context.id,
            state=self.state
        )
        response.setHeader('Content-Disposition', cd)
        return body
