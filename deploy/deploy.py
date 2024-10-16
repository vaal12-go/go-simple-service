import fabric
import get_credentials

cred = get_credentials.getServerCredentials()
executableFName = "simple-service"
serviceUserName = "vaal12"
serviceDirectoryName = "simple-service"

# TODO: add commands to add user to system

conf = fabric.Config(overrides={'sudo': {'password': cred.password}})
conn = fabric.Connection(host=f"{cred.user}@{cred.host}",
                         connect_kwargs={"password": cred.password},
                         config=conf)

tempDirName = "833ca4b-temp"
conn.run(f"mkdir -p {tempDirName}")

transf = fabric.transfer.Transfer(conn)

transf.put(local=f"..\\linux-artifacts\\{executableFName}",
           remote=f"{tempDirName}/{executableFName}")

conn.run(f"chmod u+x {tempDirName}/{executableFName}")

conn.sudo(f"mkdir -p /opt/{serviceDirectoryName}")
conn.sudo(f"chown {serviceUserName} /opt/{serviceDirectoryName}")
conn.run(f"cp {tempDirName}/{executableFName} /opt/simple-service/{executableFName}")


transf.put(local=f"..\\simple-service.service",
           remote=f"{tempDirName}/simple-service.service")

conn.sudo("systemctl stop simple-service")
conn.sudo(f"cp {tempDirName}/simple-service.service /etc/systemd/system/simple-service.service")
conn.sudo("systemctl daemon-reload")
conn.sudo("systemctl enable simple-service")
conn.sudo("systemctl start  simple-service")

print("\n\n Wating for 5 seconds for service to start\n")
conn.run("systemctl status  simple-service")

print("Deployment of simple-service finished successfully.")


