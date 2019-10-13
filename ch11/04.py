import win32com.client
import pythoncom

class XASessionEventHandler:
    login_state = 0

    def OnLogin(self, code, msg):
        if code == "0000":
            print("로그인 성공")
            XASessionEventHandler.login_state = 1
        else:
            print("로그인 실패")

instXASession = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionEventHandler)

id = "아이디"
passwd = "비밀번호"
cert_passwd = "공인인증서"

instXASession.ConnectServer("hts.ebestsec.co.kr", 20001)
instXASession.Login(id, passwd, cert_passwd, 0, 0)

while XASessionEventHandler.login_state == 0:
    pythoncom.PumpWaitingMessages()

num_account = instXASession.GetAccountListCount()
for i in range(num_account):
    account = instXASession.GetAccountList(i)
    print(account)
