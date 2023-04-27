def oxford_comma(items):
    if len(items) == 1:
        return "".join(items)
    elif len(items) == 2:
        return " and ".join(items)
    elif len(items) >= 3:
        last_item = items.pop()
        new_string = ", ".join(items) + f", and {last_item}"
        return new_string
