from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem


class LeboncoinFr_1(BasePortiaSpider):
    name = "www.leboncoin.fr_1"
    custom_settings = {
                       'CLOSESPIDER_ITEMCOUNT': 400,
                       'FEED_URI':'/tmp/export.csv'}
    handle_httpstatus_list = [301,302]

    allowed_domains = [u'www.leboncoin.fr']
    start_urls = [
        u'https://www.leboncoin.fr/ventes_immobilieres/offres/aquitaine/gironde/?th=1&location=L%E8ge-Cap-Ferret%2033950%2CAr%E8s%2033740%2CAndernos-les-Bains%2033510']
    rules = [
        Rule(
            LinkExtractor(
                allow=(u'ca=2_s',u'ventes'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [
        [
            Item(
                PortiaItem,
                None,
                u'._2ketD > div',
                [
                    Field(
                        u'Titre',
                        'div > div > ._20rd1 > ._35sFG > .OjX8R > ._2NKYa > ._3aOPO > ._14taM > div:nth-child(1) > ._1KQme *::text',
                        []),
                    Field(
                        u'Prix',
                        'div > div > ._20rd1 > ._35sFG > .OjX8R > ._2NKYa > ._3aOPO > ._14taM > .eVLNz > ._386c2 > ._1F5u3 *::text',
                        []),
                    Field(
                        u'Mis_en_ligne',
                        'div > div > ._20rd1 > ._35sFG > .OjX8R > ._2NKYa > ._3aOPO > ._14taM > ._3Pad- *::text',
                        []),
                    Field(
                        u'Type_de_Bien',
                        'div > div > ._20rd1 > ._35sFG > .OjX8R > div:nth-child(3) > div:nth-child(2) > ._277XW > div:nth-child(1) > div > ._3Jxf3 *::text',
                        []),
                    Field(
                        u'Pieces',
                        'div > div > ._20rd1 > ._35sFG > .OjX8R > div:nth-child(3) > div:nth-child(2) > ._277XW > div:nth-child(2) > div > ._3Jxf3 *::text',
                        []),
                    Field(
                        u'Surface',
                        'div > div > ._20rd1 > ._35sFG > .OjX8R > div:nth-child(3) > div:nth-child(2) > ._277XW > div:nth-child(3) > div > ._3Jxf3 *::text',
                        []),
                    Field(
                        u'Description',
                        'div > div > ._20rd1 > ._35sFG > .OjX8R > div:nth-child(4) > div:nth-child(2) > div > div:nth-child(1) *::text',
                        []),
                    Field(
                        u'Localisation',
                        'div > div > ._20rd1 > ._35sFG > .OjX8R > div:nth-child(5) > div:nth-child(2) > ._2CWtv > .trackable > ._1aCZv > span *::text',
                        []),
                    Field(
                        u'Telephone2',
                        'div > div > ._20rd1 > ._35sFG > ._1_H-h > ._2-Dyg > div > div > div > .JTTtB > div:nth-child(1) > div > div > ._2sNbI *::text',
                        []),
                    Field(
                        u'Contact',
                        'div > div > ._20rd1 > ._35sFG > ._1_H-h > ._2-Dyg > div > div > div > .JTTtB > .trackable > div > ._28rnK > ._2sNbI::attr(href)',
                        []),
                    Field(
                        u'Origine',
                        '._3mBNy > ._1AsHn > div > ._3Qo_G > ._29yTo > div:nth-child(1) *::text',
                        [])])]]
                        

class LeboncoinFr_2(BasePortiaSpider):
    name = "www.leboncoin.fr_2"
    custom_settings = {
                       'CLOSESPIDER_ITEMCOUNT': 4,
                       'FEED_URI':'/tmp/export.csv'}
    handle_httpstatus_list = [301,302]

    allowed_domains = [u'www.leboncoin.fr']
    start_urls = [
        u'https://www.leboncoin.fr/ventes_immobilieres/offres/aquitaine/gironde/?th=1&location=L%E8ge-Cap-Ferret%2033950%2CAr%E8s%2033740%2CAndernos-les-Bains%2033510']
    rules = [
        Rule(
            LinkExtractor(
                allow=(u'ca=2_s',u'ventes'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [
        [
            Item(
                PortiaItem,
                None,
                u'._2ketD > div',
                [
                    Field(
                        u'Titre',
                        'div > div > ._20rd1 > ._35sFG > .OjX8R > ._2NKYa > ._3aOPO > ._14taM > div:nth-child(1) > ._1KQme *::text',
                        []),
                    Field(
                        u'Prix',
                        'div > div > ._20rd1 > ._35sFG > .OjX8R > ._2NKYa > ._3aOPO > ._14taM > .eVLNz > ._386c2 > ._1F5u3 *::text',
                        []),
                    Field(
                        u'Mis_en_ligne',
                        'div > div > ._20rd1 > ._35sFG > .OjX8R > ._2NKYa > ._3aOPO > ._14taM > ._3Pad- *::text',
                        []),
                    Field(
                        u'Type_de_Bien',
                        'div > div > ._20rd1 > ._35sFG > .OjX8R > div:nth-child(3) > div:nth-child(2) > ._277XW > div:nth-child(1) > div > ._3Jxf3 *::text',
                        []),
                    Field(
                        u'Pieces',
                        'div > div > ._20rd1 > ._35sFG > .OjX8R > div:nth-child(3) > div:nth-child(2) > ._277XW > div:nth-child(2) > div > ._3Jxf3 *::text',
                        []),
                    Field(
                        u'Surface',
                        'div > div > ._20rd1 > ._35sFG > .OjX8R > div:nth-child(3) > div:nth-child(2) > ._277XW > div:nth-child(3) > div > ._3Jxf3 *::text',
                        []),
                    Field(
                        u'Description',
                        'div > div > ._20rd1 > ._35sFG > .OjX8R > div:nth-child(4) > div:nth-child(2) > div > div:nth-child(1) *::text',
                        []),
                    Field(
                        u'Localisation',
                        'div > div > ._20rd1 > ._35sFG > .OjX8R > div:nth-child(5) > div:nth-child(2) > ._2CWtv > .trackable > ._1aCZv > span *::text',
                        []),
                    Field(
                        u'Telephone2',
                        'div > div > ._20rd1 > ._35sFG > ._1_H-h > ._2-Dyg > div > div > div > .JTTtB > div:nth-child(1) > div > div > ._2sNbI *::text',
                        []),
                    Field(
                        u'Contact',
                        'div > div > ._20rd1 > ._35sFG > ._1_H-h > ._2-Dyg > div > div > div > .JTTtB > .trackable > div > ._28rnK > ._2sNbI::attr(href)',
                        []),
                    Field(
                        u'Origine',
                        '._3mBNy > ._1AsHn > div > ._3Qo_G > ._29yTo > div:nth-child(1) *::text',
                        [])])]]