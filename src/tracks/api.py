

import random
from typing import List, Optional
from ninja import Router, Query
from ninja.pagination import paginate, LimitOffsetPagination, PageNumberPagination
from apitemplate.exceptions import ServiceUnavailableError
from tracks.models import Track
from tracks.schema import NotFoundSchema, TrackFilters, TrackSchema

router = Router()

@router.get("", response=List[TrackSchema])
@paginate(PageNumberPagination, page_size=20)
def tracks(request, filters: Query[TrackFilters]  ):
    tracks = Track.objects.all()
    filtered_tracks = filters.filter(tracks)
    return filtered_tracks

@router.get("/{track_id}", response={200: TrackSchema, 404: NotFoundSchema})
def track(request, track_id: int):
    try:
        return Track.objects.get(id=track_id)
    except Track.DoesNotExist as e:
        return 404, NotFoundSchema(message="Track does not exist")
    

@router.post("", response={201: TrackSchema})
def create_track(request, track: TrackSchema):
    new_track = Track.objects.create(
        title=track.title,
        artist=track.artist,
        duration=track.duration,
        last_play=track.last_play
    )
    return 201, new_track


@router.put("/{track_id}", response={200: TrackSchema, 404: NotFoundSchema})
def change_track(request, track_id: int, data: TrackSchema):
    try:
        track = Track.objects.get(id=track_id)
        for attribute, value in data.dict().items():
            setattr(track, attribute, value)
        track.save()
        return 200, track
    except Track.DoesNotExist as e:
        return 404, NotFoundSchema(message="Track does not exist")
    

@router.delete("/{track_id}", response={204: None, 404: NotFoundSchema})
def delete_track(request, track_id: int):
    if random.choice([True, False]):
        raise ServiceUnavailableError()
    try:
        track = Track.objects.get(id=track_id)
        track.delete()
        return 204, None
    except Track.DoesNotExist as e:
        return 404, NotFoundSchema(message="Track does not exist")