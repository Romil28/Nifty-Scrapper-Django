# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from nifty_scrapper import settings
from django.shortcuts import render
from nifty_scrapper.assignment2.models import SharableContent
import urllib 
import uuid
from nifty_scrapper.assignment2.constants import STANDARD_URL
from cryptography.fernet import Fernet
import base64

cipher_suite = Fernet(settings.ENCRYPT_KEY)


def SharableCodeView(request):
	try:
		if request and request.method == 'POST':
			content = request.POST['Snippet'] if 'Snippet' in request.POST and request.POST['Snippet'] else None
			if content:
				unique_uid = uuid.uuid4()
				url = STANDARD_URL + str(unique_uid)
				encrypted_text = cipher_suite.encrypt(str(content).encode('ascii'))
				encrypted_text = base64.urlsafe_b64encode(encrypted_text).decode("ascii")
				if url and encrypted_text:
					SharableContent.objects.create(snippet_url=url, snippet_data=encrypted_text)
					return render(request, 'shareable.html', {'url': url})
		else:
			return render(request, 'shareable.html')
	except:
		raise ex


def ViewShareableSnippet(request):
		try:
			if request and request.method == 'POST':
				url = request.POST['url'] if 'url' in request.POST and request.POST['url'] else None
				if url:
					db_data = SharableContent.objects.filter(snippet_url=url).values()[:1]
					if db_data and db_data[0] and "snippet_data" in db_data[0] and db_data[0]["snippet_data"]:
						data = db_data[0]["snippet_data"]
						data = base64.urlsafe_b64decode(str(data))
				        decoded_text = cipher_suite.decrypt(data).decode("ascii")
				        if decoded_text:
					        return render(request, 'view_shareable_link.html', {"data": decoded_text})
			else:
				return render(request, 'view_shareable_link.html')
		except:
			raise ex