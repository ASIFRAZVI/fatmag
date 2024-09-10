Developer Guide:-

Overview:
The fatmag Video-Gallery app developded to Extract Subtitles from videos.

Configuration steps -

1. Download the provided link docs zip
   1. Folder link - https://drive.google.com/drive/folders/11gZlIDAes98WwPle3wFlaluKE_fMOiy2?usp=sharing
   2. Extract all 
   3. rename to "CCExtracror_tools" !importent
   4. copy renamed folder and paste in projects "package_dir" folder (eg = locate package_dir in root dir and paste CCExtracror_tools)


2. create .env and add following env variables, (Note- < or >this operators only from representation)

SECRET_KEY= <Django Secrate key || Any Random String>

db_mode= <dev || prod> #if dev setup dev database or if mode is prod then setup the prod db in env

DEBUG = <True || False> #if DEBUG=False then setup the allowed hosts in settings.congig "allowed_hosts"

<!-- if db_mode is dev -->

DEV_DB_ENGINE =django.db.backends.postgresql
DEV_DB_NAME = <Database-name>
DEV_DB_USER = <db-user>
DEV_DB_PASSWORD = <db-user-password>
DEV_DB_HOST = <db-host>
DEV_DB_PORT = <db-port>

<!-- if db_mode is prod -->

PROD_DB_ENGINE =django.db.backends.postgresql
PROD_DB_NAME = <Database-name>
PROD_DB_USER = <db-user>
PROD_DB_PASSWORD = <db-user-password>
PROD_DB_HOST = <db-host>
PROD_DB_PORT = <db-port>

3. run start.bat using cmd
   -command prompt -> Enter -> start.bat

4. Access api documentation by visiting url
   path = http://localhost:8000/api/schema/swagger-ui/

5. download sample videos by clicking below links and upload this through postman (in swagger this create api is not exutable)

- test videos links
  test-vid1 = https://drive.google.com/file/d/1DVjQdtb6qxzVJTYt9CAd8X_kgaIK6CMl/view?usp=sharing
  test-vid2 = https://drive.google.com/file/d/1yl6-jPwEuMgvUNf9rJ8hRh6zGi5i-36Y/view?usp=sharing

- api to upload video
  url -=- http://localhost:8000/api/video/
  Method = post
  form data-
  video_file(KEY)= File(value) #upload the above sample videos or any valid supported videos
  title(KEY)=text(Value)  
  description(KEY)=text(Value)

  - response-
    200 ok video uploaded and subtitle extracted!

  - Error code
    400 error please upload valid video format!

NOTE 1- for other all APIs please refer swagger UI (Step 4)

Note 2 - After setting up all configuration you can use docker compose(optional).

-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_THANK YOU!-:)-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
