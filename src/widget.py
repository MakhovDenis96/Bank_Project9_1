from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """Функция для маскировки номера карты или счета."""

    card_info =[]
    if "счет" in account_info.lower():
        score_list = account_info.split()
        masked_score  = get_mask_account("".join(score_list[-1]))
        return f"Счет {masked_score}"

    else:
        card_list = account_info.split()

        for card_num in card_list:
            if card_num.isalpha():
                card_info.append(card_num)
            elif card_num.isdigit():
                masked_card = get_mask_card_number(card_num)
                card_info.append(masked_card)
            else:
                print("Ошибка! Такой карты не существует")
        return " ".join(card_info)


print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))


def get_date(date_time: str) -> str:
    """Функция, которая реформатитрует дату"""
    date_info = date_time[:10].split("-")
    return ".".join(date_info[::-1])


print(get_date("2024-03-11T02:26:18.671407"))
