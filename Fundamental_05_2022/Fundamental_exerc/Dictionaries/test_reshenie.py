force_command = input()

force_book = {}


def force_side(side_, user_):
    for key in force_book:
        if user_ in force_book[key]:
            return
    force_book[side_] = force_book.get(side_, {})
    force_book[side_][user_] = force_book.get(side_, side_)


def force_change(user_, side_):
    for key in force_book:
        if user_ in force_book[key]:
            del force_book[key][user_]
            break
    force_book[side_] = force_book.get(side_, {})
    force_book[side_][user_] = force_book.get(side_, side_)
    print(f"{user_} joins the {side_} side!")


while force_command != "Lumpawaroo":

    if " | " in force_command:
        side, name = force_command.split(" | ")
        force_side(side, name)
    elif " -> " in force_command:
        side, name = force_command.split(" -> ")
        force_change(side, name)
    force_command = input()

for side in force_book:
    if force_book[side]:
        print(f"Side: {side}, Members: {len(force_book[side])}")
        for name in force_book[side]:
            print(f"! {name}")
