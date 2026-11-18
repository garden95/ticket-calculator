

def calculate_ticket(age, morning, movie_3d):
    a = 0

    if morning == True:
        a = 8000
    elif age >= 19:
        a = 15000
    elif age < 19:
        a = 12000

    if movie_3d == True:
        return a + 5000
    else :
        return a


def vip_discount(price, is_vip):

    if is_vip == True :
        final_price = price - price // 10
        return final_price
    else :
        return price