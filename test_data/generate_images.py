import numpy as np
from astropy.io import fits
import os
import sys

ccd_w, ccd_h = 4096, 4096

run_id = 1

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
out_dir = os.path.join(BASE_DIR, "CTMO_TEST")
if not os.path.exists(out_dir):
    os.mkdir(out_dir)
os.mkdir(os.path.join(out_dir, "ups"))
with open(os.path.join(out_dir, "ups", "ctmo_test.table"), "x"):
    pass

n_darks = 3
for dark_i in range(n_darks):
    img = np.random.randint(-10000, 10000, size=(ccd_h, ccd_w), dtype="int16")
    hdu = fits.PrimaryHDU(img)

    hdu.header["FILTER"] = "None"
    hdu.header["OBJECT"] = "None"
    hdu.header["DATE-OBS"] = "2020-10-11T00:00:00"
    hdu.header["EXPTIME"] = 40.0
    hdu.header["IMAGETYP"] = "Dark Frame"
    hdu.header["RUN-ID"] = run_id

    hdu.scale(type='int16', bzero=32768)
    out_path = os.path.join(out_dir, "dark_{:02d}.fits".format(dark_i + 1))
    hdu.writeto(out_path, overwrite=True)
    run_id += 1


n_bias = 3
for bias_i in range(n_bias):
    img = np.random.randint(-10000, 10000, size=(ccd_h, ccd_w), dtype="int16")
    hdu = fits.PrimaryHDU(img)

    hdu.header["FILTER"] = "None"
    hdu.header["OBJECT"] = "None"
    hdu.header["DATE-OBS"] = "2020-10-11T00:00:00"
    hdu.header["EXPTIME"] = 0.0
    hdu.header["IMAGETYP"] = "Bias Frame"
    hdu.header["RUN-ID"] = run_id

    hdu.scale(type='int16', bzero=32768)
    out_path = os.path.join(out_dir, "bias_{:02d}.fits".format(bias_i + 1))
    hdu.writeto(out_path, overwrite=True)
    run_id += 1


n_flats = 3
for flat_i in range(n_flats):
    img = np.random.randint(-10000, 10000, size=(ccd_h, ccd_w), dtype="int16")
    hdu = fits.PrimaryHDU(img)

    hdu.header["FILTER"] = "i"
    hdu.header["OBJECT"] = "None"
    hdu.header["DATE-OBS"] = "2020-10-11T00:00:00"
    hdu.header["EXPTIME"] = 10.0
    hdu.header["IMAGETYP"] = "Flat Frame"
    hdu.header["RUN-ID"] = run_id

    hdu.scale(type='int16', bzero=32768)
    out_path = os.path.join(out_dir, "flat_{:02d}.fits".format(flat_i + 1))
    hdu.writeto(out_path, overwrite=True)
    run_id += 1


n_lights = 3
for light_i in range(n_lights):
    img = np.random.randint(-10000, 10000, size=(ccd_h, ccd_w), dtype="int16")
    hdu = fits.PrimaryHDU(img)

    hdu.header["FILTER"] = "i"
    hdu.header["OBJECT"] = "NGC4993"
    hdu.header["DATE-OBS"] = "2020-10-11T00:00:00"
    hdu.header["EXPTIME"] = 40.0
    hdu.header["IMAGETYP"] = "Light Frame"
    hdu.header["RUN-ID"] = run_id

    hdu.scale(type='int16', bzero=32768)
    out_path = os.path.join(out_dir, "light_{:02d}.fits".format(light_i + 1))
    hdu.writeto(out_path, overwrite=True)
    run_id += 1
