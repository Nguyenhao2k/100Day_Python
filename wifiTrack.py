
import subprocess
import re

command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()


profile_names = (re.findall("All User Profile     : (.*)\r", command_output))

#    We create an empty list outside of the loop where dictionaries 
#    containing all the wifi usernames and passwords will be saved.
wifi_list = []

#    If any profile names are not found this means that wifi connections 
#    have also not been found. So we run this part to check the 
#    details of the wifi and see whether we can get their passwords.
if len(profile_names) != 0:
    for name in profile_names:
        #    Every wifi connection will need its own dictionary which 
        #    will be appended to the variable wifi_list.
        wifi_profile = {}
        #    We can now run a more specific command to see the information 
        #    about the wifi connection and if the Security key
        #    is not absent it may be possible to get the password.
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
        #    We use the regular expression to only look for the absent cases so we can ignore them.
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            #    Assign the ssid of the wifi profile to the dictionary.
            wifi_profile["ssid"] = name
            #    These cases aren't absent and we should run the 
            #    "key=clear" command part to get the password.
            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
            #    Again run the regular expression to capture the 
            #    group after the : (which is the password).
            password = re.search("Key Content            : (.*)\r", profile_info_pass)
            #    Check if we found a password using the regular expression. 
            #    Some wifi connections may not have passwords.
            if password == None:
                wifi_profile["password"] = None
            else:
                #    We assign the grouping (where the password is contained) that 
                #    we are interested in to the password key in the dictionary.
                wifi_profile["password"] = password[1]
            #    We append the wifi information to the variable wifi_list.
            wifi_list.append(wifi_profile) 

for x in range(len(wifi_list)):
    print(wifi_list[x]) 
