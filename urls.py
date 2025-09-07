class Urls:
    # Базовый URL
    BASE_URL = "https://qa-scooter.praktikum-services.ru"

    # URL для Dzen
    DZEN_URL = "https://dzen.ru/?yredirect=true"

    @property
    def MAIN_PAGE(self):
        return f"{self.BASE_URL}/"

    @property
    def ORDER_PAGE(self):
        return f"{self.BASE_URL}/order"

    @property
    def ORDER_STATUS_PAGE(self):
        return f"{self.BASE_URL}/track"