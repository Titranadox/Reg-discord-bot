from Classes.Views.BaseCountriesView import BaseCountriesView


class SouthAmericaView(BaseCountriesView):
    def __init__(self, bot, embed_info, author):
        self.countries = {"Бразилия": "🇧🇷", "Аргентина": "🇦🇷", "Чили": "🇨🇱", "Уругвай": "🇺🇾", "Парагвай": "🇵🇾", "Перу": "🇵🇪",
                          "Эквадор": "🇪🇨", "Венесуэла": "🇻🇪", "Колумбия": "🇨🇴", "Боливия": "🇧🇴"}
        super().__init__(bot, embed_info, author, self.countries)
