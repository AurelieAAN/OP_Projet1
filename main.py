
import os
from Request_Language import get_detection_language, get_authentication
from dotenv import load_dotenv
import sys



# chargement des variables d'environnment
load_dotenv() 
#############################################################################
def version():
    print("version of software 1.0.0")

def choice():
    print("choice=1 : send array of texts / choice=2 : send text -- (limit 1000 characters by text)")

def entry():
    print("Text/Array of texts to detect - limit by text is 1000 characters")
 
#############################################################################
def main( choice, entry_user):
    SECRET_NAME_CG = os.getenv('SECRET_NAME_CG')
    ENDPOINT_KV = os.environ.get('ENDPOINT_KV')
    ENDPOINT_CG = os.getenv('ENDPOINT_CG')

    TENANT_ID = os.getenv('TENANT_ID')
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')

    # on demande au user de rentrer du texte > limite 1 000
    #entry_user = input("Entrez un texte pour connaitre la langue : ")

    cred = get_authentication(TENANT_ID, CLIENT_ID, CLIENT_SECRET, ENDPOINT_KV, SECRET_NAME_CG)
    # on fait la requête grâce à la fonction "get_detection_language"
    result = get_detection_language(cred, ENDPOINT_CG, choice, entry_user)

    for doc in result:
        print("Language detected: {}".format(doc.primary_language.name))
        print("ISO6391 name: {}".format(doc.primary_language.iso6391_name))
        print("Confidence score: {}\n".format(doc.primary_language.confidence_score))
 
#############################################################################
if __name__ == "__main__":

    import argparse
    
    # création du parse des arguments
    parser = argparse.ArgumentParser(description="To get language Text sent. This programm use function get_detection_language in file Request_language.py")
 
    # déclaration et configuration des arguments
    parser.add_argument('-v', '--version', action='store_true', default=False, help="Version of software")
    parser.add_argument('-c', '--choice', required=True, help="choice=1 : send array of texts / choice=2 : send text -- (limit 1000 characters by text)")
    parser.add_argument('-e','--entry', required=True, help="Text/Array of texts to detect - limit by text is 1000 characters")

    # dictionnaire des arguments
    dargs = vars(parser.parse_args())
 
    # print(dargs) # affichage du dictionnaire pour mise au point
    if dargs['version']:
        version()
        sys.exit()
    args = parser.parse_args()
    main(args.choice, args.entry)
