##########################
#  Описание моделей с    #
#   использованием       #
#    DJANGO ORM          #
##########################
from django.db import models


class Player(models.model):
    """
    Модель игрока

    ## Attrs:
        - username: str - Юзернейм поользователя
        - firsrname: str - Имя пользовтаеля
        - lastname: str - Фамилия пользователя
        - email: str - Электронная почта пользователя
        - hash_password: str - Хэш пароля пользователя
        - last_login: datetime - Время последнего
            входа в систему для статистики
        - boosts: Boost m2m - связь награды
             полученные пользователем
    """

    username = models.CharField(max_length=100)
    firstame = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    hash_password = models.CharField()
    last_login = models.DateTimeField(auto_now_add=True)
    boosts = models.ManyToManyField("Boosts", related_name="boosted_players")

    def __str__(self):
        return f"{self.username} {self.firstname} {self.lastname}"


class Boost(models.Model):
    """
    Модель буста

    ## Attsrs:
        - description: str - описание буста
        - players: M2M связь пользователи
            получившие буст
    """

    description = models.CharField(max_length=100)
    players = models.ManyToManyField(Player)

    def __str__(self):
        return f"{self.name}"
