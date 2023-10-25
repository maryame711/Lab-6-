github = ''

def encode(password):
    encode_list = []
    for digit in password:
        encode_list.append(int(digit))

    for i in range(0,len(encode_list)):
        encode_list[i] = encode_list[i] + 3

    for j in range(0, len(encode_list)):
        encode_list[i] = str(encode_list[i])
    enc = "".join(encode_list)
    global github
    github = enc
    print("Your password has been encoded and stored!")

def menu():
    print("Menu", "\n------------- \n1. Encode \n2. Decode"
        "\n3. Quit")



def decode(password):
    decode_list =[]
    for digit in password:
        decode_list.append(int(digit))

    ranng = len(decode_list)

    for i in range(0,ranng):
        decode_list[i] = decode_list[i] - 3

    for i in range(0,ranng):
        decode_list[i] = str(decode_list[i])

    decoded_pass = "".join(decode_list)
    print(decoded_pass)



menu()
#option = int(input("Please enter an option")
passwrd = input("Please enter your password to encode:")

decode(passwrd)





