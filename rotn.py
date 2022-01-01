class rotn:
    
    # international alphabet
    #alphabet = "abcdefghijklmnopqrstuvxyz" 
    
    #using only italian letters.
    alphabet = "abcdefghilmnopqrstuvz" 

    # encrypt a plain text using rotn
    # number define the rot type (numnber=13 => rot13)
    def encrypt(self, plain_text, number):
        plain_text = plain_text.lower()
        final = ""
        finalencrypted = ''
        rotation = self.alphabet[number:] + self.alphabet[:number]

        
        for i in range(len(plain_text)):
            if plain_text[i].isalpha():
                final = rotation[self.alphabet.index(plain_text[i])]
                finalencrypted += final
            else:
                finalencrypted += plain_text[i]
        
        return finalencrypted

    # decrypt a ciphred text using rotn
    # number define the rot type (number=13 => rot13)
    def decrypt(self, encrypted_text, number):
        encrypted_text = encrypted_text.lower()
        final = ""
        finaldecrypted = ''
        rotation = self.alphabet[number:] + self.alphabet[:number]

        for i in range(len(encrypted_text)):
            if encrypted_text[i].isalpha():
                final = self.alphabet[rotation.index(encrypted_text[i])]
                finaldecrypted += final
            else:
                finaldecrypted += encrypted_text[i]
        
        return finaldecrypted