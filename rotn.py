class rotn:
    
    # encrypt a plain text using rotn
    # number define the rot type (numnber=13 => rot13)
    def encrypt(self, plain_text, number):
        plain_text = plain_text.lower()
        text = "abcdefghilmnopqrstuvz"
        final = ""
        finalencrypted = ''
        rotation = text[number:] + text[:number]

        
        for i in range(len(plain_text)):
            if plain_text[i].isalpha():
                final = rotation[text.index(plain_text[i])]
                finalencrypted += final
            else:
                finalencrypted += plain_text[i]
        
        return finalencrypted

    # decrypt a ciphred text using rotn
    # number define the rot type (number=13 => rot13)
    def decrypt(self, encrypted_text, number):
        encrypted_text = encrypted_text.lower()
        #number = int(input('input rot: '))
        #text = "abcdefghijklmnopqrstuvwxyz"
        text = "abcdefghilmnopqrstuvz"
        final = ""
        finaldecrypted = ''
        rotation = text[number:] + text[:number]

        for i in range(len(encrypted_text)):
            if encrypted_text[i].isalpha():
                final = text[rotation.index(encrypted_text[i])]
                finaldecrypted += final
            else:
                finaldecrypted += encrypted_text[i]
        
        return finaldecrypted