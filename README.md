```text
                       _____                _   ____  _         _       
                      / ____|              | | |  _ \(_)       | |      
                     | (___   ___ _ __   __| | | |_) |_ _ __ __| |_   _ 
                      \___ \ / _ \ '_ \ / _` | |  _ <| | '__/ _` | | | |
                      ____) |  __/ | | | (_| | | |_) | | | | (_| | |_| |
                     |_____/ \___|_| |_|\__,_| |____/|_|_|  \__,_|\__, |
                                                                   __/ |
                                                                  |___/ 
                                   ___     ___
                                  (o o)   (o o)     Author: Tyler Butler
                                 (  V  ) (  V  )    Site: tbutler.org
                                /--m-m- /--m-m-     @tbutler0x90   
```
# About 
Sendbirdy is an exploitation framework for the Sendbird chat API (https://sendbird.com/). Sendbird is a third-party serivce used by developers to integrate chat and video call features into their application. Sendbirdy uses python to automate HTTP requests to chat end-point API. Depending on the implementation of sendbird is in use, senbirdy can enumerate service users, make authenticated requests to change user data, query accounts and more. 

# Installation 

1) Clone the sendbirdy repository
```bash
git clone https://github.com/tcbutler320/sendbirdy.git
```
2) Install the required packages with pip
```bash
pip install -r requirements.txt
```
3) Launch the sendbirdy python CLI
```bash
python sendbirdy.py --app [Application]
``` 

# Use 
Refer to [modules](#modules) for application specific options 

1) Set workspace path in proj.properties file located in `res`

```properties
# Workspace Settings
WORKSPACE=/test-workspace/
OUTDIR=/Users/tylerbutler/PycharmProjects/SendBird-API-Enumeration/test-workspace/data/
OUTFILE=/Users/tylerbutler/PycharmProjects/SendBird-API-Enumeration/test-workspace/data/output.json
FORMATTEDOUTFILE=/Users/tylerbutler/PycharmProjects/SendBird-API-Enumeration/test-workspace/formatted/
PUTFILE=put.json

# Application Settings

# Instance Settings
CURRENTAPP=DEFAULT
```

2) Run sendbirdy using Hinge module

```python
 python3 sendbirdy.py --app Hinge  
```  
*Results*  

```bash
(venv) ➜  SendBird-API-Enumeration python3 sendbirdy.py --app Hinge 

   _____                _   ____  _         _       
  / ____|              | | |  _ \(_)       | |      
 | (___   ___ _ __   __| | | |_) |_ _ __ __| |_   _ 
  \___ \ / _ \ '_ \ / _` | |  _ <| | '__/ _` | | | |
  ____) |  __/ | | | (_| | | |_) | | | | (_| | |_| |
 |_____/ \___|_| |_|\__,_| |____/|_|_|  \__,_|\__, |
                                               __/ |
                                              |___/ 
               ___     ___
              (o o)   (o o)     Author: Tyler Butler
             (  V  ) (  V  )    Site: tbutler.org
            /--m-m- /--m-m-     @tbutler0x90                                                            

{!}-----[INFO]--- Starting Sendbirdy -----[11/13/2020, 20:31:00]
{!} https://api-3cdad91c-1e0d-4a0d-bbee-9671988bf9e9.sendbird.com/v3/users/
{!}----- Staring sendbirdy round [1]-----
{!}----- Sleeping for 5 seconds [x]-----
{!}----- Gathered [100.0] user details-----
{!}-----[INFO]--- Gathered [100.0] user details-----
{!}-----[INFO]--- Output Located : [/Users/tylerbutler/PycharmProjects/SendBird-API-Enumeration/test-workspace/data/202011132031.json
{!}-----[INFO]--- Output Located : [/Users/tylerbutler/PycharmProjects/SendBird-API-Enumeration/test-workspace/formatted/sendbirdy-202011132031.json
```    

3) Preview results

```bash
(venv) ➜  SendBird-API-Enumeration cat test-workspace/formatted/sendbirdy-202011132031.json
 "users": [
        {
    "created_at": 1605317457,
    "friend_discovery_key": null,
    "friend_name": null,
    "has_ever_logged_in": true,
    "is_active": true,
    "is_online": true,
    "last_seen_at": 0,
    "metadata": {},
    "nickname": "Robert",
    "phone_number": "",
    "preferred_languages": [],
    "profile_url": "https://hinge-res.cloudinary.com/image/upload/v1605317314/f4chksar7dhreec0fbkg.jpg",
    "require_auth_for_profile_image": false,
    "user_id": "2419906019430761589"
},

```
# Result Sets   
Result sets are the gathered information from Sendbirdy. Sendbirdy produces formatted and unformatted result sets. Unformatted output is valid json but is printed as one long string. Formatted output is produced to make it more human readible.   

**Formatted Output** 

```json
{
    "created_at": 
    "friend_discovery_key": 
    "friend_name": 
    "has_ever_logged_in": 
    "is_active": 
    "is_online": 
    "last_seen_at": 
    "metadata": 
    "nickname": 
    "phone_number": 
    "preferred_languages":
    "profile_url": 
    "require_auth_for_profile_image": 
    "user_id": 
 }
```
# Modules
The SendBird Chat API has various forms of implementation including IOS, Android, .Net, Javascript, Unity, and the Platform API. Becuase of this, and because of unique features of the applications used with the API, running sendbirdy is different per app. To hanle this, sendbirdy supports a modules option.   

Modules are YAML formatted files located in the lib.modules package. Each Module comes with a standard set of definitions as well as unique options required for specific apps. The sample format of a module is shown below.

```yaml
 Sample:
   app-name:
   sendbird-id:
   session-token:
   request_limit:
   app_dir_base:
   options:
     can_escape_userdir:
     can_query_userbase:
     can_update_profile:
   headers:
     Accept-Encoding:
     SendBird:
     Request-Sent-Timestamp:
     Accept:
     User-Agent:
     SB-User-Agent:
     Accept-Language:
   ploads:
     public_mode:
     limit:
   url-format:
     urlheader:
     urlTail:
```

## Authentication
Some form of authenticaiton is required by applications using sendbirdy, however, not all applications have the same high standards of secuirty. This repository will not be publically disclosing authentication tokens for applications, however, it is fairly straight forward to capture tokens yourself with burpsuite.

### Capturing Authentication Tokens


# Development Roadmap