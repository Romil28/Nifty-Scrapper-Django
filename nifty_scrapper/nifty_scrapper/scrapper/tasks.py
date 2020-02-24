
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache
from django.conf import settings
from nifty_scrapper.scrapper.constants import SCRAPING_URL, HEADERS, NIFTY_API_URL
# from nifty_scrapper.celery import app
import celery
import datetime


def get_scrapped_data():
	try:
		response = requests.get(SCRAPING_URL, headers=HEADERS)
		soup = BeautifulSoup(response.content, 'lxml')
		return soup if soup else None
	except Exception as ex:
		logging.info("UNABLE TO SCRAPE THE DATA!")
		raise ex

def get_nse_json_data():
	try:
		code = requests.get(NIFTY_API_URL, headers=headers)
		if code:
			plain = code.text
			jsonData = BeautifulSoup(plain, "html.parser")
			return jsonData if jsonData and isinstance(jsonData, dict) else None
		return None
	except Exception as ex:
		logging.info("UNABLE TO GET THE DATA OF NIFTY URL!")
		raise ex

# @app.task()
def scrapper():
	try:
		soup_data = get_scrapped_data()
		if soup_data:
			class_data = soup_data.find("div", class_ = "tabular_data_live_analysis")
			if class_data:
				table_content = class_data.find("table", attrs={"id": "topGainers"})
				if table_content:
					tr_data = table_content.find_all("tr")
					if tr_data and tr_data[0]:
						for th_data in tr_data[0].find_all("th"):
							print("th_data", th_data.text)

			nifty_url_data = get_nse_json_data()
			if nifty_url_data != None:
				cached_keys = cache.keys('prefix:*')
				if cached_keys:
					for key in cached_keys:
						cache.delete(key)

			current_timestamp = datetime.datetime.now()
			cache.set('valid_key', current_timestamp, timeout=None)
			cache.set(current_timestamp, nifty_url_data, timeout=None)
			logging.info("DATA SUCCESSFULLY CACHED IN REDIS")
		else:
			logging.info("NO SOUP DATA FOUND AFTER SCRAPING!")
	except:
		raise ex

# from celery.task.schedules import crontab
# from celery.decorators import periodic_task

# @periodic_task(run_every=crontab(minute=1))
# def every_monday_morning():
#     print("This runs every Monday morning at 7:30a.m.")
