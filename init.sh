python test_data/generate_images.py
docker build --tag ctmo/lsstpipe:latest .
docker run -itd --name ctmo \
-v `pwd`/test_data:/home/lsst/pipe \
-v `pwd`:/opt/lsst/software/stack/stack/miniconda3-py37_4.8.2-cb4e2dc/Linux64/obs_ctmo/v1 \
ctmo/lsstpipe:latest
