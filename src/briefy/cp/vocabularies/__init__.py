# -*- coding: utf-8 -*-
"""Vocabularies used by CMS."""
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary


requirement_item_tags = SimpleVocabulary.fromItems(
    [
        ('Bedroom', 'bedroom'),
        ('Bathroom', 'bathroom'),
        ('Gym', 'gym'),
        ('Spa', 'spam'),
        ('Swimming Pool', 'swimming_pool'),
        ('Roof Terrace', 'roof_terrace'),
        ('Restaurant', 'restaurant'),
        ('Bar', 'bar'),
        ('Executive Lounge', 'executive_lounge'),
        ('Business Centre', 'business_centre'),
        ('Event room', 'event_room'),
        ('Reception', 'reception'),
        ('Lobby', 'lobby'),
        ('Exterior', 'exterior'),
    ]
)

@implementer(IVocabularyFactory)
class RequirementItemsTagsVocabulary(object):
    """Requirement item tags."""

    def __call__(self, context):

        return requirement_item_tags


RequirementItemsTagsVocabularyFactory = RequirementItemsTagsVocabulary()  # noqa


accommodation_types = SimpleVocabulary.fromItems(
    [
        ('Hotel', 'hotel'),
        ('Hostel', 'hostel'),
        ('Pension', 'pension'),
        ('BnB', 'bnb'),
        ('Apartment / Studio', 'apartment'),
    ]
)

@implementer(IVocabularyFactory)
class AccommodationTypesVocabulary(object):
    """Accommodation types."""

    def __call__(self, context):

        return accommodation_types


AccommodationTypesVocabularyFactory = AccommodationTypesVocabulary()  # noqa


accommodation_states = SimpleVocabulary.fromItems(
    [
        ('Not Started', 'not_started'),
        ('In Progress', 'in_progress'),
        ('Skipped', 'skipped'),
        ('Denied', 'rejected'),
        ('Accepted Shoot', 'accepted'),
        ('Scheduled Shoot', 'scheduled'),
        ('Delivered Assets', 'delivered'),
    ]
)

@implementer(IVocabularyFactory)
class AccommodationStatesVocabulary(object):
    """Accommodation states."""

    def __call__(self, context):

        return accommodation_states


AccommodationStatesVocabularyFactory = AccommodationStatesVocabulary()  # noqa


accommodation_stars = SimpleVocabulary.fromItems(
    [
        ('N/A', '-'),
        ('5 Stars', '5'),
        ('4 Stars', '4'),
        ('3 Stars', '3'),
        ('2 Stars', '2'),
        ('1 Star', '1'),
        ('0 Stars', '0'),
    ]
)

@implementer(IVocabularyFactory)
class AccommodationStarsVocabulary(object):
    """Accommodation stars."""

    def __call__(self, context):

        return accommodation_stars


AccommodationStarsVocabularyFactory = AccommodationStarsVocabulary()  # noqa
