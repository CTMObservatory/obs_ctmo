setup lsst_distrib
setup obs_ctmo
setup -j -r CTMO_TEST
ingestImages.py DATA $CTMO_TEST_DIR/*.fits --mode=link
