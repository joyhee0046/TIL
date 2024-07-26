# 아래에 코드를 작성하시오.
class MovieTheater:
    reserved_seats  = 0                                
    def __init__(self, name, total_seats, rev_seat):
        self.name=name
        self.total_seats=total_seats
        self.rev_seat = rev_seat
    def TheaterInfo(self) :
        return f'{self.name}'
    def reserve_seat(self) :
        for i in range(self.rev_seat) :
            if self.total_seats - MovieTheater.reserved_seats > 0 :
                MovieTheater.reserved_seats +=1
                print("좌석 예약이 완료되었습니다.")
            else : 
                print("좌석 예약에 실패하였습니다.")
    def current_status(self) :
        return f'총 좌석 수: {self.total_seats}\n예약된 좌석 수: {self.rev_seat}'
    
theater1=MovieTheater("메가박스",100 ,3)
theater1.reserve_seat()
print(theater1.current_status())

# class MovieTheater:
#     def __init__(self, name, total_seats):
#         self.name = name
#         self.total_seats = total_seats
#         self.reserved_seats = 0

#     def reserve_seat(self):
#         if self.reserved_seats < self.total_seats:
#             self.reserved_seats += 1
#             return "좌석 예약이 완료되었습니다."
#         else:
#             return "더 이상 예약 가능한 좌석이 없습니다."

#     def current_status(self):
#         print(f"총 좌석 수: {self.total_seats}")
#         print(f"예약된 좌석 수: {self.reserved_seats}")

# # 인스턴스 생성
# theater1 = MovieTheater("메가박스", 100)
# theater2 = MovieTheater("CGV", 80)

# # 좌석 예약
# print(theater1.reserve_seat())
# print(theater1.reserve_seat())
# print(theater1.reserve_seat())

# # 현재 예약 상태 출력
# theater1.current_status()
