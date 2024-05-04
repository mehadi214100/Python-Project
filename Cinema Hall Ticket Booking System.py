class Star_Cinema:
    hall_list = []  # class attribute 

    def entry_hall(self,hall_object):   # entry hall method that insert an object of class hall
        self.hall_list.append(hall_object)  

class Hall:
    def __init__(self,rows,cols,hall_no) -> None:
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        Star_Cinema().entry_hall(self) # insert the object to the star cinema  class attribute hall list

    def entry_show(self,id,movie_name,time):  # entry show for add a new show
        t = (id,movie_name,time)
        self._show_list.append(t)
        seat = []
        for i in range(1,self._rows+1):  # make 2d matrix for seat
            col = []
            for j in range(1,self._cols+1):
                col.append('✅')
            seat.append(col)
        self._seats[id] = seat # seat add to the given cinema id
    
    def book_seats(self,id,seatlist):  # for book a seat
        if id not in self._seats: # error handle if given id is invalid
            print("Invalid show id ")
            return

        for row,col in seatlist:
            if(row<1 or row>self._cols and col<1 or col>self._cols):  # check given row and column is valid or not
                print("Invalid seat")
                return 
        if(self._seats[id][row-1][col-1]=='❌'):  # check seat is booked or free
            print("Seat already booked")
            return

        self._seats[id][row-1][col-1] = '❌'   # if all condition satisfy then successfully booked a seat
        print('\n----------------------------')
        print("|  Seat booking successful  |")
        print('----------------------------')
    
    def view_show_list(self): # for showing all running shows
        print('\nAll Running Shows : ')
        print('\n---------------------------------------------------------\n')
        for id,name,time in self._show_list:
            print(f'Show id : {id} Movie Name : {name} Time : {time}')
        
        print('\n---------------------------------------------------------\n')

    def  view_available_seats(self,id):  # view avaible seat
        if(id not in self._seats):
            print("\nInvalid ID \n")
            return
        
        print('\n✅ ---> Available and ❌ ---> Booked\n')
        ct = 0
        for seat in self._seats[id]:
            print(seat)
            ct += seat.count('✅')
        print(f'\nTotal {ct} seat avaiable .\n')



# some show entry to the cinema hall

hall = Hall(10,10,101)
hall.entry_show(1001,'Priyotoma','10:00 PM')
hall.entry_show(1002,'Dhoom 3','1:00 AM')
hall.entry_show(1003,'Titanic','6:00 PM')
hall.entry_show(1004,'Puspa 2','12:00 AM')
hall.entry_show(1005,'KICK','2:00 PM')

# replica 
while True:
        print("\n========== Welcome to Star Cinema Hall ==========")
        print('''
            1. View All Shows
            2. View Avaiable Seats
            3. Book Seat
            4. Exit           
        ''')
        op = int(input("Enter option : "))
        if(op==4):
            print("Thank You !!!")
            break
        elif(op==1):
            hall.view_show_list()
        elif(op==2):
            id = int(input("Enter show id : "))
            hall.view_available_seats(id)
        elif(op==3):
            id = int(input("Enter cinema id :"))
            row,col = input("Enter row and col with comma separate : ").split(',')
            row = int(row)
            col = int(col)
            hall.book_seats(id,[(row,col)])
