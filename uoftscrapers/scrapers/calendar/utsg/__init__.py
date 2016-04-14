from ...scraper import Scraper
from bs4 import BeautifulSoup
from collections import OrderedDict
import json
import os
import requests

class UTSGCalendar:

    host = 'http://www.artsandscience.utoronto.ca/ofr/calendar/'

    @staticmethod
    def scrape(location='.'):
        Scraper.logger.info('UTSGCalendar initialized.')
        Scraper.logger.info('Not implemented.')
        raise NotImplementedError('This scraper has not been implemented yet.')
        Scraper.logger.info('UTSGCalendar completed.')
