from __future__ import absolute_import

import scrapy
from collections import defaultdict
from scrapy.loader.processors import Join, MapCompose, Identity
from w3lib.html import remove_tags
from .utils.processors import Text, Number, Price, Date, Url, Image


class PortiaItem(scrapy.Item):
    fields = defaultdict(
        lambda: scrapy.Field(
            input_processor=Identity(),
            output_processor=Identity()
        )
    )

    def __setitem__(self, key, value):
        self._values[key] = value

    def __repr__(self):
        data = str(self)
        if not data:
            return '%s' % self.__class__.__name__
        return '%s(%s)' % (self.__class__.__name__, data)

    def __str__(self):
        if not self._values:
            return ''
        string = super(PortiaItem, self).__repr__()
        return string


class BrachTerrainDeMItem(PortiaItem):
    Surface = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Mis_en_ligne = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Titre = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Prix = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    type_de_bien = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class AppartementPicesMItem(PortiaItem):
    Prix = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Localisation = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Pieces = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Telephone = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    Surface = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Titre = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Description = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Mis_en_ligne = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )


class VenteImmobilireNosAnnoncesGirondeLebonItem(PortiaItem):
    pass
