def get_alphabet():
    """
    This function returns the alphabet in a list
    :return: list
    """

    alphabet = list()
    for a in range(26):
        alphabet.append(chr(97+a))

    return alphabet
def cipher_alphabet(key='meowc'):
    """
    Creates the cipher alphabet with the key provided
    :param key: string
    :return cipher: list
    """
    #Convert the key to list, add it to cipher
    #cipher = list(key)

    alphabet = get_alphabet()
    '''
    for a in alphabet:
        if a not in key:
            cipher.append(a)
    '''
    cipher = list(key) + [a for a in alphabet if a not in key]

    '''
    cipher_d = dict()
    for a, c in zip(alphabet, cipher):
        cipher_d[a] = c
    '''
    cipher_d = {a:c for a, c in zip(alphabet, cipher)}

    return cipher_d

def encrypt(msg, key='meowc'):
    """
    Encrypts the msg using the key provided
    :param msg: string
    :param key: string
    :return encrypted_msg: string
    """

    #cipher alphabet
    cipher = cipher_alphabet(key)
    encrypted_msg = ''
    for s in msg.lower():
        encrypted_msg += cipher.get(s, s)

    return encrypted_msg

def decrypt(encrypted_msg, key='meowc'):
    cipher = cipher_alphabet(key)
    reversed_cipher = {v:k for k, v in cipher.items()}
    msg = ''
    for s in encrypted_msg:
        msg += reversed_cipher.get(s,s)

    return msg

i = cipher_alphabet()
print(i)
print(decrypt('''ifz cda qmvmpdi ecdpdetmpfqtfeq tcdt jdam cmp queemqqsui fk ifsm.
tcmqm ecdpdetmpfqtfeq nplnmiima cmp tcplubc tmppfrim elkaftflkq fk cmp ecfiaclla,
ifvfkb fk ecdlq, smdp, dka mvmk qussmpfkb splj bpmdt ilqqmq.
tcm ecdpdetmpfqtfeq qcm nlqqmqqmq dpm slpbfvmkmqq dka rpdvmkmqq.
tcmqm ecdpdetmpfqtfeq ecdkbma fk afssmpmkt jdbkftuamq dq ifz bpmw liamp;
kmvmptcmimqq, tcmqm nplbpmqqflk fk ifzq ecdpdetmp diilwma cmp tl amdi wftc
qftudtflkq eimvmpiy, rut fq diql drim tl jlvm lk fk cmp lwk ifsm wcmk sdefkb
tcm dryqq ls ifsm, fk alfkb cmp vmpy rmqt fk decfmvfkb bpmdt bldiq dka rmttmp tcfkbq,
pmbdpaimqq ls ltcmpq kmbdtfvm fksiumkemq.'''))
print()
print(encrypt('''I have a dog, two cats, two tortoises, and a tank of fish. Once I had a mouse but it
                        ran away long time six years ago. Tomorrow is my dog's eighth year-old birthday. Although
                        she is getting old, but she still act like kid running around all the time with the cats.
                        And most of the time she run just to catch the cats. Mentioned about cats, I had the first
                        cat last year March. He was two weeks old then, and was weighted less than one kilogram.
                        Now he is about one and a half year-old but he is now six and a half kilograms!!! I am afraid
                        that he will get too fat in the future T^T'''))

def cici(c):
    c = list()
    for i in range(7893600):
        print(c)


cici('''ifz cda qmvmpdi ecdpdetmpfqtfeq tcdt jdam cmp queemqqsui fk ifsm.
tcmqm ecdpdetmpfqtfeq nplnmiima cmp tcplubc tmppfrim elkaftflkq fk cmp ecfiaclla,
ifvfkb fk ecdlq, smdp, dka mvmk qussmpfkb splj bpmdt ilqqmq.
tcm ecdpdetmpfqtfeq qcm nlqqmqqmq dpm slpbfvmkmqq dka rpdvmkmqq.
tcmqm ecdpdetmpfqtfeq ecdkbma fk afssmpmkt jdbkftuamq dq ifz bpmw liamp;
kmvmptcmimqq, tcmqm nplbpmqqflk fk ifzq ecdpdetmp diilwma cmp tl amdi wftc
qftudtflkq eimvmpiy, rut fq diql drim tl jlvm lk fk cmp lwk ifsm wcmk sdefkb
tcm dryqq ls ifsm, fk alfkb cmp vmpy rmqt fk decfmvfkb bpmdt bldiq dka rmttmp tcfkbq,
pmbdpaimqq ls ltcmpq kmbdtfvm fksiumkemq.''')

