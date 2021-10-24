
from logging import error
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
from azure.keyvault.secrets import SecretClient
from azure.identity import ClientSecretCredential
from dotenv import load_dotenv


# chargement des variables d'environnment
load_dotenv()

def get_authentication(tenant_id, client_id, client_secret, endpoint_kv, secret_name_cg):
    try:

        credential = ClientSecretCredential(
            tenant_id=tenant_id,
            client_id=client_id,
            client_secret=client_secret
        )

        # authentication to keyvault
        secret_client = SecretClient(vault_url=endpoint_kv, credential=credential)
        # retrieve secret in keyvault
        secret = secret_client.get_secret(secret_name_cg)

        # connect to service text analyze
        key_credential = AzureKeyCredential(secret.value)
        return key_credential
    except TypeError as e:
        print("error authentication ",e)

def get_detection_language(key_credential, endpoint_cg, choice, entry_user):
    """
    [summary]
    request to service cognitive azure (analysis text) in order to analyze text sent and to get language, code iso and score
    
    Args:
        tenant_id ([type]): information in app registration in Azure
        client_id ([type]): information in app registration in Azure
        client_secret ([type]): information in app registration in Azure
        secret_name_cg ([type]): information in key vault is the name of secret in Azure
        endpoint_kv ([type]): endpoint of keyvault in azure
        endpoint_cg ([type]): endpoint of service cognitive in azure
        entry_user ([type]): text entry by user
    
    
    Returns:
        [type]: documents 
        Example :
        "documents": [
        {
            "id": "1",
            "detectedLanguage": {
                "name": "English",
                "iso6391Name": "en",
                "confidenceScore": 0.99
            },
            "warnings": []
        },
        ...
        ]
    """
    # If use managed identity, with script in azure function. Authentication  > credential = DefaultAzureCredential()
    # here we use appregistration to authenticate keyvault
    text_analytics_client = TextAnalyticsClient(endpoint_cg, key_credential)
    documents = []

    if choice=="2":
        documents.append(entry_user)

    if choice=="1":
        documents = entry_user

    try:
    # request to pass user's entry t
        response = text_analytics_client.detect_language(documents)
        result = [doc for doc in response if not doc.is_error]
        return result
    except TypeError as e:
        return print("error cognitif ",e)
        
    

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    help(get_detection_language)