# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        # sets the attributes into their respective values
        self.message_text=text
        self.valid_words=load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        
        valid_words_copy = self.valid_words.copy()
        return valid_words_copy

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        #checks if our shift is within a reasonable range
        assert (0<=shift) and (shift<=26), "Invalid shift value"
        #initialises upper and lower case letters in a list
        alphabet_lowercase = string.ascii_lowercase
        alphabet_uppercase = string.ascii_uppercase

        map_letter = {}
        #A range for all 26 letters of the alphabet
        for i in range(26):
            #checks if the sum of shift and loop variable is less than 26
            if shift+i<26:
                # build the shift dictionary
                map_letter[alphabet_lowercase[i]] = alphabet_lowercase[shift+i]
                map_letter[alphabet_uppercase[i]] = alphabet_uppercase[shift+i]
            else:
                # build the shift dictionary if the sum of shift and loop variable is greater than 26
                map_letter[alphabet_lowercase[i]] = alphabet_lowercase[shift+i-26]
                map_letter[alphabet_uppercase[i]] = alphabet_uppercase[shift+i-26]
        # returns the dictionary
        return map_letter

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        
        shift_text = ""
        map_letter = self.build_shift_dict(shift)
        #loop over the letters in self.message_text
        for letter in self.message_text:
            # if the letter is in the key of our shift dictionary add it to our holding string
            if letter in map_letter.keys():
                shift_text += map_letter[letter]
            else:
                # all other letters or punctuations are added to the string
                shift_text += letter
        return shift_text

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        # inherit the constructor from Message into our new costructor for PlaintextMessage 
        Message.__init__(self,text)
        self.shif = shift
        self.encrypt_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
                

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
         
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
         
        encryption_copy = self.encrypt_dict.copy()
        return  encryption_copy

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        
        return self.message_text_encrypted
    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        
        self.shift = shift
        self.encrypt_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
        return


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
    
        Message.__init__(self, text)
    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        # keeps track of the maximum shift number and maximum real words number
        max_shift_num = 0
        max_real_word_num = 0
        # A for loop for all letters of the alphabet and to build our shift dictionary for all possible combinations
        for shift in range(26):
            real_word_num = 0
            # applies a shift to our word
            temp_text = self.apply_shift(shift)
            # creates a list of alll shifted words
            temp_text_list = temp_text.split()
            # loop over our word list 
            for word in temp_text_list:
                # checks if the word in the list is valid
                if is_word(self.get_valid_words(),word):
                    # adds 1 to our real word count
                    real_word_num += 1
                # checks if our real word count is greater than maximum shift number
                if real_word_num > max_real_word_num:
                    # assigns our loop varibale/shift to our maximum shift number variable
                    max_shift_num = shift
                    max_real_word_num = real_word_num
        # returns a tuple of the maximum shift number and the shift applied to the encrypted word
        return (max_shift_num, self.apply_shift(max_shift_num))

if __name__ == '__main__':

    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())

    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE
    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())


    plaintext = PlaintextMessage('happy', 2)
    print('Expected Output: jcrra')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    ciphertext = CiphertextMessage('jcrra')
    print('Expected Output:', (24, 'happy'))
    print('Actual Output:', ciphertext.decrypt_message())

    plaintext = PlaintextMessage('jazz', 24)
    print('Expected Output: hyxx')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    ciphertext = CiphertextMessage('hyxx')
    print('Expected Output:', (2, 'jazz'))
    print('Actual Output:', ciphertext.decrypt_message())
    #TODO: best shift value and unencrypted story 
    ciphertext = CiphertextMessage(get_story_string())
    print("unencrypted story: ", ciphertext.decrypt_message())
