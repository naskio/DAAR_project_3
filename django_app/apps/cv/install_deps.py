# import nltk
# import ssl
# import spacy
#
# # fix for ssl error (https://stackoverflow.com/questions/38916452/nltk-download-ssl-certificate-verify-failed)
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
#
# # to install all nltk projects (if there is some missing packages use this instead)
# # nltk.download('all')
# # alternatively
# # nltk.download('popular')
# # only used packages
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('universal_tagset')
# nltk.download('wordnet')
# nltk.download('brown')
# nltk.download('maxent_ne_chunker')
# # pip3 install spacy
# # validation: python -m spacy validate
# # not required already requirements (it can be used to force update of the model)
# # force update model: python3 -m spacy download en_core_web_sm
# # nlp = None
# nlp = spacy.load('en_core_web_sm')
