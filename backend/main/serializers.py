from .models import Apple
from typing import Iterable, List, Dict, Any

def serialize_apples(apples: Iterable[Apple]) -> List[Dict[str, Any]]:
    data = []
    for apple in apples:
        data.append({
            'name': apple.name,
            'color': apple.color,
            'photo_url': apple.photo_url,
        })
    return data

# def serialize_persons(persons: Iterable[Person]) -> List[Dict[str, Any]]:
#     data = []
#     for person in persons:
#         data.append({
#             'name': person.name,
#             'age': person.age,
#         })
#     return data