import os 
try:
    from requests import post,get
    from time import sleep
    import json
    import getpass
except ModuleNotFoundError as err:
    os.system('pip install '+err)
    

u = ("""\033[36m
⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠄⠒⠤⢄⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⡤⠚⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣋⠁⠈⠻⣷⡄⠙⣷⣦⡾⢛⡿⠶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡠⠋⠀⡠⠊⠁⠀⠀⠀⠀⠀⠀⢀⡠⠾⠯⣭⣒⢯⣕⣲⣬⣿⣆⠸⣿⣴⣗⡒⢤⡀⠹⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡽⠣⢄⠞⠀⠀⠀⠀⠀⠀⠀⠀⣰⣯⣶⣿⣉⣩⠝⠛⠛⠋⠛⠿⢿⠀⣿⠇⠸⠛⢆⢹⣦⢜⡞⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠃⠀⡌⠁⠀⠀⠀⠀⠀⠀⠀⣸⣫⣵⣾⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠆⢻⡟⢿⡺⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀
⠀⠠⠁⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⡾⢋⠀⠀⡆⠀⡀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠘⡘⣿⣎⣧⡈⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣽⣿⠟⡏⠀⢰⠇⢀⡧⠤⠧⠀⠀⠒⢒⣨⢵⠶⠑⢀⣀⣇⢹⣟⣯⣻⡜⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⡿⣘⡇⠀⠜⠀⣼⠟⠛⠻⠿⢿⣭⠁⠂⡡⠖⠉⢀⠞⢻⢸⣿⣇⠹⣧⠻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⡆⠀⠀⠀⠀⠀⠀⠀⣼⠇⣰⣯⣽⣿⣄⠔⢋⣹⣷⣄⣀⠀⠀⣋⣷⢼⣁⣠⠞⠓⠒⢾⢸⣏⢻⣻⣿⣾⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀
⠀⢱⠀⠀⠀⠀⠀⠀⢠⡟⢰⣿⣿⡟⢬⣏⣶⡻⠛⠛⢷⣿⣿⣿⣿⣶⢶⣿⡿⠭⠭⠽⢻⣼⣿⣄⡇⣇⣟⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀
⠀⠈⡄⠀⠀⠀⠀⠀⣼⠃⣼⠏⣿⡋⢩⠿⣯⠭⣽⣉⠽⠚⢉⠁⠁⠸⠼⠸⣌⠑⠒⠀⢀⡿⢣⣸⣇⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀
⠀⠀⡇⠀⠀⠀⠀⡼⡟⠀⣿⣴⣸⡟⠁⠀⠙⠦⣨⣇⣀⠤⠋⠀⠀⠀⠀⡆⠈⠑⠒⠒⢸⡇⠀⢿⣿⡿⡏⢇⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀
⠀⠀⡇⠀⠀⠀⠀⣣⡇⠀⣧⡟⣟⢿⠀⠀⠀⠀⢸⣧⠄⠀⠀⠀⣠⢤⣤⣖⣀⣀⣰⡦⢼⣥⡆⢸⢻⣷⣷⠈⠲⠤⢤⡀⠀⠀⠀⣀⠇⠀
⠀⢀⠃⠀⡠⠔⠊⡩⠿⡄⢿⡌⣿⣜⣇⣠⣾⣿⣿⣗⣛⣟⣛⣊⠿⠯⠤⠍⠉⠀⠒⠒⠻⣿⡅⢺⣿⣾⢹⢳⣴⡒⢢⢹⣀⣀⣀⠙⠻⣆
⠀⢸⢀⠞⠓⠦⣯⠄⠀⣿⣿⡘⢮⡻⡇⢺⣿⣏⠛⠀⠁⣀⣀⣤⣤⣤⣶⣶⣶⣦⣤⣄⣀⡿⣇⢸⡿⣧⡻⣮⡉⢻⡾⣏⡁⠈⠉⠙⢦⡙
⠀⣻⣿⠂⠀⢰⡿⢀⡴⢻⠇⢸⣎⢿⣿⡈⠇⡏⢷⣶⣿⠟⠋⠉⠉⠀⠀⠈⠉⠉⠻⢿⡿⡀⢹⣿⡇⠈⣹⠇⢈⣽⠗⢦⣹⡦⠀⠀⠀⢹
⣀⡟⠁⠀⠀⢸⠃⡾⡔⠁⣰⠕⢿⠘⣿⣷⣄⠀⢀⠻⣍⣀⡠⠤⠤⠄⠒⠒⠀⢐⣰⠞⡱⠁⢸⣿⣇⠸⡋⠻⢅⣯⣴⣿⡟⢿⠀⠀⠀⢸
⣿⠁⠀⠀⠀⢸⣆⠳⢧⣀⠹⣦⡞⣶⡇⢻⣏⠣⡀⠱⣌⡓⠒⠂⠐⠒⠒⠂⢉⣁⣠⣴⠁⢠⣿⣿⣿⣦⣝⢆⠀⠈⣿⣿⠃⢸⠃⠀⠀⣾
⣿⣇⠀⠀⠀⠀⣿⡿⡙⣌⣷⣼⡷⣿⣷⠀⢿⣧⠹⡎⢸⠉⠙⡿⡏⠉⡟⡏⠙⡼⡄⢋⢳⣿⣿⣿⣿⣿⠟⣸⣀⠴⢛⡏⢀⡏⠀⠀⢀⠯
⠻⣿⣆⠀⠀⠀⠘⣷⡙⠿⢏⢹⣧⣿⣿⣇⠈⢿⠇⠁⢸⠀⠀⠀⡇⠀⡇⢡⠀⡇⢱⢸⠀⠛⣿⣿⣿⣵⣾⣿⠋⢠⠎⢀⡟⠀⠀⢠⠊⢀
⠛⠻⢿⣷⣤⡀⠀⠈⠻⣄⠈⢻⣰⣽⠃⣾⠀⢸⠀⠀⠈⠳⠶⠀⢷⣤⠇⠸⠷⠃⠈⠋⠀⣼⣿⣿⢻⡟⣿⡿⡔⠁⢀⡞⠀⠀⡰⠃⣠⢞
⠛⠲⠬⠉⢉⣹⣦⣄⣀⠈⠂⠀⠹⣿⣾⡟⠀⢺⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡽⢠⡿⢻⣃⣿⠞⢀⣴⠋⠀⣠⠞⢁⣾⣏⡾
⣠⠤⠔⢺⠁⢀⠏⠈⢿⣻⡿⣶⣦⠈⣿⣴⣲⠈⠿⣇⢀⠀⠀⡄⠀⡀⠀⡀⠰⡴⡰⣤⣼⣷⡟⠀⣾⣿⠏⢠⡟⠁⣠⡾⣋⢾⣿⡿⠋⠀
⠀⠀⠀⠘⠒⠁⠀⢀⣾⣿⣿⣿⣿⡃⣈⠻⣄⠀⠀⠻⣼⣴⣆⣃⡇⢹⣆⣆⢠⣿⣷⣽⡟⠛⠂⠀⣿⠏⢠⡟⢠⣾⣿⠟⣱⡿⠋⠀⠀⢀
⠀⠀⢀⣀⣀⣠⣴⣿⣇⣽⣿⣿⣿⠁⠈⠓⣿⣧⣀⠀⠀⠸⣿⣿⣿⣾⣿⣿⣿⣿⣿⡟⠀⠀⠀⣰⡏⣰⣟⣴⣿⠟⢁⣴⠋⠀⢀⣠⣶⣿
\033[32m
               by: @BBZZS in telegram\033[0m
       """)
print(u)

class MyClass: 
    def __init__(self):
        self.ask_time=int(input("set how many times to unfollow:  "))
        self.ask_following=int(input("The number of unfollows until the sleep you set is executed:  "))
        
        self.bad=0
        self.NO=0
        self.done = 0
        self.ban = 0
        self.unfolowing=0
        self.backred= '\033[41m'
        self.bigline="\033[1m"
        self.red="\033[31m"
        self.purple="\033[35m"
        self.offcolor="\033[0m"
        try:
            with open("info-acc.json", "r") as file:
                try:
                    self.data = json.load(file)
                    if 'appid' in self.data:
                        self.get_following_id()
                except json.JSONDecodeError:
                    with open("info-acc.json", "w") as file:
                            daata = ""
                            json.dump(daata, file)
                            self.login()
        except FileNotFoundError:
                # إذا لم يتم العثور على الملف، قم بإنشاءه
                with open("info-acc.json", "w") as file:
                    daata = ""
                    json.dump(daata, file)
                    self.login()

    def save_info_acc(self):
        ss = {
                        "username": self.user,
                        "password": self.password,
                        "ses": self.ses,
                        "csr": self.csrftoken,
                        "id": self.userid,
                        "appid": self.appid
                        }
        with open('info-acc.json', 'w') as f:
            json.dump(ss,f)
    def login(self):
            print(self.purple+self.bigline+"start")
            rw = post("https://www.instagram.com/logging/falco",headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    })
            self.token=str(rw.cookies['csrftoken'])
            print(self.token)
            self.user= input("Enter your username:  ")
            self.password = getpass.getpass("Enter your password:  ")
            url = "https://www.instagram.com/api/v1/web/accounts/login/ajax/"
            headers = {
                'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
    'content-length': '295',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': f'mid=ZEcYCQALAAHQtLAJc-1zEazpOj1I; ig_did=D9FBC01E-879C-4064-ACFF-775DB19CA7FF; ig_nrcb=1; datr=BxhHZHz9IX4mqSYvbWIONw6M; shbid="9450\05431850092326\0541721664008:01f784d8cf42e06bfbbf04341ee6223e73ac8973ac567e022f273d8c5896722fb950eff8"; shbts="1690128008\05431850092326\0541721664008:01f7cd78546d9d3f8e14fcd210b0f7061977bee8470f40782273038ffdd7ba0e49aa0eba"; csrftoken={self.token}',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'viewport-width': '1040',
    'x-asbd-id': '129477',
    'x-csrftoken': self.token,
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1007887911',
    'x-kl-kfa-ajax-request': 'Ajax_Request',
    'x-requested-with': 'XMLHttpRequest',
            }
            data = {'enc_password': '#PWD_INSTAGRAM_BROWSER:0:&:'+self.password,
                'optIntoOneTap': 'false',
                'queryParams': '{}',
                'trustedDeviceRecords': '{}',
                'username': self.user,

            }
            r = post(url, data=data, headers=headers)
            
            if '"userId"' in r.text: 
                self.csrftoken = str(r.cookies['csrftoken']) 
                self.ses = str(r.cookies['sessionid']) 
                
                
                self.appid = '936619743392459' 
                tt = r.text 
                dataa = json.loads(tt) 
                self.userid = dataa['userId'] 
                self.save_info_acc()

                print("your userid: "+self.userid) 
                self.get_following_id() 
            if '"message":""' in r.text:
                print(self.red+self.bigline+"There was an error, try again later "+self.offcolor)
                sleep(50)
                exit()
            if '"authenticated":false' in r.text:
                print(self.red+self.bigline+"username or password incorrect"+self.offcolor)
                sleep(50)
                exit()
            else:
                print(self.backred+r.text+self.offcolor)
                exit()
            
        
    def get_following_id(self):
        with open("info-acc.json", "r") as file:
                self.data = json.load(file)
        self.ses = self.data["ses"]
        self.csrftoken = self.data["csr"]
        self.appid = self.data["appid"]
        self.userid = self.data["id"]
        self.user = self.data["username"]
        url = f"https://www.instagram.com/api/v1/friendships/{self.userid}/following/?count=12"
        headers = { 
    "Accept": "*/*", 
    "Referer": f"https://www.instagram.com/{self.user}/following/", 
    "sec-ch-prefers-color-scheme": "light",
    "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"", 
    "sec-ch-ua-full-version-list": "\"Not.A/Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"114.0.5735.248\", \"Google Chrome\";v=\"114.0.5735.248\"", 
    "sec-ch-ua-mobile": "?0", 
    "sec-ch-ua-platform": "\"Windows\"", 
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    'cookie': f'mid=ZEcYCQALAAHQtLAJc-1zEazpOj1I; ig_did=D9FBC01E-879C-4064-ACFF-775DB19CA7FF; ig_nrcb=1; datr=BxhHZHz9IX4mqSYvbWIONw6M; shbid="9450\05431850092326\0541721664008:01f784d8cf42e06bfbbf04341ee6223e73ac8973ac567e022f273d8c5896722fb950eff8"; shbts="1690128008\05431850092326\0541721664008:01f7cd78546d9d3f8e14fcd210b0f7061977bee8470f40782273038ffdd7ba0e49aa0eba"; ds_user_id={self.userid}; sessionid={self.ses}; csrftoken=EPCnYSUmlMlOrarVyv7jY06dpDHJs0Uj; rur="CLN\05449441374693\0541721831165:01f7d586f0f7ab6d5fdc829d4a3bc4dc158a1ea78796bf1f59877573ef73953b3251e701"', 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36", 
    "viewport-width": "1040", 
    "X-ASBD-ID": "129477", 
    "X-CSRFToken": "EPCnYSUmlMlOrarVyv7jY06dpDHJs0Uj", 
    "X-IG-App-ID": "936619743392459", 
    "X-IG-WWW-Claim": "hmac.AR2gTCJERHJMjTV94sTc-eWCNMcG8labBdiZ0T-SETSLuz1w", 
    "X-KL-kfa-Ajax-Request": "Ajax_Request", 
    "X-Requested-With": "XMLHttpRequest" 
}
        data={'count': '12'}
        r = get(url, data=data,headers=headers).text
        while True:
            try: 
                def error():
                    print(self.red+self.bigline+'\nu need to wait for 2m and run again, or clear info-acc.json and try again'+self.offcolor)
                    print(self.backred+r+self.offcolor)
                    sleep(120)
                    pass
                if '"Please wait a few minutes before you try again."' in r:
                    error()
                if '"spam":true' in r:
                    error()
                if '"users"' in r:
                    dataa = json.loads(r)
                    self.follow_id = dataa['users'][self.NO]['pk_id']
                    self.use = dataa['users'][self.NO]['username']
                    self.unfolow()
                    self.NO+=1
                    self.unfolowing+=1
                    if self.NO==12:
                        self.NO=0 
                        r = get(url, data=data,headers=headers).text                
            except IndexError:
                print("DONE UNfollowing all"+self.offcolor)
                sleep(50)
                exit()
                

    def unfolow(self): # Here it is unfollowed
        if self.unfolowing == self.ask_following:  
            print(self.red+"sleep time sir", end="\r")
            self.unfolowing=0
            sleep(self.ask_time)
            pass               
        else:
            url = f"https://www.instagram.com/api/v1/friendships/destroy/{self.follow_id}/"
            headers = {
                            'accept': '*/*',
                            'accept-encoding': 'gzip, deflate, br',
                            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                            'content-length': '106',
                            'content-type': 'application/x-www-form-urlencoded',
                            'cookie': f'mid=ZEcYCQALAAHQtLAJc-1zEazpOj1I; ig_did=D9FBC01E-879C-4064-ACFF-775DB19CA7FF; ig_nrcb=1; datr=BxhHZHz9IX4mqSYvbWIONw6M; ds_user_id={self.userid}; csrftoken=EPCnYSUmlMlOrarVyv7jY06dpDHJs0Uj; shbid="15628\05449441374693\0541721923272:01f707fb99815378080390bfc0696493144e1ce2a89f732b096c18a3b5128f3b00f3101e"; shbts="1690387272\05449441374693\0541721923272:01f77659d8bdd8d8ac05ca252ac5923193c334b23c8465afecdbb6df0c6114bdbed05670"; sessionid={self.ses}; rur="CLN\05449441374693\0541721923612:01f7d0f4813ecd0fc24564447584a333e253a1cfec45e5c9f26a020ff7b337193a7c23f2"',
                            'origin': 'https://www.instagram.com',
                            'referer': f'https://www.instagram.com/{self.use}/',
                            'sec-ch-prefers-color-scheme': 'light',
                            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                            'sec-ch-ua-full-version-list': '"Not.A/Brand";v="8.0.0.0", "Chromium";v="114.0.5735.248", "Google Chrome";v="114.0.5735.248"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': '"Windows"',
                            'sec-ch-ua-platform-version': '"10.0.0"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                            'viewport-width': '1040',
                            'x-asbd-id': '129477',
                            'x-csrftoken': 'EPCnYSUmlMlOrarVyv7jY06dpDHJs0Uj',
                            'x-ig-app-id': '936619743392459',
                            'x-ig-www-claim': 'hmac.AR2gTCJERHJMjTV94sTc-eWCNMcG8labBdiZ0T-SETSLu4ux',
                            'x-instagram-ajax': '1007904367',
                            'x-kl-kfa-ajax-request': 'Ajax_Request',
                            'x-requested-with': 'XMLHttpRequest'
            }
            data = f"container_module=profile&nav_chain=PolarisProfileRoot%3AprofilePage%3A1%3Avia_cold_start&user_id={self.follow_id}"
            try:
                r = post(url, data=data,headers=headers).text
                if '"status":"ok"' in r:
                    self.done+=1
                    sleep(0.5)
                else:self.bad+=1
            except IndexError:
                self.bad+=1
                pass
            print(self.purple+f"[ Done ] : {self.done}  | [ bad unfollowing ] : {self.bad}  | [ User ] : {self.use} | [ userid ] : {self.follow_id}", end="\r")

obj = MyClass()
obj.login()
