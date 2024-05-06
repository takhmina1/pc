from .models import UserProfile, CryptoWallet, FiatWallet, Cryptocurrency, FiatCurrency, Transaction

def get_user_profile(user):
    # Получить профиль пользователя.
    # Если профиль уже существует, возвращает его.
    # Если нет, создает новый профиль для указанного пользователя.
    return UserProfile.objects.get_or_create(user=user)[0]

def get_crypto_wallet(user, cryptocurrency):
    # Получить кошелек для криптовалюты пользователя.
    # Если кошелек уже существует, возвращает его.
    # Если нет, создает новый кошелек для указанного пользователя и криптовалюты.
    return CryptoWallet.objects.get_or_create(user=user, cryptocurrency=cryptocurrency)[0]

def get_fiat_wallet(user, fiat_currency):
    # Получить кошелек для фиатной валюты пользователя.
    # Если кошелек уже существует, возвращает его.
    # Если нет, создает новый кошелек для указанного пользователя и фиатной валюты.
    return FiatWallet.objects.get_or_create(user=user, fiat_currency=fiat_currency)[0]

def get_cryptocurrency_by_id(cryptocurrency_id):
    # Получить криптовалюту по ее идентификатору.
    return Cryptocurrency.objects.get(pk=cryptocurrency_id)

def get_fiat_currency_by_id(fiat_currency_id):
    # Получить фиатную валюту по ее идентификатору.
    return FiatCurrency.objects.get(pk=fiat_currency_id)

def create_transaction(user_profile, transaction_type, cryptocurrency=None, fiat_currency=None, amount=0, price=0, commission=0):
    # Создать новую транзакцию.
    # Принимает профиль пользователя, тип транзакции,
    # криптовалюту или фиатную валюту, сумму, цену и комиссию.
    # Возвращает созданную транзакцию.
    return Transaction.objects.create(user=user_profile, transaction_type=transaction_type, cryptocurrency=cryptocurrency, fiat_currency=fiat_currency, amount=amount, price=price, commission=commission)


def get_user_profile(user):
    """
    Получить профиль пользователя.

    Если профиль уже существует, возвращает его.
    Если нет, создает новый профиль для указанного пользователя.

    Args:
        user: Объект пользователя.

    Returns:
        Профиль пользователя.
    """
    return UserProfile.objects.get_or_create(user=user)[0]

def get_crypto_wallet(user, cryptocurrency):
    """
    Получить кошелек для криптовалюты пользователя.

    Если кошелек уже существует, возвращает его.
    Если нет, создает новый кошелек для указанного пользователя и криптовалюты.

    Args:
        user: Объект пользователя.
        cryptocurrency: Объект криптовалюты.

    Returns:
        Кошелек для криптовалюты.
    """
    return CryptoWallet.objects.get_or_create(user=user, cryptocurrency=cryptocurrency)[0]

def get_fiat_wallet(user, fiat_currency):
    """
    Получить кошелек для фиатной валюты пользователя.

    Если кошелек уже существует, возвращает его.
    Если нет, создает новый кошелек для указанного пользователя и фиатной валюты.

    Args:
        user: Объект пользователя.
        fiat_currency: Объект фиатной валюты.

    Returns:
        Кошелек для фиатной валюты.
    """
    return FiatWallet.objects.get_or_create(user=user, fiat_currency=fiat_currency)[0]

def get_cryptocurrency_by_id(cryptocurrency_id):
    """
    Получить криптовалюту по ее идентификатору.

    Args:
        cryptocurrency_id: Идентификатор криптовалюты.

    Returns:
        Криптовалюта.
    """
    return Cryptocurrency.objects.get(pk=cryptocurrency_id)

def get_fiat_currency_by_id(fiat_currency_id):
    """
    Получить фиатную валюту по ее идентификатору.

    Args:
        fiat_currency_id: Идентификатор фиатной валюты.

    Returns:
        Фиатная валюта.
    """
    return FiatCurrency.objects.get(pk=fiat_currency_id)

def create_transaction(user_profile, transaction_type, cryptocurrency=None, fiat_currency=None, amount=0, price=0, commission=0):
    """
    Создать новую транзакцию.

    Args:
        user_profile: Профиль пользователя.
        transaction_type: Тип транзакции.
        cryptocurrency: Криптовалюта (если есть).
        fiat_currency: Фиатная валюта (если есть).
        amount: Сумма транзакции.
        price: Цена единицы криптовалюты или фиатной валюты.
        commission: Комиссия.

    Returns:
        Созданная транзакция.
    """
    return Transaction.objects.create(user=user_profile, transaction_type=transaction_type, cryptocurrency=cryptocurrency, fiat_currency=fiat_currency, amount=amount, price=price, commission=commission)


