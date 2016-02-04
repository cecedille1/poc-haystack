# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.lorem_ipsum import paragraph

from poc_haystack.models import Model, Model1


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, **options):
        models = [Model(text=paragraph()) for x in range(100)]
        Model.objects.bulk_create(models)

        models = [Model1(text=paragraph()) for x in range(100)]
        Model1.objects.bulk_create(models)
