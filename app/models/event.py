class Event:
    def __init__(self, date, title, number_of_guests, room_location, description, recurring):
        self.date = date
        self.title = title
        self.number_of_guests = number_of_guests
        self.room_location = room_location
        self.description = description
        self.recurring = recurring