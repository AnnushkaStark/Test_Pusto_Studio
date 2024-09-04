from datetime import datetime

from ..models import Player, PlayerLevel, Level, LevelPrize


async def assign_prize(player_id: str, level_id: int):
    try:
        player = await Player.objects.aget(id=player_id)
        level = await Level.objects.aget(id=level_id)
        player_level = await PlayerLevel.objects.get_or_create(
            player=player,
            level=level,
        )
        if not player_level.is_complited:
            level_prize = await LevelPrize.objects.filter(level=level).first()
            if level_prize:
                player_level.is_completed = True
                player_level.completed = datetime.now()
                await player_level.save()
                await LevelPrize.objects.create(
                    level=level,
                    prize=level_prize.prize,
                    received=datetime.now(),
                )
                return (
                    f"Приз за уровень '{level.title}' присвоен игроку с id {player_id}"
                )
            else:
                return f"Для уровня '{level.title}' не назначен приз"
        else:
            return f"Игрок с id {player_id} уже прошел уровень '{level.title}'"
    except Player.DoesNotExist:
        return f"Игрок с id {player_id} не найден"
    except Level.DoesNotExist:
        return f"Уровень с id {level_id} не найден"
    except Exception as e:
        return f"Произошла ошибка: {str(e)}"
