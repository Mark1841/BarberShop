from barberShop import BarberShop
from customer import Customer
from service import Service

if __name__ == '__main__':

    shop = BarberShop('JanoCutz')
    new_customer = Customer(len(shop.customers) + 1, "Mark Janovitz", "9059250766", "mjanovitz@outlook.com")
    shop.add_customer(new_customer)

    new_service = Service(len(shop.services) + 1, "The Beard Trim", "Reduce beard length, outline neck and cheeks", 30, 39.80)
    shop.add_service(new_service)

    print(shop.customers[1])





