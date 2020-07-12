from corona_api import Corona
from events import Events
from mood import Mood
from article import Article

crawler = Corona()

japan_data = crawler.get_confirmed_by_country("Japan")[-1]
world_data = crawler.get_confirmed_globally()

print(japan_data)
print(world_data)

events = Events()

events.event_process(japan_data, world_data)

processed_events = events.__dict__

mood = Mood()

mood.decision(processed_events)

article = Article(processed_events, mood.__dict__)

today_covid_article = article.generate()

print(today_covid_article)