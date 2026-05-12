from datetime import datetime
from src.masks import get_mask_card_number, get_mask_account  # Импорт ваших старых функций


def mask_account_card(card_string: str) -> str:
    """
    Маскирует номер карты или счёта из одной строки.
    Пример: 'Visa Platinum 7000792289606361' -> 'Visa Platinum 7000 79** **** 6361'
            'Счет 73654108430135874305' -> 'Счет **4305'
    """
    parts = card_string.split()
    number = parts[-1]  # Последний элемент всегда номер
    card_type = " ".join(parts[:-1])  # Всё остальное - тип

    if card_type.lower() == "счет":
        masked = get_mask_account(number)
    else:
        masked = get_mask_card_number(number)

    return f"{card_type} {masked}"