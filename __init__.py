# Initial Copyright (c)2023 M4L
# The CalibrationShapes plugin is released under the terms of the AGPLv3 or higher.

from . import Models

def getMetaData():
    return {}

def register(app):
    return {"extension": Models.Models()}
