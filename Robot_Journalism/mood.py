class Mood:
    def decision(self, events):
        country_cases = events["country_cases"]
        country_name = events["country_name"]
        world_cases = events["world_cases"]

        # world_cases mood
        if world_cases >= 200000:
            self.covid_mood_globally = "Highly Dangerous"
        elif world_cases >= 150000:
            self.covid_mood_globally = "Dangerous"
        else:
            self.covid_mood_globally = "Safe"

        # country_cases mood
        if country_name == "Japan":
            if country_cases >= 300:
                self.covid_mood_in_country = "Dangerous"
            else:
                self.covid_mood_in_country = "Safe"