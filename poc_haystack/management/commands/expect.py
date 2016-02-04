# -*- coding: utf-8 -*-


from django.core.management.base import BaseCommand
from django.db import transaction
from haystack.query import SearchQuerySet
from poc_haystack.models import Model


class Command(BaseCommand):
    def handle(self, **options):
        sqs = SearchQuerySet().models(Model).auto_query('nesciunt')
        length = len(sqs)
        iterate_count = sum(1 for x in sqs)

        assert length == iterate_count, ('%s != %s' % (length, iterate_count))
