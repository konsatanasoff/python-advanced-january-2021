def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())
    return lines


def input_until_command(end_command):
    lines = []
    while True:
        command = input()
        if command == end_command:
            break
        lines.append(command)
    return lines


def is_vip_check(guest):
    return guest[0].isdigit()


def vip_regular_separation(guests):
    vip_guests = []
    regular_guests = []
    for guest in guests:
        if is_vip_check(guest):
            vip_guests.append(guest)
        else:
            regular_guests.append(guest)
    return sorted(vip_guests), sorted(regular_guests)


def print_result(guests):
    print(len(guests))
    (vip_guests, regular_guests) = vip_regular_separation(guests)

    for guest in vip_guests:
        print(guest)
    for guest in regular_guests:
        print(guest)


guest_count = int(input())
reservations = input_to_list(guest_count)
guests_arrived = input_until_command('END')
not_arrived = set(reservations).difference(guests_arrived)

print_result(not_arrived)
