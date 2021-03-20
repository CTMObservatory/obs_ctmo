# obs_ctmo

This repo contains code to adapt the Cristina Torres Memorial Observatory in
Brownsville, Texas to work with the LSST software stack.

## Generate Test Images

To test the pipeline, you may want to first execute the script to generate the test fake images:

    % python test_data/generate_images.py

This will create a `CTMO_TEST` folder inside `test_data` and generate 3 dark, 3 bias, 3 flat and 3 light frames with random 16-bit integer data.

## Docker Image

The `obs_ctmo` package is under development with version 21 of the docker image of the LSST Software Stack.
We provide a Dockerfile that creates an image with `obs_ctmo` package installed by EUPS.
You can create it, by running:

    % docker build --tag ctmo/lsstpipe:latest .

### Create a Detachable Container

Prepare to run it in [detached mode](https://pipelines.lsst.io/install/docker.html).
Make sure you are in this package folder (`obs_ctmo`) so that `pwd` resolves correctly.

    % docker run -itd --name ctmo \
    -v `pwd`/test_data:/home/lsst/pipe \
    -v `pwd`:/opt/lsst/software/stack/stack/miniconda3-py37_4.8.2-cb4e2dc/Linux64/obs_ctmo/v1 \
    ctmo/lsstpipe:latest

This will create a container from the ctmo image in detached mode.

The two `-v` arguments are optional. The first one mounts the directory with the test data inside the container. The second will mirror the `obs_ctmo` package inside the EUPS manager so that it can immediately pick up the edits when it's changed (useful when debugging).

_Note: Check the `init.sh` that summarizes most of these initial steps._

### Hop In and Out the Detachable Container

From a shell on your host system, open a shell in the container with the docker exec command:

    % docker exec -it ctmo /bin/bash

Your prompt is now a prompt in the container with `obs_ctmo` installed.

You can repeat this process, attaching to the container multiple times, to open multiple container shells.
To close a container shell, terminate the session with `exit`.

To stop the container entirely, run this command from your host’s shell:

    % docker stop ctmo

And delete the container after you no longer need it.

    % docker rm ctmo

### Run LSST Stack Commands

From inside the `ctmo` container:

    $ cd ~/pipe
    $ setup lsst_distrib
    $ setup obs_ctmo
    $ setup -j -r CTMO_TEST
    $ ingestImages.py DATA $CTMO_TEST_DIR/*.fits --mode=link

You should see the ingested images in `~/pipe/DATA` inside the container (`test_data/DATA` in your local machine.)

_Note: These commands are summarized in `test_data/prepare.sh`._

---

(c) CTMO Dev Team
