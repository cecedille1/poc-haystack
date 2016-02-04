# -*- coding: utf-8 -*-

from haystack import indexes

from poc_haystack.models import Model, Model1


class ModelIndex(indexes.ModelSearchIndex, indexes.Indexable):
    text = indexes.CharField(
        document=True,
        model_attr='text',
    )

    class Meta:
        model = Model


class Model1Index(indexes.ModelSearchIndex, indexes.Indexable):
    text = indexes.CharField(
        document=True,
        model_attr='text',
    )

    class Meta:
        model = Model1
