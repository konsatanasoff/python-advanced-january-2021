from collections import deque


def stock_availability(list, action, *args):
    cupcakes = deque(list)

    if action == "delivery":
        for el in args:
            cupcakes.append(el)

    elif action == "sell":
        if args:
            if isinstance(args[0], str):
                # cupcakes = deque([el for el in cupcakes if not el == args[0]])
                for arg in args:
                    cupcakes = deque([el for el in cupcakes if not el == arg])
            else:
                for _ in range(args[0]):
                    cupcakes.popleft()

        else:
            cupcakes.popleft()

    return [el for el in cupcakes]


# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
