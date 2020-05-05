import time
import requests
import re
import os
import threading

def Mainf():
    clear()
    x = """
 __   __   _____     ______    __  __     ____   __      __   ______    _____  
 \ \ / /  |  __ \   |  ____|  |  \/  |   / __ \  \ \    / /  |  ____|  |  __ \ 
  \ V /   | |__) |  | |__     | \  / |  | |  | |  \ \  / /   | |__     | |__) |
   > <    |  _  /   |  __|    | |\/| |  | |  | |   \ \/ /    |  __|    |  _  / 
  / . \   | | \ \   | |____   | |  | |  | |__| |    \  /     | |____   | | \ \ 
 /_/ \_\  |_|  \_\  |______|  |_|  |_|   \____/      \/      |______|  |_|  \_\\

- Instagram : @69v2
- Github : @RaghadIsTaken"""
    for char in x:
        print(char, end="")
        time.sleep(0.004)
    print("\n")
    print("1 - Followers Remover")
    print("2 - Following Remover")
    print("3 - Saves Remover")
    print("4 - Posts Remover")
    print("5 - DM Cleaner")
    print("</> * You Can Choose Multiple Options *")
    print("</> * ex (1, 3, 5) *")
    num = str(input("</> "))
    if len(num) == 1:
        clear()
        detect(int(num))
    else:
        clear()
        for x in num.strip().split(","):
            detect(int(x))

def detect(num):
    if num == 1:
        t1 = threading.Thread(target=GetFollowers)
        t1.start()
    elif num == 2:
        t1 = threading.Thread(target=GetFollowing)
        t1.start()
    elif num == 3:
        t1 = threading.Thread(target=GetSaves)
        t1.start()
    elif num == 4:
        t1 = threading.Thread(target=GetPosts)
        t1.start()
    elif num == 5:
        t1 = threading.Thread(target=GetDM)
        t1.start()
    else:
        return
   




#########################################
#########################################
#########################################
#########################################
#########################################
#########################################
#########################################

def Loginer():
    global xname
    xname = input("</> Enter Your Username: ")
    password = input("</> Enter Your Password: ")
    if not login(xname, password):
        Loginer()
        return
    global sleep
    sleep = int(input("</> Enter New Sleep (Default = 30): "))
    Mainf()
    
    

def login(username, password):
    postdata = {
        'username': username,
        'password': password,
    }

    xheaders = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win69; x69) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        'x-csrftoken': 'missing',
        'x-requested-with': 'XMLHttpRequest'
    }

    r = requests.post("https://www.instagram.com/accounts/login/ajax/", data=postdata, headers=xheaders)
    if "authenticated\": true" in r.text:
        global xid, cookies
        session = re.search("sessionid=(.*?);", r.headers['set-cookie'])[1]
        xid = re.search("ds_user_id=(.*?);", r.headers['set-cookie'])[1]
        cookies = "csrftoken=missing; sessionid=" + session + "; ds_user_id=" + xid + "; mid=missing;"
        return True
    else:
        print(r.text)
        return False



#########################################
#########################################
#########################################
#########################################
#########################################
#########################################
#########################################

def GetFollowers():
    while True:
        try:
            xheaders = {
            'Host': 'www.instagram.com',
            'Accept': '*/*',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win69; 69) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
            'X-CSRFToken': 'missing',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cookie': cookies,
        }
            request = requests.get('https://www.instagram.com/graphql/query/?query_hash=c76146de99bb02f6415203be841dd25a&variables={"id":"' + xid + '","include_reel":true,"fetch_mutual":true,"first":50}', headers=xheaders)
            response = request.text
            if '"edge_followed_by":{"count":0,' in response:
                print("• Followers ➝  Finished")
                break
            elif 'id' in response:
                ids = re.findall('{"id":"(.*?)",', response)
                ids = list(set(ids))
                current = int(re.search('"edge_followed_by":{"count":(.*?),', response)[1])
                for id in ids:
                    if Block(id):
                        if UnBlock(id):
                            current -= 1
                            print("• Followers ➝  " + str(current))
                        else:
                            print("• Followers ➝  Blocked : Sleep 10minutes")
                            time.sleep(60 * 10)
                    else:
                        print("• Followers ➝  Blocked : Sleep 10minutes")
                        time.sleep(60 * 10)
                    time.sleep(sleep)
            else:
                print("• Followers ➝  Something is wrong..")
                break
        except Exception as ex:
            print("• Followers ➝  Something is wrong...")
            break
            





def Block(id):
    try:
        xheaders = {
        'Host': 'www.instagram.com',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win69; x69) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        'X-CSRFToken': 'missing',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': cookies,
        'Content-Type': 'application/x-www-form-urlencoded',
           }
        request = requests.post('https://www.instagram.com/web/friendships/' + id + '/block/', headers=xheaders, data="")
        if "ok" in request.text:
            return True
    except Exception as ex:
        pass
    return False

def UnBlock(id):
    try:
        xheaders = {
        'Host': 'www.instagram.com',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win69; x69) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        'X-CSRFToken': 'missing',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': cookies,
        'Content-Type': 'application/x-www-form-urlencoded',
    }
        request = requests.post('https://www.instagram.com/web/friendships/' + id + '/unblock/', headers=xheaders, data="")
        if "ok" in request.text:
            return True
    except:
        pass
    return False
    




#########################################
#########################################
#########################################
#########################################
#########################################
#########################################
#########################################


def GetFollowing():
    while True:
        try:
            xheaders = {
            'Host': 'www.instagram.com',
            'Accept': '*/*',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win69; x69) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
            'X-CSRFToken': 'missing',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cookie': cookies,
            }
            request = requests.get('https://www.instagram.com/graphql/query/?query_hash=d04b0a864b4b54837c0d870b0e77e076&variables={"id":"' + xid + '","include_reel":true,"fetch_mutual":false,"first":50}', headers=xheaders)
            response = request.text
            if 'edge_follow":{"count":0,' in response:
                print("• Following ➝  Finished")
                break
            elif 'id' in response:
                ids = re.findall('{"id":"(.*?)",', response)
                ids = list(set(ids))
                current = int(re.search('edge_follow":{"count":(.*?),', response)[1])
                for id in ids:
                    if UnFollow(id):
                        current -= 1
                        print("• Following ➝  " + str(current))
                    else:
                        print("• Following ➝  Blocked : Sleep 10minutes")
                        time.sleep(60 * 10)
                    time.sleep(sleep)
            else:
                print("• Following ➝  Something is wrong..")
                break
        except:
            print("• Following ➝  Something is wrong...")
            break
                    

def UnFollow(id):
    try:
        xheaders = {
        'Host': 'www.instagram.com',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win69; x69) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        'X-CSRFToken': 'missing',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': cookies,
        'Content-Type': 'application/x-www-form-urlencoded',
    }
        request = requests.post('https://www.instagram.com/web/friendships/' + id + '/unfollow/', headers=xheaders, data="")
        if "ok" in request.text:
            return True
    except:
        pass
    return False



#########################################
#########################################
#########################################
#########################################
#########################################
#########################################
#########################################

def GetSaves():
    while True:
        try:
            xheaders = {
            'Host': 'www.instagram.com',
            'Accept': '*/*',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win69; x69) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
            'X-CSRFToken': 'missing',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cookie': cookies,

        }
            request = requests.get('https://www.instagram.com/graphql/query/?query_hash=8c86fed24fa03a8a2eea2a70a80c7b6b&variables={"id":"' + xid + '","first":50}', headers=xheaders)
            response = request.text
            if 'edge_saved_media":{"count":0,' in response:
                print("• Saves ➝  Finished")
                break
            elif 'id' in response:
                ids = re.findall('{"node":{"id":"(.*?)",', response)
                ids = list(set(ids))
                current = int(re.search('edge_saved_media":{"count":(.*?),', response)[1])
                for id in ids:
                    if UnSave(id):
                        current -= 1
                        print("• Saves ➝  " + str(current))
                    else:
                        print("• Saves ➝  Blocked : Sleep 10minutes")
                        time.sleep(60 * 10)
                    time.sleep(sleep)
            else:
                print("• Saves ➝  Something is wrong..")
                break
        except:
            print("• Saves ➝  Something is wrong...")
            break
                    

def UnSave(id):
    try:
        xheaders = {
        'Host': 'www.instagram.com',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win69; x69) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        'X-CSRFToken': 'missing',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': cookies,
        'Content-Type': 'application/x-www-form-urlencoded',
    }
        request = requests.post('https://www.instagram.com/web/save/' + id + '/unsave/', headers=xheaders, data="")
        if "ok" in request.text:
            return True
    except:
        pass
    return False




#########################################
#########################################
#########################################
#########################################
#########################################
#########################################
#########################################


def GetPosts():
    while True:
        try:
            request = requests.get('https://www.instagram.com/' + xname + '/?__a=1')
            response = request.text
            if '"edge_owner_to_timeline_media":{"count":0,' in response:
                print("• Posts ➝  Finished")
                break
            elif 'id' in response:
                ids = re.findall('","id":"(.*?)",', response)
                ids = list(set(ids))
                current = int(re.search('"edge_owner_to_timeline_media":{"count":(.*?),', response)[1])
                for id in ids:
                    if DeletePost(id):
                        current -= 1
                        print("• Posts ➝  " + str(current))
                    else:
                        print("• Posts ➝  Blocked : Sleep 10minutes")
                        time.sleep(60 * 10)
                    time.sleep(sleep)
            else:
                print("• Posts ➝  Something is wrong..")
                break
        except:
            print("• Posts ➝  Something is wrong...")
            break
                    

def DeletePost(id):
    try:
        xheaders = {
        'Host': 'www.instagram.com',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win69; x69) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        'X-CSRFToken': 'missing',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': cookies,
        'Content-Type': 'application/x-www-form-urlencoded',
    }
        request = requests.post('https://www.instagram.com/create/' + id + '/delete/', headers=xheaders, data="")
        if "ok" in request.text:
            return True
    except:
        pass
    return False



#########################################
#########################################
#########################################
#########################################
#########################################
#########################################
#########################################



def GetDM():
    while True:
        try:
            xheaders = {
            'Host': 'www.instagram.com',
            'Accept': '*/*',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win69; x69) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
            'Referer': 'https://www.instagram.com/direct/inbox/',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cookie': cookies,

            }
            request = requests.get('https://www.instagram.com/direct_v2/web/inbox/?persistentBadging=true&folder=&limit=100', headers=xheaders)
            response = request.text
            if '"threads" : [],' in response:
                print("• DM ➝  Finished")
                break
            elif 'thread_id' in response:
                ids = re.findall('"thread_id": "(.*?)",', response)
                ids = list(set(ids))
                for id in ids:
                    if DeleteDM(id):
                        print("• DM ➝  One DM Was Deleted Successfully")
                    else:
                        print("• DM ➝  Blocked : Sleep 10minutes")
                        time.sleep(60 * 10)
                    time.sleep(sleep)
            else:
                print("• DM ➝  Something is wrong..")
                break
        except:
            print("• DM ➝  Something is wrong...")
            break


def DeleteDM(id):
    try:
        xheaders = {
            'Host': 'www.instagram.com',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win69; x69) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': 'missing',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cookie': cookies,
        }
        request = requests.post('https://www.instagram.com/direct_v2/web/threads/' + id + '/hide/', headers=xheaders, data="")
        if "ok" in request.text:
            return True
    except:
        pass
    return False



token = 'Instagram : @69v2'
cookies = 'Github : @RaghadIsTaken'
xid = 'Instagram : @69v2'
xname = 'Github : @RaghadIsTaken'
sleep = 30


#Utils

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

Loginer()






