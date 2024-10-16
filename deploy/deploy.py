import fabric
import get_credentials

cred = get_credentials.getServerCredentials()
executableFName = "simple-service"

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

