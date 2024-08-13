from amocrm.v2 import tokens, Lead as _Lead, custom_field, Event, Contact, Company

class Lead(_Lead):
    new_field = custom_field.UrlCustomField("")

if __name__ == '__main__':

    tokens.default_token_manager(
        client_id="",
        client_secret="",
        subdomain="",
        redirect_url="",
        storage=tokens.FileTokensStorage(),  # by default FileTokensStorage
    )
    #tokens.default_token_manager.init(code="", skip_error=False)

    contacts = Contact.objects.all()

    for contact in contacts:
        print(contact.id)

    #lead = Lead.objects.get(query='Python script')
    #print(lead)
    #lead.new_field = "9/10"
    #lead.save()

    events = Event.objects.all()
    print(events)
    i = 0
    for eventus in events:
        if eventus.entity_type == 'lead':
            print(eventus)
            i = i + 1
    print(i)        
