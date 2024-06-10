from datetime import datetime
from typing import Optional

from ninja import Field, FilterSchema, Schema


class TrackSchema(Schema):
    title: str
    artist: str
    duration: float
    last_play: datetime


class NotFoundSchema(Schema):
    message: str


class TrackFilters(FilterSchema):
    title: Optional[str] = Field(None, q="title__icontains")
    artist: Optional[str] = Field(None, q="artist__icontains")
