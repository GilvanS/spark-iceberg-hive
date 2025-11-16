#!/bin/bash
export SPARK_HOME=/opt/spark
export JAVA_HOME=/opt/java/openjdk
export PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.9.7-src.zip:$PYTHONPATH
export PATH=$SPARK_HOME/bin:$SPARK_HOME/sbin:$JAVA_HOME/bin:$PATH

# Install jupyterlab_materialdarker if not already installed
pip install -q jupyterlab_materialdarker

# Start Jupyter Lab
exec jupyter lab --notebook-dir=/opt/notebook --ip='*' --NotebookApp.token='' --NotebookApp.password='' --port=8888 --no-browser --allow-root

