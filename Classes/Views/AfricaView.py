from Classes.Views.BaseCountriesView import BaseCountriesView

class AfricaView(BaseCountriesView):
    def __init__(self, bot, embed_info, author):
        self.countries = {"Южно-Африканский Союз": "🇿🇦", "Эфиопия": "🇪🇹", "Либерия": "🇱🇷"}

        super().__init__(bot, embed_info, author, self.countries)