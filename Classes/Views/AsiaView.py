from Classes.Views.BaseCountriesView import BaseCountriesView

class AsiaView(BaseCountriesView):
    def __init__(self, bot, embed_info, author):
        self.countries = {"Япония": "🇯🇵", "Китай": "🇨🇳", "Коммунистический Китай": "🇨🇳", "Монголия": "🇲🇳", "Маньчжоу-го": "🇲🇦",
                          "Сиам (Таиланд)": "🇹🇭", "Афганистан": "🇦🇫",
                          "Иран": "🇮🇷", "Ирак": "🇮🇶", "Саудовская Аравия": "🇸🇦", "Турция": "🇹🇷"}
        super().__init__(bot, embed_info, author, self.countries)