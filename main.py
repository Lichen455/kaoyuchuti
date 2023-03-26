import Selector_document
import variable
import chatgpt_api
variable.Subject="English"
variable.type=4
variable.content="过去进行时"
def main():
    with open('data/apikey.tls', encoding='utf-8') as file_obj:
        variable.api_Key = file_obj.read()
    if variable.Subject == "History":
        Selector_document.select_History()
    if variable.Subject == "English":
        Selector_document.select_English()
    chatgpt_api.chatgpt()
    #print(variable.answer)
    #print(variable.cache)