class Address:
    def __init__(self, street, city, province, zipcode):
        self.street = street
        self.city = city
        self.province = province
        self.zipcode = zipcode

    def __str__(self):
        return f"{self.street}, {self.city}, {self.province} {self.zipcode}"