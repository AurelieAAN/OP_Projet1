# Openclassroom : Projet 1

Install environment : pip install -r requirements.txt

Modify variables in .env to connect Azure :
	- create appregistration to authenticate keyvault
	- create secret in key vault with secret service cognitive azure
(best practice is to use manage identities but your application needs to host in azure, by example you can use azure function)


Then, 

1) launch git bash and activate environment : source activate
2) launch P1_01_script.py : python P1_01_script.py --help (function is DETECT_LANG)

or 

1) launch Script.bat
2) launch P1_01_script.py : python P1_01_script.py --help  (function is DETECT_LANG)

- Help : 

python P1_01_script.py --help

python request_language.py --help
