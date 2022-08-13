def enterProducts():
    buyingData = {}
    enterDetails = True
    while enterDetails:
        details = input('Press A to enter itema nd Q to Quit')
        if details == 'A':
            product = input('Enter product name:')
            quantity=int(input('Enter quantity:'))
            buyingData.update({product: quantity})
        elif details == 'Q':
            enterDetails = False
        else:
            print('Please enter correct option')
    return buyingData
