import string
import subprocess
from random import choice

def gerar_senha():
    tamanho1 = 4
    valores1 = string.ascii_lowercase
    senha1 = ''
    for i in range(tamanho1):
        senha1 += choice(valores1)
    
    tamanho2 = 4
    valores2 = string.digits
    senha2 = ''
    for i in range(tamanho2):
        senha2 += choice(valores2)

    senhaF = senha1 + senha2
    return senhaF

def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True)
    return completed


def get_email(username, emailD):
    get_email_cmd = f"Get-ADUser {username} -Properties EmailAddress | Select-Object EmailAddress"

    get_email_info = run(get_email_cmd)

    email = get_email_info.stdout.strip().split('\n')[2].strip()

    if email != emailD:
        return False         
    return True


def get_change_user(username, senhaF):
        change_P = f"Set-ADAccountPassword -Identity {username} -Reset -NewPassword (ConvertTo-SecureString -AsPlainText {senhaF} -Force)"
    
        hello_info = run(change_P)

        if hello_info.returncode != 0:
            print("An error occured: %s", hello_info.stderr)
        else:
            print("Hello command executed successfully!")
        
        print("-------------------------")
        
        bad_syntax_command = "Write-Host 'Incorrect syntax command!'"
        bad_syntax_info = run(bad_syntax_command)
        if bad_syntax_info.returncode != 0:
            print("An error occured: %s", bad_syntax_info.stderr)
        else:
            print("Bad syntax command executed successfully!")
       