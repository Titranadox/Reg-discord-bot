from Classes.Views.BaseCountriesView import BaseCountriesView

class CentralAmericaView(BaseCountriesView):
    def __init__(self, bot, embed_info, author):
        self.countries = {"Гватемала": "🇬🇹", "Гондурас": "🇭🇳", "Сальвадор": "🇸🇻", "Никарагуа": "🇳🇮", "Коста-Рика": "🇨🇷",
                          "Панама": "🇵🇦"}
        super().__init__(bot, embed_info, author, self.countries)
