from Classes.Views.BaseCountriesView import BaseCountriesView

class NorthAmericaView(BaseCountriesView):
    def __init__(self, bot, embed_info, author):
        self.countries = {"США": "🇺🇸", "Мексика": "🇲🇽", "Канада": "🇨🇦"}
        super().__init__(bot, embed_info, author, self.countries)
