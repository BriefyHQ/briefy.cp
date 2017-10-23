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
        ('Close-ups', 'closeups'),
        ('Food / Drinks', 'food_drinks'),
        ('Kitchen', 'kitchen'),
        ('Living Room', 'living_room'),
        ('Terrace / Balcony', 'terrace_balcony'),
        ('Staircase', 'staircase'),
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
        ('Bed & Breakfast', 'bnb'),
        ('Holiday Home', 'holiday_home'),
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

berlin_sublocalities = SimpleVocabulary.fromItems(
    [
        # (u'Charlottenburg', u'Charlottenburg'),
        # (u'Grunewald', u'Grunewald'),
        # (u'Schmargendorf', u'Schmargendorf'),
        # (u'Wilmersdorf', u'Wilmersdorf'),
        # (u'Friedrichshain', u'Friedrichshain'),
        # (u'Kreuzberg', u'Kreuzberg'),
        # (u'Falkenberg', u'Falkenberg'),
        # (u'Fennpfuhl', u'Fennpfuhl'),
        # (u'Friedrichsfelde', u'Friedrichsfelde'),
        # (u'Hohenschönhausen', u'Hohenschönhausen'),
        # (u'Karlshorst', u'Karlshorst'),
        # (u'Lichtenberg', u'Lichtenberg'),
        # (u'Malchow', u'Malchow'),
        # (u'Rummelsburg', u'Rummelsburg'),
        # (u'Wartenberg', u'Wartenberg'),
        # (u'Biesdorf', u'Biesdorf'),
        # (u'Hellersdorf', u'Hellersdorf'),
        # (u'Kaulsdorf', u'Kaulsdorf'),
        # (u'Mahlsdorf', u'Mahlsdorf'),
        # (u'Marzahn', u'Marzahn'),
        # (u'Biesdorf', u'Biesdorf'),
        # (u'Hellersdorf', u'Hellersdorf'),
        # (u'Kaulsdorf', u'Kaulsdorf'),
        # (u'Mahlsdorf', u'Mahlsdorf'),
        # (u'Marzahn', u'Marzahn'),
        # (u'Gesundbrunnen', u'Gesundbrunnen'),
        # (u'Hansaviertel', u'Hansaviertel'),
        # (u'Moabit', u'Moabit'),
        # (u'Mitte', u'Mitte'),
        # (u'Tiergarten', u'Tiergarten'),
        # (u'Wedding', u'Wedding'),
        # (u'Britz', u'Britz'),
        # (u'Buckow', u'Buckow'),
        # (u'Gropiusstadt', u'Gropiusstadt'),
        # (u'Neukölln', u'Neukölln'),
        # (u'Rudow', u'Rudow'),
        # (u'Blankenburg', u'Blankenburg'),
        # (u'Blankenfelde', u'Blankenfelde'),
        # (u'Buch', u'Buch'),
        # (u'Französisch Buchholz', u'Französisch Buchholz'),
        # (u'Heinersdorf', u'Heinersdorf'),
        # (u'Karow', u'Karow'),
        # (u'Malchow', u'Malchow'),
        # (u'Niederschönhausen', u'Niederschönhausen'),
        # (u'Pankow', u'Pankow'),
        # (u'Prenzlauer Berg', u'Prenzlauer Berg'),
        # (u'Rosenthal', u'Rosenthal'),
        # (u'Weißensee', u'Weißensee'),
        # (u'Wilhelmsruh', u'Wilhelmsruh'),
        # (u'Frohnau', u'Frohnau'),
        # (u'Heiligensee inkl, Schulzendorf', u'Heiligensee inkl, Schulzendorf'),
        # (u'Hermsdorf', u'Hermsdorf'),
        # (u'Konradshöhe inkl, Tegelort u, Jörsfelde', u'Konradshöhe inkl, Tegelort u, Jörsfelde'),
        # (u'Lübars', u'Lübars'),
        # (u'Märkisches Viertel', u'Märkisches Viertel'),
        # (u'Reinickendorf', u'Reinickendorf'),
        # (u'Tegel', u'Tegel'),
        # (u'Waidmannslust', u'Waidmannslust'),
        # (u'Wittenau inkl, Borsigwalde', u'Wittenau inkl, Borsigwalde'),
        # (u'Falkenhagener Feld', u'Falkenhagener Feld'),
        # (u'Gatow', u'Gatow'),
        # (u'Hakenfelde', u'Hakenfelde'),
        # (u'Haselhorst', u'Haselhorst'),
        # (u'Kladow', u'Kladow'),
        # (u'Siemensstadt', u'Siemensstadt'),
        # (u'Spandau', u'Spandau'),
        # (u'Staaken', u'Staaken'),
        # (u'Wilhelmstadt', u'Wilhelmstadt'),
        # (u'Dahlem', u'Dahlem'),
        # (u'Lankwitz', u'Lankwitz'),
        # (u'Lichterfelde', u'Lichterfelde'),
        # (u'Nikolassee', u'Nikolassee'),
        # (u'Steglitz', u'Steglitz'),
        # (u'Wannsee', u'Wannsee'),
        # (u'Zehlendorf', u'Zehlendorf'),
        # (u'Friedenau', u'Friedenau'),
        # (u'Mariendorf', u'Mariendorf'),
        # (u'Marienfelde', u'Marienfelde'),
        # (u'Lichtenrade', u'Lichtenrade'),
        # (u'Schöneberg', u'Schöneberg'),
        # (u'Tempelhof', u'Tempelhof'),
        # (u'Adlershof', u'Adlershof'),
        # (u'Altglienicke', u'Altglienicke'),
        # (u'Alt-Treptow', u'Alt-Treptow'),
        # (u'Baumschulenweg', u'Baumschulenweg'),
        # (u'Bohnsdorf', u'Bohnsdorf'),
        # (u'Friedrichshagen', u'Friedrichshagen'),
        # (u'Grünau', u'Grünau'),
        # (u'Hessenwinckel', u'Hessenwinckel'),
        # (u'Johannisthal', u'Johannisthal'),
        # (u'Köpenick', u'Köpenick'),
        # (u'Müggelheim', u'Müggelheim'),
        # (u'Niederschöneweide', u'Niederschöneweide'),
        # (u'Oberschöneweide', u'Oberschöneweide'),
        # (u'Plänterwald', u'Plänterwald'),
        # (u'Rahnsdorf', u'Rahnsdorf'),
        # (u'Schmöckwitz', u'Schmöckwitz'),
        # (u'Treptow', u'Treptow')
    ]
)

@implementer(IVocabularyFactory)
class BerlinSublocalitiesVocabulary(object):
    """Berlin sublocalities."""

    def __call__(self, context):

        return berlin_sublocalities


BerlinSublocalitiesVocabularyFactory = BerlinSublocalitiesVocabulary()  # noqa


gallery_quality = SimpleVocabulary.fromItems(
    [
        ('--', ''),
        ('5', '5'),
        ('4', '4'),
        ('3', '3'),
        ('2', '2'),
        ('1', '1'),
        ('0', '0'),
    ]
)

@implementer(IVocabularyFactory)
class AccommodationGalleryVocabulary(object):
    """Accommodation Gallery quality."""

    def __call__(self, context):

        return gallery_quality


AccommodationGalleryVocabularyFactory = AccommodationGalleryVocabulary()  # noqa
