from django.db import models


def getObjectById(model: models.model, id: str = None):
    if id is None:
        return model.objects.all()
    try:
        return model.objects.get(pk=id)
    except model.DoesNoteNotExist:
        return None
