from django.shortcuts import render
from django.core.cache import cache
from django.views import generic

def create_nifty_required_data(data):
  nifty_data = list()
  for data in cached_data["data"]:
    temp_nifty_dict = dict()
    temp_nifty_dict["symbol"] = data["symbol"] if "symbol" in data and data["symbol"] else None
    temp_nifty_dict["Last Traded Price"] = data["ltp"] if "ltp" in data and data["ltp"] else None
    temp_nifty_dict["Open"] = data["openPrice"] if "openPrice" in data and data["openPrice"] else None
    temp_nifty_dict["High"] = data["highPrice"] if "highPrice" in data and data["highPrice"] else None
    temp_nifty_dict["Low"] = data["lowPrice"] if "lowPrice" in data and data["lowPrice"] else None
    temp_nifty_dict["% Change"] = data["netPrice"] if "netPrice" in data and data["netPrice"] else None
    temp_nifty_dict["Traded Quantity"] = data["tradedQuantity"] if "tradedQuantity" in data and data["tradedQuantity"] else None
    temp_nifty_dict["Value(In lakhs)"] = data["lastCorpAnnouncement"] if "lastCorpAnnouncement" in data and data["lastCorpAnnouncement"] else None
    temp_nifty_dict["Latest Ex Date"] = data["lastCorpAnnouncementDate"] if "lastCorpAnnouncementDate" in data and data["lastCorpAnnouncementDate"] else None
    nifty_data.append(temp_nifty_dict)

  return nifty_data


def NiftyView(request):
  nifty_data = list()
  try:
    valid_key_for_data = cache.get('valid_key', None)
    if valid_key_for_data:
      cached_data = cache.get(valid_key_for_data, None)
      if cached_data and "data" in cached_data and isinstance(cached_data, list) and cached_data["data"]:
          nifty_data = create_nifty_required_data(data)
    if nifty_data:
    	return render(request, 'nifty.html', {"niftyData": nifty_data})
  except Exception as ex:
    raise ex

