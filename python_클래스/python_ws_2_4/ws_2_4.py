# 아래에 코드를 작성하시오.

class MovieTheater:
    reserved_seats  = 0
    total_movies = 0

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
                print("좌석 예약이 성공적으로 완료되었습니다.")
            else : 
                print("좌석 예약에 실패하였습니다.")

    def current_status(self) :
        return f'{self.name} 영화관의 총 좌석 수: {self.total_seats}\n{self.name} 영화관의 예약된 좌석 수: {self.rev_seat}'
    
    def add_movie(self) : 
        for i in range(self.rev_seat) : 
            MovieTheater.total_movies+=1
            print("영화가 성공적으로 추가되었습니다.")
        
    @staticmethod  #정적메소드
    def description() :
        print("이 클래스는 영화관의 정보를 관리하고 좌석 예약 및 영화 추가 기능을 제공합니다.")
        print("영화관의 이름, 총 좌석 수, 예약된 좌석 수, 총 영화 수를 관리합니다.")

theater1=MovieTheater("메가박스", 100 ,2)
theater2=MovieTheater("CGV", 150 ,1)

theater1.reserve_seat()
theater2.reserve_seat()
theater1.add_movie()
print(theater1.current_status())
print(theater2.current_status())
print(f"총 영화 수: {theater2.total_movies}")
theater2.description()
