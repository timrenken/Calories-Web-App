from selectorlib import Extractor
import requests


class Temperature:
    """
    Represent a temperature value extracted from timeanddate.com/weather webpage.
    """
    headers = {
        "user-agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 "
        "Safari/537.36 Edg/97.0.1072.55"
    }
    base_url = "https://www.timeanddate.com/weather/"
    yaml_file = 'temperature.yaml'

    def __init__(self, country, city):
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def _build_url(self):
        url = f"{self.base_url}{self.country}/{self.city}"
        return url

    def _scrape(self):
        url = self._build_url()
        extractor = Extractor.from_yaml_file(self.yaml_file)
        res = requests.get(url, headers=self.headers)
        raw_result = extractor.extract(res.text)
        return raw_result

    def get(self):
        raw_content = self._scrape()
        return float(raw_content['temp'].replace("\xa0°F", ""))


if __name__ == '__main__':
    home = Temperature(city="fort-collins", country="usa")
    print(f"It is {home.get()} degrees Fahrenheit in Fort Collins, Colorado, USA")
