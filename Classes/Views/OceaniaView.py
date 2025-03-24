from Classes.Views.BaseCountriesView import BaseCountriesView


class OceaniaView(BaseCountriesView):
    def __init__(self, bot, embed_info, author):
        self.countries = {"Австралия": "🇦🇺", "Новая Зеландия": "🇳🇿", "Филиппины": "🇵🇭"}
        super().__init__(bot, embed_info, author, self.countries)