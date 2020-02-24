from django.shortcuts import render

from django.views import generic

def index(request):
	
	nifty_data = {
  "data": [
    {
      "symbol": "INDUSINDBK",
      "series": "EQ",
      "openPrice": "1,145.05",
      "highPrice": "1,203.85",
      "lowPrice": "1,145.05",
      "ltp": "1,180.95",
      "previousPrice": "1,142.15",
      "netPrice": "3.40",
      "tradedQuantity": "1,57,03,698",
      "turnoverInLakhs": "1,85,715.07",
      "lastCorpAnnouncementDate": "08-Aug-2019",
      "lastCorpAnnouncement": "Annual General Meeting\\/Dividend - Rs 7.50 Per Share"
    },
    {
      "symbol": "ZEEL",
      "series": "EQ",
      "openPrice": "252.50",
      "highPrice": "260.85",
      "lowPrice": "251.00",
      "ltp": "260.55",
      "previousPrice": "252.25",
      "netPrice": "3.29",
      "tradedQuantity": "96,84,251",
      "turnoverInLakhs": "24,915.64",
      "lastCorpAnnouncementDate": "15-Jul-2019",
      "lastCorpAnnouncement": "Annual General Meeting\\/ Dividend - Rs 3.50 Per Share"
    },
    {
      "symbol": "TATASTEEL",
      "series": "EQ",
      "openPrice": "429.00",
      "highPrice": "447.70",
      "lowPrice": "428.00",
      "ltp": "443.45",
      "previousPrice": "433.20",
      "netPrice": "2.37",
      "tradedQuantity": "1,29,80,237",
      "turnoverInLakhs": "57,238.95",
      "lastCorpAnnouncementDate": "04-Jul-2019",
      "lastCorpAnnouncement": "Annual General Meeting\\/Dividend - Rs 13 Per Share"
    },
    {
      "symbol": "SBIN",
      "series": "EQ",
      "openPrice": "319.35",
      "highPrice": "329.20",
      "lowPrice": "318.75",
      "ltp": "327.90",
      "previousPrice": "320.35",
      "netPrice": "2.36",
      "tradedQuantity": "4,01,50,409",
      "turnoverInLakhs": "1,30,569.13",
      "lastCorpAnnouncementDate": "15-Jun-2018",
      "lastCorpAnnouncement": "Annual General Meeting\\/ Change In Registrar And Transfer Agent"
    },
    {
      "symbol": "POWERGRID",
      "series": "EQ",
      "openPrice": "187.50",
      "highPrice": "190.70",
      "lowPrice": "185.90",
      "ltp": "189.85",
      "previousPrice": "187.50",
      "netPrice": "1.25",
      "tradedQuantity": "1,45,73,061",
      "turnoverInLakhs": "27,353.64",
      "lastCorpAnnouncementDate": "19-Aug-2019",
      "lastCorpAnnouncement": "Annual General Meeting\\/Dividend - Rs 2.50 Per Share"
    },
    {
      "symbol": "ONGC",
      "series": "EQ",
      "openPrice": "102.00",
      "highPrice": "104.10",
      "lowPrice": "101.70",
      "ltp": "102.75",
      "previousPrice": "101.70",
      "netPrice": "1.03",
      "tradedQuantity": "2,83,78,025",
      "turnoverInLakhs": "29,274.77",
      "lastCorpAnnouncementDate": "22-Aug-2019",
      "lastCorpAnnouncement": "Annual General Meeting\\/Dividend - Rs 0.75 Per Share"
    },
    {
      "symbol": "HINDALCO",
      "series": "EQ",
      "openPrice": "187.80",
      "highPrice": "191.00",
      "lowPrice": "185.40",
      "ltp": "190.00",
      "previousPrice": "188.10",
      "netPrice": "1.01",
      "tradedQuantity": "62,07,445",
      "turnoverInLakhs": "11,720.28",
      "lastCorpAnnouncementDate": "14-Aug-2019",
      "lastCorpAnnouncement": "Annual General Meeting\\/Dividend - Rs 1.20 Per Share"
    },
    {
      "symbol": "COALINDIA",
      "series": "EQ",
      "openPrice": "177.75",
      "highPrice": "180.25",
      "lowPrice": "175.20",
      "ltp": "179.10",
      "previousPrice": "177.75",
      "netPrice": "0.76",
      "tradedQuantity": "1,67,76,977",
      "turnoverInLakhs": "29,797.59",
      "lastCorpAnnouncementDate": "09-Aug-2019",
      "lastCorpAnnouncement": "Annual General Meeting"
    },
    {
      "symbol": "YESBANK",
      "series": "EQ",
      "openPrice": "35.30",
      "highPrice": "36.50",
      "lowPrice": "34.65",
      "ltp": "35.55",
      "previousPrice": "35.30",
      "netPrice": "0.71",
      "tradedQuantity": "11,94,36,898",
      "turnoverInLakhs": "42,782.30",
      "lastCorpAnnouncementDate": "03-Jun-2019",
      "lastCorpAnnouncement": "Annual General Meeting\\/ Dividend - Rs 2 Per Share"
    },
    {
      "symbol": "HCLTECH",
      "series": "EQ",
      "openPrice": "611.00",
      "highPrice": "612.95",
      "lowPrice": "605.15",
      "ltp": "610.00",
      "previousPrice": "605.75",
      "netPrice": "0.70",
      "tradedQuantity": "48,20,313",
      "turnoverInLakhs": "29,329.68",
      "lastCorpAnnouncementDate": "24-Jan-2020",
      "lastCorpAnnouncement": "Interim Dividend - Rs 2 Per Share"
    }
  ],
  "time": "Feb 20, 2020 16:00:00"
}
	

	return render(request, 'nifty.html', {"niftyData": nifty_data})

