from barberShop import BarberShop
from customer import Customer

if __name__ == '__main__':

    shop = BarberShop('JanoCutz')
    new_customer = Customer(1, "Mark Janovitz", "9059250766", "mjanovitz@outlook.com")
    shop.add_customer(new_customer)

    print(shop.customers[1])




