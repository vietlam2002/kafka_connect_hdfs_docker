import pyhdfs
import uuid

hdfs = pyhdfs.HdfsClient(hosts="172.19.0.2:9870", user_name="hdfs")

userhomedir = hdfs.get_home_directory()
print(userhomedir)
availablenode = hdfs.get_active_namenode()
print(availablenode)
print(hdfs.listdir("/"))

hdfs.mkdirs('/data')
print(hdfs.list_status('/data'))

def write_to_hdfs(json_str):

    hdfs.create("/data/{}.json".format(str(uuid.uuid1())), json_str)