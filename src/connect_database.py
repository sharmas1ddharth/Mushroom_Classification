from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
        'secure_connect_bundle': '..\\Mushroom_Classification\\secure-connect-mushroom.zip'
}
auth_provider = PlainTextAuthProvider('SRYgaGTMQxZDqFhZJXkgdnPo', 'aHuqeol76wj.Q5v7RcQw6hmFp4uExscpCSqff-gM9lo7SGQxktqYsOKCJmpTmPUu+b4OUe1Zx02JF2H.gOITaeUjE5fF.ia,+liDa8W7ndCN0b2.zR,BRQNPI0_Xwh8v')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")