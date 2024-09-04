# Тестовое задание для бэкенд разработчика на Python

## Задания раздельные, в первой таске нужно просто описать модели.

1. Приложение подразумевает ежедневный вход пользователя, начисление баллов за вход. Нужно отследить момент первого входа игрока для аналитики. Также у игрока имеются игровые бонусы в виде нескольких типов бустов. Нужно описать модели игрока и бустов с возможностью начислять игроку бусты за прохождение уровней или вручную. (Можно написать, применяя sqlachemy)

```
from django.db import models


class Player(models.Model):
    pass
    

class Boost(models.Model):
    pass 
```
2. Дано несколько моделей
```
from django.db import models

class Player(models.Model):
    player_id = models.CharField(max_length=100)
    
    
class Level(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    
    
    
class Prize(models.Model):
    title = models.CharField()
    
    
class PlayerLevel(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    completed = models.DateField()
    is_completed = models.BooleanField(default=False)
    score = models.PositiveIntegerField(default=0)
    
    
class LevelPrize(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    prize = models.ForeignKey(Prize, on_delete=models.CASCADE)
    received = models.DateField()
     
```
Написать два метода:

 * Присвоение игроку приза за прохождение уровня.

 * Выгрузку в csv следующих данных: id игрока, название уровня, пройден ли уровень, полученный приз за уровень. Учесть, что записей может быть 100 000 и более.


# Что было сделано
## Задача 1
* Описание моделей (2 варианта) с использованием Django ORM и SQLAlchemy

## Задача 2
 * Использованы асинхронные функции, так как асинхронный подход может быть более эффективным для обработки больших объемов данных.

* Создана утилите присвоения приза игнроку с учетом предоставленных моделей

* Для выгрузки большого количества данных в CSV использованы  генераторы и асинхронные запросы к базе данных. Это позволит эффективно обрабатывать большое количество записей без загрузки всего в память сразу.
* Созданы утилиты создания CSV файла и выгрузки данных в CSV 


