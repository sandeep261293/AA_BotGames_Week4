import datetime
import json
from azure.ai.formrecognizer import FormRecognizerClient
from azure.core.credentials import AzureKeyCredential

def readInvoiceData(docPath):
    endpoint = "https://invoice-fr.cognitiveservices.azure.com/"
    credentials = AzureKeyCredential("1376324571884622bc2b73ddbca91706")

    form_recognizer_client = FormRecognizerClient(endpoint,credentials)


    with open(docPath,"rb") as bf:
        invoice = bf.read()

    poller = form_recognizer_client.begin_recognize_invoices(invoice)
    invoiceData = poller.result()

    invoiceData_json = json.dumps(invoiceData, default=json_default)

    return str(invoiceData_json)


def json_default(value):
    if isinstance(value, datetime.date):
        return dict(year=value.year, month=value.month, day=value.day)
    else:
        return value.__dict__




    






