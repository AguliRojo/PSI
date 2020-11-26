def function(data_text):
    lenght = len(data_text)
    letters = list(data_text)
    big_letters = data_text.upper()
    small_letter = data_text.lower()
    slow = {
        "lenght": lenght,
        "letters": letters,
        "big_letters": big_letters,
        "small_letter": small_letter
    }
    # loop is made for creating new line after new key + value is returned.
    # Return slow is aceptable, but not well formatted
    for k, v in slow.items():
        print(k, '-->', v)


function("Ziemniak")
