# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class SharableContent(models.Model):
	id = models.AutoField(primary_key=True, verbose_name="Content ID")
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	snippet_url = models.CharField(max_length=500)
	snippet_data = models.TextField()

	class Meta:
		db_table = 'sharable_content'
		indexes = [
            models.Index(fields=['snippet_url'], name='snippet_url_idx'),
        ]
