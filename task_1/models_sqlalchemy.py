##########################
#  Описание моделей с    #
#   использованием       #
#   SQLAlchemy           #
##########################

from datetime import datetime
from typing import List

from sqlalchemy import ForeignKey, Integer, String, Text, DateTime, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.sql.sqltypes import ARRAY, Integer, String


class Base(DeclarativeBase):
    type_annotation_map = {
        list: ARRAY,
        list[str]: ARRAY(String),
        list[int]: ARRAY(Integer),
    }


class Player(Base):
    """
    Модель игрока

    ## Attrs:
        - id: int - идентификатор пользователя
        - username: str - Юзернейм поользователя
        - firsrname: str - Имя пользовтаеля
        - lastname: str - Фамилия пользователя
        - email: str - Электронная почта пользователя
        - hash_password: str - Хэш пароля пользователя
        - last_login: datetime - Время последнего
            входа в систему для статистики
        - boosts: List[Boost] m2m - связь награды
             полученные пользователем
    """

    __tablename__ = "player"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True)
    firantame: Mapped[str]
    lastname: Mapped[str]
    email: Mapped[str]
    hash_password: Mapped[str]
    last_login: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    boosts: Mapped[List["Boost"]] = relationship(
        "Boost", back_populates="players", secondary=BoostedUsers.__table__
    )

    def __repr__(self):
        return f"{self.username} {self.firstname} {self.lastname}"


class Boost(Base):
    """
    Модель буста

    ## Attsrs:
        - id: int - идентификатор пользователя
        - description: str - описание буста
        - users: List[Player] M2M связь пользователи
            получившие буст
    """

    __tablename__ = "boost"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    descripton: Mapped[str] = mapped_column(Text)
    players: Mapped[List["Player"]] = relationship(
        "Player", back_populates="boosts", secondary=BoostedUsers.__table__
    )

    def __repr__(self):
        return f"{self.description}"


class BoostedUsers(Base):
    """
    Модель связи м2м - пользователи
    получившие буст
    ## Attrs:
        -  boost_id: int - идентификатор
            буста
        -  user_id : int - идентификатор игрока


    """

    __tablename__ = "boosted_users"

    boost_id: Mapped[int] = mapped_column(
        ForeignKey("boost.id", ondelete="CASCADE"),
        primary_key=True,
    )
    player_id: Mapped[int] = mapped_column(
        ForeignKey("player.id", ondelete="CASCADE"),
        primary_key=True,
    )
