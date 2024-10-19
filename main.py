import requests
import uuid
from datetime import datetime, timedelta


def send_soap_request():
    url = 'https://int44.zakupki.gov.ru/eis-integration/services/getDocsMis2'

    yesterday = (datetime.now() - timedelta(1)).strftime('%Y-%m-%d')

    xml_request = f'''
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ws="http://zakupki.gov.ru/fz44/get-docs-mis/ws">
    <soapenv:Header/>
    <soapenv:Body>
    <ws:getPublicDocsRequest>
    <index>
    <id>{uuid.uuid4()}</id>
    <createDateTime>{datetime.utcnow().isoformat()}</createDateTime>
    <mode>PROD</mode>
    </index>
    <selectionParams44>
    <subsystemType>PRIZ</subsystemType>
    <periodInfo>
    <exactDate>{yesterday}</exactDate>
    </periodInfo>
    <isAllOrganizations44>true</isAllOrganizations44>
    </selectionParams44>
    </ws:getPublicDocsRequest>
    </soapenv:Body>
    </soapenv:Envelope>
    '''

    headers = {
    'Content-Type': 'text/xml; charset=utf-8',
    }

    response = requests.post(url, data=xml_request, headers=headers)

    if response.status_code == 200:
        print("Response:", response.content)
    else:
        print("Failed to get response. Status code:", response.status_code)
    print("Response:", response.text)


try:
    send_soap_request()
except Exception as e:
    print('Error:', e)
