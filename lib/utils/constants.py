# Constants
app = None
interactive_mode = False
verbose = False
output_filename = False
app_id = None            # App ID of the application you are testing
session_token = "c600ca619bf36c3c92a2d0586a0bf20ce5b1b08b"     # A valid session key, can be option through burp intercept
request_limit = 100                                          # 100 is the default limit for maximum amount of respones allowed per GET request
users_to_enumerate = 100                                      # set the total number of responses you want to receive, must be a multiple of 10
ploads = {                                                  # Define Parameters to Pass in the URL
    'public_mode': 'all'
}
data = ""
filePath = 'formatted.txt';
filePath2 = 'demofile2.json';
output_filename = "sendbirdy.json"
sendBirdyHeader = """
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
""";

usage = (
    "{!}-----[Usage]--- Usage:python sendbirdy.py -i [app-id] -t [session-token] -o [options] -out [output file]\n"
    "{!}-----[Help]------  -h --help    : Print the help page\n"
    "{!}-----[APP]---  -p --app : Use App settings defined in proj.properties file\n"

    "{!}-----[APP-ID]---  -i --id : Set the SendBird Application ID for the platform your searching\n"
    "{!}-----[APP-ID][Supported]\n"
    "                |[Hinge]    api: api-3cdad91c-1e0d-4a0d-bbee-9671988bf9e9 \n"
    "                |[Reddit]   api: api-3cdad91c-1e0d-4a0d-bbee-9671988bf9e9 \n"
    "{!}-----[SESSION-TOKEN]---  -t --token: A valid session token, see research paper on obtaining with burp\n"
    "{!}-----[Options]--- : Supported options included ... \n"
    "                |[enum]-- -e --enum-all: enumrate all users of the application \n"
    "                |[check-enum]-- -ce --check-enum: test if the session token includes permissions to run enmum \n"
    "                |[check-put]-- -cp --check-put: check if you have permission to put data to sendbird api\n"
    "                |[put-data]-- -cp --check-put: check if you have permission to put data to sendbird api\n")

errorMsg = "{!}-----[ERROR] You did not supply the correct arguments\n";
askForHelp = "{!}-----[ERROR] use --help for help with usage\n";
indent_msg = "{!}-----"
indent_err = "[ERROR]---"
indent_info = "[INFO]---"
warn_err = "[WARN]---"