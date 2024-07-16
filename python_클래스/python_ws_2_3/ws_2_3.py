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

class VIPMovieTheater(MovieTheater) :

    def __init__(self, name, total_seats, rev_seat, vip_seats):
        super().__init__(name, total_seats, rev_seat)
        self.vip_seats = vip_seats

    def reserve_vip_seat(self) :
        
        for i in range(self.rev_seat) :
            if self.vip_seats - MovieTheater.reserved_seats > 0 :
                MovieTheater.reserved_seats +=1
                print("VIP 좌석 예약이 완료되었습니다.")
            else : 
                self.rev_seat = self.rev_seat-MovieTheater.reserved_seats
                super().reserve_seat()
                print("예약 가능한 VIP 좌석이 없습니다.")


    
theater1=VIPMovieTheater("메가박스", 100 ,4, 3)
theater1.reserve_vip_seat()