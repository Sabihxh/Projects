
from aolpy.api.aol_fields_api.contacts.fields import fields
import vobject

vcard = open('vcard_reader.txt')
vcard_text = vcard.read()


def get_field_names():
    """not used"""
    all_fields = []
    for field in fields:
        all_fields.append(field['fieldname'])
    return all_fields



def vcard_to_dict(vcard_text):

    vcard_objects = set()
    vcards = ['%sEND:VCARD' % item for item in vcard_text.split('END:VCARD') if item.strip()]

    for item in vcards:
        vcard = vobject.readOne(item)
        print get_address(vcard)


def get_address(vcard):
    """Return dicitonary with vcard"""
    addr_dict = {}
    addr_dict['address'] = vcard.adr.value.street
    addr_dict['postcode'] = vcard.adr.value.code
    addr_dict['town'] = vcard.adr.value.city
    addr_dict['state'] = vcard.adr.value.region
    addr_dict['country'] = vcard.adr.value.country
    addr_dict['main_address_label'] = vcard.adr.params.get('TYPE')[0]

    return addr_dict    
    
    


vcard_to_dict(vcard_text)























