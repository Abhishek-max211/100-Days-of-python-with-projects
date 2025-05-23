print('''
   ____                                _____  _     _               
  / ___|__ _ _ __ ___   ___  ___ ___  | ____|(_)___| |_ _   _ _ __  
 | |   / _` | '_ ` _ \ / _ \/ __/ __| |  _|  | / __| __| | | | '_ \ 
 | |__| (_| | | | | | |  __/\__ \__ \ | |___ | \__ \ |_| |_| | |_) |
  \____\__,_|_| |_| |_|\___||___/___/ |_____||_|___/\__|\__,_| .__/ 
                                                            
''')
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def caesar(original_text,shift_amount,encoder_or_decoder):
    output_text=""
    if encoder_or_decoder=="decode":
        shift_amount*=-1
    for letters in original_text:
        if letters not in alphabet:
            output_text+=letters
        else:
            shifted_position=alphabet.index(letters)+shift_amount
            shifted_position%=len(alphabet)
            output_text+=alphabet[shifted_position]
    print(f"Here is the {encoder_or_decoder}d result: {output_text}")

shoulld_continue=True
while shoulld_continue:
    direction=input("Type 'encode' to encrypt,type 'decode' to decrypt:\n").lower()
    text=input("Type your message:\n").lower()
    shift=int(input("Type the Shift number:\n"))

    caesar(original_text=text,shift_amount=shift,encoder_or_decoder=direction)

    restart=input("Type 'yes' if you want to go again.Otherwise type 'no'.\n").lower()
    if restart=="no":
        shoulld_continue=False
        print("Good Bye!")