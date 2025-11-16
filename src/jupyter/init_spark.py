"""
Spark initialization script for Jupyter notebooks
This script should be imported at the beginning of notebooks to ensure
Spark is properly configured.
"""
import os
import sys

# Set environment variables - ensure no newlines or whitespace
os.environ['SPARK_HOME'] = '/opt/spark'
os.environ['JAVA_HOME'] = '/opt/java/openjdk'
os.environ['PYTHONPATH'] = '/opt/spark/python:/opt/spark/python/lib/py4j-0.10.9.7-src.zip:' + os.environ.get('PYTHONPATH', '')

# Add to Python path
if '/opt/spark/python' not in sys.path:
    sys.path.insert(0, '/opt/spark/python')
if '/opt/spark/python/lib/py4j-0.10.9.7-src.zip' not in sys.path:
    sys.path.insert(0, '/opt/spark/python/lib/py4j-0.10.9.7-src.zip')

# Verify paths exist
jars_path = '/opt/spark/assembly/target/scala-2.12/jars'
if not os.path.exists(jars_path):
    raise RuntimeError(f"Spark JARs not found at {jars_path}")

print(f"✓ SPARK_HOME: {os.environ.get('SPARK_HOME')}")
print(f"✓ JAVA_HOME: {os.environ.get('JAVA_HOME')}")
print(f"✓ Spark JARs found at: {jars_path}")

