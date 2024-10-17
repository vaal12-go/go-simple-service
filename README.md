# Go-simple-service

This is a skeleton application which provides necessary components for linux service (systemd).

In this repository following components are provided:

1. Golang service application (simple loop which prints every 5 seconds a message to console). Also it reacts to system messages (so it can be gracefully stopped by systemd daemon). 
1. linux-artifacts/Dockerfile for compiling linux executable on windows machine.
1. compile_for_linux.bat file for invoking docker image to compile linux application on windows machine (resulting simple-service executable will be placed to linux-artifacts folder)
1. simple-service.service file which is needed for systemd to manage service. It has to be synchronized with deploy.py manually at the moment (linux user, under which service is run, ExecStart executable name)
1. deploy/deploy.py python script to install service on remote machine with ssh enabled. At the moment only password authentication is supported.

## Tested OSes
Ubuntu server 22.04.5 LTS

TODO: 
1. Add SSH keyfile authentification
1. Add generation of .service file based on python variables (at the moment .service file and deploy.py have to be synchronized manually)
1. Test on more linux versions (at least ubuntu server 24.04.1 LTS and 20.04.6 LTS)
    
    