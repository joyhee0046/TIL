# 아래에 코드를 작성하시오.
class MovieTheater:
    reserved_seats  = 0
    def __init__(self, name, total_seats):
        self.name=name
        self.total_seats=total_seats
    def TheaterInfo(self) :
        return f'{self.name}'
     
# class MovieTheater:
#     def __init__(self, name, total_seats):
#         self.name = name
#         self.total_seats = total_seats
#         self.reserved_seats = 0

#     def __str__(self) -> str:
#         return self.name

    
theater1=MovieTheater("메가박스", 5)
theater2=MovieTheater("CGV", 7)
print(theater1.TheaterInfo())
print(theater2.TheaterInfo())