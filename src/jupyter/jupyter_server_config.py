c = get_config()
c.ServerApp.ip = '0.0.0.0'
c.ServerApp.port = 8899
c.ServerApp.token = ''
c.ServerApp.password = ''
c.ServerApp.terminado_settings = {'shell_command': ['/usr/bin/zsh']}

# Set environment variables for all kernels
import os
os.environ['SPARK_HOME'] = '/opt/spark'
os.environ['JAVA_HOME'] = '/opt/java/openjdk'
os.environ['PYTHONPATH'] = '/opt/spark/python:/opt/spark/python/lib/py4j-0.10.9.7-src.zip:' + os.environ.get('PYTHONPATH', '')