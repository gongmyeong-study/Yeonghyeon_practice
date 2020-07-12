class Article:
    def __init__(self, events, moods):
        self.events = events
        self.moods = moods

    def generate(self):
        country_name = self.events["country_name"]
        country_cases = self.events["country_cases"]
        world_cases = self.events["world_cases"]

        mood_globally = self.moods["covid_mood_globally"]
        mood_in_country = self.moods["covid_mood_in_country"]

        article = f"오늘 전 세계 신규 확진자 수는 {world_cases}명입니다. " \
                  f"그리고 {country_name}의 확진자 수는 {country_cases}명입니다."

        if mood_globally == "Highly Dangerous":
            article += "\n전 세계가 위험해!"
        elif mood_globally == "Dangerous":
            article += "\n세계가 큰 위기는 넘긴 것 같다."

        if mood_in_country == "Highly Dangerous":
            article += "\n사회적 거리두기가 시급합니다."
        elif mood_in_country == "Dangerous":
            article += "\n노래방만 가지마세요."


        return article
