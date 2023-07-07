from deep_translator import MyMemoryTranslator
print(MyMemoryTranslator.__doc__)

def english_to_french(english_text):
    '''Takes in a string english_text, returns the french translation of english_text'''
    translator = MyMemoryTranslator(source='en', target='fr')
    french_text = translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    '''Takes in a string french_text, returns the english translation of french_text'''
    translator = MyMemoryTranslator(source='fr', target='en')
    english_text = translator.translate(french_text)
    return english_text
