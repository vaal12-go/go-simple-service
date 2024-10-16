REM standard compilation
docker run -it --name golang-simple-service-image_c1 --rm -v .:/app golang-simple-service-image


REM run with shell
@REM docker run -it --name golang-simple-service-image_c1 --rm -v .:/app --entrypoint sh golang-simple-service-image 