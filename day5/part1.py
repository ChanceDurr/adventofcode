all_seats = [*range(0, 1024)]

max_seat_id = 0

with open('day5/input.txt') as f:
    seats = f.readlines()
    for seat in seats:
        seat = seat.strip('\n')

        # Get the row number
        start_row = [0, 127]
        n_of_seats = 128
        for letter in seat[:6]:
            n_of_seats = n_of_seats / 2
            if letter == 'F':
                start_row[1] -= n_of_seats
            if letter == 'B':
                start_row[0] += n_of_seats

        if seat[6] == "F":
            row = start_row[0]
        if seat[6] == "B":
            row = start_row[1]

        # Get the column number
        start_col = [0, 7]
        n_of_rows = 8
        for letter in seat[7:9]:

            n_of_rows = n_of_rows / 2
            if letter == 'L':
                start_col[1] -= n_of_rows
            if letter == 'R':
                start_col[0] += n_of_rows


        if seat[9] == "L":
            col = start_col[0]
        if seat[9] == "R":
            col = start_col[1]

        

        id = (row * 8) + col
        all_seats.remove(id)

for id in all_seats:
    if id+1 in all_seats or id-1 in all_seats:
        pass
    else:
        print('Your ID: ', id)
