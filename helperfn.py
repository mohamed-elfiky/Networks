def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)


def longdiv(divident, divisor):
    pick = len(divisor)
    tmp = divident[0: pick]

    while pick < len(divident):

        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + divident[pick]

        else:
            tmp = xor('0' * pick, tmp) + divident[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    checkword = tmp
    return checkword


def decode(data, key):
    l_key = len(key)

    # Appends n-1 zeroes at end of data
    appended_data = data + '0' * (l_key - 1)
    remainder = longdiv(appended_data, key)

    return remainder


def encode(data, key):

    l_key = len(key)

    # Appends n-1 zeroes at end of data
    appended_data = data + '0' * (l_key - 1)
    remainder = longdiv(appended_data, key)

    encoded_date = data + remainder
    return encoded_date


def verify(data, key, a=int(0)):
    ans = decode(data, key)
    temp = "0" * (len(key) - 1)

    if ans == temp and a == 0:
        print('Message -> Message is correct')
    else:
        print('Message -> Message is not correct')


def alter(str_, argu_):
    operand2 = []
    for i in range(len(str_)):
        if(i == argu_ - 1):
            operand2.append("1")
        else:
            operand2.append("0")
    str2_ = "".join(operand2)
    return xor(str_, str2_)
