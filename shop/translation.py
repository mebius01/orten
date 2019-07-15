# -*- coding: utf-8 -*-

from modeltranslation.translator import translator, TranslationOptions
from shop.models import Product, Services, Category

class CategoryTranslationOptions(TranslationOptions):
	fields = ('name', 'description')

class ProductTranslationOptions(TranslationOptions):
	fields = ('name', 'specifications', 'description')

class ServicesTrnsletionOptions(TranslationOptions):
	fields = ('name', 'description')

translator.register(Category, CategoryTranslationOptions)
translator.register(Product, ProductTranslationOptions)
translator.register(Services, ServicesTrnsletionOptions)
