
import os
from request_language.request_language import get_detection_language, get_authentication
from dotenv import load_dotenv
import sys
import argparse
import warnings
warnings.filterwarnings("ignore")

# chargement des variables d'environnment
load_dotenv() 


#############################################################################

##function principal to get language of text/ list of texts
def main( choice, entry_user):
    
    SECRET_NAME_CG = os.getenv('SECRET_NAME_CG')
    ENDPOINT_KV = os.environ.get('ENDPOINT_KV')
    ENDPOINT_CG = os.getenv('ENDPOINT_CG')

    TENANT_ID = os.getenv('TENANT_ID')
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')

    # authentication to get secret to connect to service cognitive azure
    cred = get_authentication(TENANT_ID, CLIENT_ID, CLIENT_SECRET, ENDPOINT_KV, SECRET_NAME_CG)

    # on fait la requête grâce à la fonction "get_detection_language"
    result = get_detection_language(cred, ENDPOINT_CG, choice, entry_user)

    # print informations about result
    for doc in result:
        print("Language detected: {}".format(doc.primary_language.name))
        print("ISO6391 name: {}".format(doc.primary_language.iso6391_name))
        print("Confidence score: {}\n".format(doc.primary_language.confidence_score))

def main_send_text(entry):
    main(2,entry)

def main_send_list(entry):
    main(1,entry)
 
#############################################################################
if __name__ == "__main__":
    
    # create args
    parser = argparse.ArgumentParser(prog="DETECT_LANG",description="To get language Text/Array sent")

    subparsers = parser.add_subparsers(dest='command', help='sub-command help')
    
    # Create a send_text subcommand    
    parser_send_text = subparsers.add_parser('send_text', help='send text (limit 1000 characters by text)')
    parser_send_text.add_argument('-t','--entry_text',  required=True, help="send text to detect language - limit by text is 1000 characters")

    # Create a send_list subcommand       
    parser_list_text = subparsers.add_parser('send_list', help='send list of text (limit 1 000 characters by text)')
    parser_list_text.add_argument('-l','--entry_list', nargs='+', required=True, help="send list of texts to detect language - limit by text is 1000 characters")

    args = parser.parse_args()
    if args.debug:
        print("debug: " + str(args))
    if args.command == 'send_text':
        if args.entry_text:
            main_send_text( args.entry_text)
    elif args.command == 'send_list':
        if args.entry_list:
            main_send_list( args.entry_list)