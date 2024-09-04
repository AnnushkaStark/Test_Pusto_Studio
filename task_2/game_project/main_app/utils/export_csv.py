import asyncio
import csv
from io import StringIO

import aiofiles
from django.db.models import F
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from ..models import PlayerLevel


async def create_csv_file(filename: str):
    default_storage.save(filename, ContentFile(b""))
    async with aiofiles.open(
        default_storage.path(filename), mode="w", encoding="utf-8"
    ) as f:
        csv_data = await export_to_csv()
        await f.write(csv_data)


async def export_to_csv():
    output = StringIO()
    writer = csv.writer(output)
    header = ["Player ID", "Level Title", "Completed", "Prize"]
    writer.writerow(header)
    query = (
        PlayerLevel.objects.select_related("player", "level")
        .annotate(prize_title=F("level__levelprize__prize__title"))
        .values_list("player__player_id", "level__title", "is_completed", "prize_title")
    )
    async for result in query.iterator():
        writer.writerow(result)

    output.seek(0)
    return output.getvalue()
