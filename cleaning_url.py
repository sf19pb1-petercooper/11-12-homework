"""
A script for removing trash before and after any given URL e.g. https//,www,http as well as removing duplicate URLs.
Currently pulls domains.
"""

import re
import pprint
from urllib.parse import urlparse

URLS = [
       "https://www.eeweb.com/profile/max-maxfield/articles/are-you-ready-for-ces-2019",
"http://www.computing.es/mundo-digital/opinion/1109416046601/cinco-tendencias-del-ces-2019.1.html",
"https://innovadores.larazon.es/es/not/las-cinco-tendencias-del-ces-2019-del-5g-a-la-realidad-inmersiva",
"https://www.revistabyte.es/actualidad-byte/cinco-tendencias-ces-2019/",
"https://www.eweek.com/innovation/why-ces-2019-will-star-5g-immersive-reality-digital-trust-voice-ui",
"Print Only",
"https://www.iot-now.com/2019/01/10/91968-smart-speaker-usage-booms-worldwide-trust-key-continued-adoption-says-accenture/",
"https://www.informationweek.com/strategic-cio/digital-business/platforms-where-the-digital-and-physical-worlds-meet/a/d-id/1334255",
"https://www.techdigest.tv/2019/01/smart-speaker-usage-booming-worldwide-accenture-study-finds.html",
"https://www.androidheadlines.com/2019/01/smart-speaker-usage-study-2019.html",
"https://www.computerweekly.com/news/252455444/Smart-speakers-set-to-own-the-consumer-ecosystem",
"https://www.mediaplaynews.com/study-standalone-voice-assistants-one-of-fastest-adopted-technologies-in-u-s-history/",
"https://www.globalbankingandfinance.com/smart-speaker-usage-booming-worldwide-accenture-study-finds/",
"https://www.barrons.com/articles/big-tech-to-consumers-you-can-trust-us-really-51546980034?mod=bol-social-tw",
"https://telecom.economictimes.indiatimes.com/news/smart-speakers-have-97-satisfaction-rate-in-india-accenture/67455270",
"https://gadgets.ndtv.com/tv/news/smart-speakers-have-97-percent-satisfaction-rate-in-india-accenture-1975249",
"https://www.timesnownews.com/technology-science/article/smart-speakers-one-of-the-fastest-adopted-technologies-have-97-satisfaction-rate-in-india-accenture/344537",
"https://www.pcquest.com/smart-speaker-usage-booming-india-accenture-study-finds/",
"https://www.telegraph.co.uk/technology/2019/01/10/ces-2019-tvs-have-become-new-battleground-tech-giants/",
"https://finance.yahoo.com/video/battle-smart-speakers-003509711.html",
"https://itbrief.co.nz/story/reshape-to-relevance-accenture-s-2019-consumer-survey",
"https://voicebot.ai/2019/01/14/alexa-automotive-news-round-up-ces-2019/",
"https://itbrief.com.au/story/reshape-to-relevance-accenture-s-2019-consumer-survey",
"https://futurefive.co.nz/story/reshape-to-relevance-accenture-s-2019-consumer-survey",
"https://channellife.co.nz/story/reshape-to-relevance-accenture-s-2019-consumer-survey",
"https://finance.yahoo.com/news/how-amazon-alexa-is-winning-the-smart-assistant-race-193904486.html",
"https://www.theaustralian.com.au/life/personal-technology/help-with-routine-activities-is-increasingly-as-easy-as-asking-a-device/news-story/ab4aa6a39048d16ed9e4f43302fc26f3",
"https://www.business-standard.com/article/specials/online-consumers-in-india-are-clearly-ahead-of-the-global-average-study-119011601372_1.html",
"https://www.gadgetguy.com.au/accenture-survey-shows-we-are-a-talkative-lot/",
"https://www.itwire.com/home-it/85768-australian-use-of-dvas-increasing,-accenture-survey-claims.html",
"https://www.techshout.com/gadgets/2019/23/smart-home-speakers-take-india-by-storm/",
"https://www.vanillaplus.com/2019/01/23/44614-speak-digital-virtual-assistants-open-door-ai-csps/",
"https://geekpopsite.wordpress.com/2019/01/28/accenture-confirma-las-tecnologias-cuyo-uso-esta-creciendo-entre-los-consumidores/",
"http://www.webretail.news/index.php/info-rss/3546-pisan-fuerte",
]

for url in URLS:
  parsed_object = (urlparse(url))
  try:
    if parsed_object.netloc.startswith('www.'):
        print(parsed_object.netloc[4:])
    elif parsed_object.netloc == '':
        pass
    else:
        print(parsed_object.netloc)
  except:
      print("Something went wrong when trying to parse URLS")
      sys.exit(1)
