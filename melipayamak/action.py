from melipayamak.melipayamak import Api



def sendMaskSMS(phone:int, code:int, data:list[str]):
    api = Api("09212702708", 'Mohamadrezahi72@')
    sms_soap = api.sms('soap')
    res = sms_soap.send_by_base_number(data, f"0{phone}", code)
    print("sms send")