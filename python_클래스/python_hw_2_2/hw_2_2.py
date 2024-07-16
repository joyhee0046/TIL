# 아래에 코드를 작성하시오.
class Product :
    product_count = 0

    def __init__(self, name, price) :
        self.name = name
        self.price = price
        Product.product_count +=1

    def display_info(self) :
        print(f"상품명: {self.name}, 가격: {self.price}원")
    

pro1 = Product("사과", 1000)
pro2 = Product("바나나", 1500)

pro1.display_info()
pro2.display_info()
print(f"총 상품 수: {Product.product_count}")