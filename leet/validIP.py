def validIPv4(IP):
    # print(IP)
    ip4 = IP.split('.')
    if len(ip4) != 4:
        return False
    for i in range(4):
        s = ip4[i]
        # print(s)
        if not s or not s.isdigit() or s[0] == '0' or int(s) > 255:
            return False
    return True


def validIPv6(IP):
    ip6 = IP.split(':')
    if len(ip6) != 8:
        return False
    for i in range(8):
        s = ip6[i]
        if not s or not s.isalnum() or len(s) > 4:
            print(s)
            return False
        try:
            int(s, 16)
        except ValueError:
            return False
    return True


def validIPAddress(IP):
    """
    :type IP: str
    :rtype: str
    """

    if ':' in IP and validIPv6(IP):
        return "IPv6"
    elif '.' in IP and validIPv4(IP):
        return "IPv4"
    else:
        return "Neither"


def main():
    # print(validIPAddress("172.16.254.1"))
    print(validIPAddress("20EE:FGb8:85a3:0:0:8A2E:0370:7334"))


main()
