hotel_dict = { 'data': { 'rooms': 
    [ { 'id': 1, 'room_number': "201", 'capacity': 50}, { 'id': 2, 'room_number': "301", 'capacity': 200 }, { 'id': 3, 'room_number': "1B", 'capacity': 100}
    ],
    'events': [
      { 'id': 1, 'room_id': 2, 'start_time': 18, 'end_time': 20, 'attendees': 75 },
      { 'id': 2, 'room_id': 1, 'start_time': 10, 'end_time': 18, 'attendees': 25 },
      { 'id': 3, 'room_id': 2, 'start_time': 10, 'end_time': 18, 'attendees': 20 },
      { 'id': 4, 'room_id': 3, 'start_time': 18, 'end_time': 21, 'attendees': 56 },
    ]
  }
}

# Retrieve the capacity of room 201 and store it in a variable.
room_201 = hotel_dict['data']['rooms'][0]['capacity']






# # Find all the events taking place in room 201. Iterate through them and print "ok" if the number of planned attendees will fit in the room.
# print(hotel_dict['data']['rooms'][0]['id'])
# print(hotel_dict['data']['events'][0]['room_id'])
i = 0
while i < 4:
    if hotel_dict['data']['rooms'][0]['id'] == hotel_dict['data']['events'][i]['room_id']:
        if room_201 > hotel_dict['data']['events'][i]['attendees']:
            print("ok")
    else:
            print("cannot fit")
    i += 1