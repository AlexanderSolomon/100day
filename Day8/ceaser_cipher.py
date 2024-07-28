import art

#TODO-1: Import and print the logo from art.py when the program starts.
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

password = []
not_encripted_letter_number = []
not_encrpted_text = []
cipher_text_posistion = []




#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):    
    #appending letters from the word
    for letter in text:
        #print(alphabet.index(letter))
        number = alphabet.index(letter)
        # print(number)
        not_encripted_letter_number.append(number)
        # print(not_encripted_letter_number)
        not_encrpted_text.append(letter)

    # adding the new position of the encripted  chipher text
    for x in not_encripted_letter_number:
        new_text = (x + shift)
        if new_text > 26:
            new_text = new_text % 26
        cipher_text_posistion.append(new_text)
        # print(cipher_text_posistion)        
        
    for index in cipher_text_posistion:
        password.append(alphabet[index])


    # Joining the list into a string
    result_encription = ''.join(password)

    print(f"you encripted msg is: {result_encription}" )
    print(cipher_text_posistion)
    print(not_encrpted_text)
    play_again = input("type yes or no to play or not to play... \n")
    if play_again == "no":
        keep_going = False
    
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    #🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

def decode(text, shift):    
    #appending letters from the word
    for letter in text:
        #print(alphabet.index(letter))
        number = alphabet.index(letter)
        # print(number)
        not_encripted_letter_number.append(number)
        # print(not_encripted_letter_number)
        not_encrpted_text.append(letter)

    # adding the new position of the encripted  chipher text
    for x in not_encripted_letter_number:
        new_text = (x - shift)
        if new_text > 26:
            new_text = new_text % 26
        cipher_text_posistion.append(new_text)
        # print(cipher_text_posistion)        
        
    for index in cipher_text_posistion:
        password.append(alphabet[index])


    # Joining the list into a string
    result_encription = ''.join(password)

    print(f"your none encripted msg is: {result_encription}" )
    print(cipher_text_posistion)
    print(not_encrpted_text)
    play_again = input("type yes or no to play or not to play... \n")
    if play_again == "no":
        keep_going = False








# create as one function

def cesearcipher():
    if direction == "encode" :
        encrypt(text, shift)
    else:
        decode(text,shift)



cesearcipher()


###### the super simple solution... so annoying :) lol
    
    
# def encrypt1(text_write, shift_amount):
#     cipher_text =""
#     for letter in text_write:
#         posistion = alphabet.index(letter)
#         new_position = posistion + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text +=new_letter
#     print(f"the encoded text is {cipher_text}")
    

# encrypt1(text_write= text, shift_amount=shift)


#   #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
# def decrypt(cipher_text, shift_amount):
#   plain_text = ""
#   for letter in cipher_text:
#     position = alphabet.index(letter)
#     new_position = position - shift_amount
#     plain_text += alphabet[new_position]
#   print(f"The decoded text is {plain_text}")


# #TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
# if direction == "encode":
#   encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#   decrypt(cipher_text=text, shift_amount=shift)