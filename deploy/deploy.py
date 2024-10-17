import fabric
import get_credentials
import time
import uuid

cred = get_credentials.getServerCredentials()
executableFName = "simple-service"
serviceUserName = "simple-service-user"
serviceDirectoryName = "simple-service"
tempDirName = str(uuid.uuid4())[-12:]+"-temp"

print("Simple-service deployment script. v1.0_17Oct2024")

conf = fabric.Config(overrides={'sudo': {'password': cred.password}})
conn = fabric.Connection(host=f"{cred.user}@{cred.host}",
                         connect_kwargs={"password": cred.password},
                         config=conf)

res = conn.run(f"id -u {serviceUserName}", warn=True)

if "no such user" in res.stderr:
    conn.sudo(f"useradd --shell /bin/false --system {serviceUserName}")
    conn.sudo(f"usermod -L {serviceUserName}")
else:
    print(f"{serviceUserName} user exists")


conn.run(f"mkdir -p {tempDirName}")

transf = fabric.transfer.Transfer(conn)

transf.put(local=f"..\\linux-artifacts\\{executableFName}",
           remote=f"{tempDirName}/{executableFName}")

transf.put(local=f"..\\simple-service.service",
           remote=f"{tempDirName}/simple-service.service")


conn.sudo("systemctl stop simple-service")
print("Waiting for service to stop")
time.sleep(5)#waiting for the service to stop
conn.run(f"chmod u+x {tempDirName}/{executableFName}")
print("Before copying")
conn.sudo(f"mkdir -p /opt/{serviceDirectoryName}")
conn.sudo(f"cp {tempDirName}/{executableFName} /opt/{serviceDirectoryName}/{executableFName}")
print("After copy")

conn.sudo(f"chown {serviceUserName} /opt/{serviceDirectoryName}")
conn.sudo(f"chown {serviceUserName} /opt/{serviceDirectoryName}/{executableFName}")
# TODO: change cp to move file here and for .service file


conn.sudo(f"cp {tempDirName}/simple-service.service /etc/systemd/system/simple-service.service")
conn.sudo("systemctl daemon-reload")
conn.sudo("systemctl enable simple-service")
conn.sudo("systemctl start  simple-service")


conn.run(f"rm -r {tempDirName}")

print("\n\n Wating for 10 seconds for service to start\n")
time.sleep(10)  
res = conn.run("systemctl status  simple-service")

if "Active: active (running)" in res.stdout:
    print("Deployment of simple-service finished successfully.")
else:
    print("Something wrong with deployment. Service does not seem to be active(running)")


