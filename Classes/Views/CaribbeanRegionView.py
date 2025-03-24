from Classes.Views.BaseCountriesView import BaseCountriesView

class CaribbeanRegionView(BaseCountriesView):
    def __init__(self, bot, embed_info, author):
        self.countries = {"Гаити": "🇭🇹", "Диминиканская Руспублика": "🇩🇴", "Куба": "🇨🇺"}
        super().__init__(bot, embed_info, author, self.countries)