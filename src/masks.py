def get_mask_card_number(number_card: str) -> str:
    """Функция маскировки номера банковской карты"""

    number_card_1 = "".join(number_card)
    number_card_1 = number_card_1.replace(number_card_1[6:-4], "******")
    mask_card = " ".join(number_card_1[i:i+4] for i in range(0, len(number_card_1), 4))
    return mask_card


def get_mask_account(number_account: str) -> str:
    """Функция маскировки номера банковского счета"""
    number_account = number_account.replace(" ", "")
    mask_account = str(number_account[-4:])
    return f"**{mask_account}"



