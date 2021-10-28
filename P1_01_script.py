
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
def main( entry_user):
    SECRET_NAME_CG = os.getenv('SECRET_NAME_CG')
    ENDPOINT_KV = os.environ.get('ENDPOINT_KV')
    ENDPOINT_CG = os.getenv('ENDPOINT_CG')

    TENANT_ID = os.getenv('TENANT_ID')
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')

    # authentication to get secret to connect to service cognitive azure
    cred = get_authentication(TENANT_ID, CLIENT_ID, CLIENT_SECRET, ENDPOINT_KV, SECRET_NAME_CG)

    # on fait la requête grâce à la fonction "get_detection_language"
    #toujours choix 1
    result = get_detection_language(cred, ENDPOINT_CG, 1, entry_user)

    # print informations about result
    for doc in result:
        print("Language detected: {}".format(doc.primary_language.name))
        print("ISO6391 name: {}".format(doc.primary_language.iso6391_name))
        print("Confidence score: {}\n".format(doc.primary_language.confidence_score))
 
#############################################################################
if __name__ == "__main__":
    
    # create args
    parser = argparse.ArgumentParser(prog="DETECT_LANG",description="To get language Text/Array sent")
 
    # declare and config argument
    parser.add_argument('-e','--entry', nargs='+', required=True, help="Text/List of texts to detect - limit by text is 1000 characters")

    args = parser.parse_args()

    #launch function with args
    main(args.entry)
