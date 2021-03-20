from lsst.pipe.tasks.ingest import ParseTask
from astropy.time import Time


class CtmoParseTask(ParseTask):
    """[From https://github.com/lsst/obs_lsst/blob/f0c4ae506e8e0a85789aebdd970d7e704c9c6e24/
    python/lsst/obs/lsst/ingest.py#L54]:
    All translator methods receive the header metadata [here via "md"] and
    should return the appropriate value, or None if the value cannot be determined.
    """

    def translate_date(self, md):
        "Convert date format from yyyy-mm-ddThh:mm:ss to yyyy-mm-dd."
        date = md.get("DATE-OBS")
        t = Time(date, out_subfmt="date").isot
        return t

    def translate_dateObs(self, md):
        "Convert date format from yyyy-mm-ddThh:mm:ss to yyyy-mm-dd."
        date = md.get("DATE-OBS")
        t = Time(date, out_subfmt="date").isot
        return t

    def translate_imageType(self, md):
        datatype = md.get("IMAGETYP")
        if "dark" in datatype.lower():
            return "dark"
        if "flat" in datatype.lower():
            return "flat"
        if "bias" in datatype.lower():
            return "bias"
        if "light" in datatype.lower():
            return "light"
        return "unknown"

    def translate_expTime(self, md):
        "Convert string 'expTime' from FITS header into float"
        return float(md.get("EXPTIME"))

    def translate_visit(self, md):
        "Convert string 'visit' from FITS header into integer"
        return int(md.get("RUN-ID"))

    def translate_expId(self, md):
        return int(md.get("RUN-ID"))

    def translate_detector(self, md):
        return 0
