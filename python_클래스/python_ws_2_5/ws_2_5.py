# 아래에 코드를 작성하시오.

class Theater :
    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
        self.reserved_seats = 0
    def reserve_seat(self) :
        if self.total_seats > self.reserved_seats :
            self.reserved_seats+=1
            print("좌석 예약이 완료되었습니다.")
        else :
            print("좌석 예약에 실패하였습니다.")


class MovieTheater(Theater) :
    total_movies = 0
    
    @classmethod
    def add_movie(cls) :
        cls.total_movies+=1
        return "영화추가성공"

    @staticmethod  #정적메소드, 남의 메소드도 쓸 수 있음.. 왜냐면 무조건 밖에서 가져올거니까.
    def description(mt) :
        print(f"영화관의 이름: {mt.name}\n총 좌석 수: {mt.total_seats}\n예약된 좌석 수: {mt.reserved_seats}\n총 영화 수: {MovieTheater.total_movies}")

hel = MovieTheater("메가박스", 100)
hel.reserve_seat()
hel.add_movie()
MovieTheater.description(hel)