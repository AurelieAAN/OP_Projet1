import os
from Request_Language import get_detection_language
from dotenv import load_dotenv
import sys



# chargement des variables d'environnment
load_dotenv() 
#############################################################################
def version():
    print("version of software 1.0.0")
 
#############################################################################
def main():
    SECRET_NAME_CG = os.getenv('SECRET_NAME_CG')
    ENDPOINT_KV = os.environ.get('ENDPOINT_KV')
    ENDPOINT_CG = os.getenv('ENDPOINT_CG')

    TENANT_ID = os.getenv('TENANT_ID')
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')

    # on demande au user de rentrer du texte > limite 1 000
    entry_user = input("Entrez un texte pour connaitre la langue : ")

    # on fait la requête grâce à la fonction "get_detection_language"
    result = get_detection_language(TENANT_ID, CLIENT_ID, CLIENT_SECRET, SECRET_NAME_CG, ENDPOINT_KV, ENDPOINT_CG, entry_user)

    for doc in result:
        print("Language detected: {}".format(doc.primary_language.name))
        print("ISO6391 name: {}".format(doc.primary_language.iso6391_name))
        print("Confidence score: {}\n".format(doc.primary_language.confidence_score))
 
#############################################################################
if __name__ == "__main__":

    import argparse
 
    # création du parse des arguments
    parser = argparse.ArgumentParser(description="To get language Text sent. Use function get_detection_language in file Request_language.py")
 
    # déclaration et configuration des arguments
    parser.add_argument('-v', '--version', action='store_true', default=False, help="Version of software")
 
    # dictionnaire des arguments
    dargs = vars(parser.parse_args())
 
    # print(dargs) # affichage du dictionnaire pour mise au point
    if dargs['version']:
        version()
        sys.exit()
 
    main()
    