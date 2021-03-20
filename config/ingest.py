from lsst.obs.ctmo.ingest import CtmoParseTask

config.parse.retarget(CtmoParseTask)

config.parse.translation = {
    "filter": "FILTER",
    "object": "OBJECT",
    "run": "RUN-ID",
}
config.parse.translators = {
    "imageType": "translate_imageType",
    "expTime": "translate_expTime",
    "date": "translate_date",
    "dateObs": "translate_dateObs",
    "expId": "translate_expId",
    "detector": "translate_detector",
    "visit": "translate_visit",
}
config.parse.defaults = {
}
config.parse.hdu = 0

config.register.columns = {
    'run': 'text',
    'visit': 'int',
    'filter': 'text',
    'date': 'text',
    'dateObs': 'text',
    'expTime': 'double',
    'detector': 'int',
    'object': 'text',
    'imageType': 'text',
    'expId': 'int',
}

config.register.unique = ["expId", "detector", "visit"]
config.register.visit = ['visit', 'filter', 'dateObs', 'expTime']
