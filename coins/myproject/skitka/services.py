from .models import Discount, Transaction

def update_discount(user, amount):
    """
    Update user's discount based on transaction amount.
    """
    user_discount, created = Discount.objects.get_or_create(user=user)
    user_discount.total_transactions += amount

    # Update discount percentage based on total_transactions
    if user_discount.total_transactions < 500:
        user_discount.discount_percentage = 0.08
    elif 500 <= user_discount.total_transactions < 1000:
        user_discount.discount_percentage = 0.1
    elif 1000 <= user_discount.total_transactions < 2000:
        user_discount.discount_percentage = 0.12
    elif 2000 <= user_discount.total_transactions < 4000:
        user_discount.discount_percentage = 0.14
    elif 4000 <= user_discount.total_transactions < 6000:
        user_discount.discount_percentage = 0.16
    elif 6000 <= user_discount.total_transactions < 10000:
        user_discount.discount_percentage = 0.18
    else:
        user_discount.discount_percentage = 0.2

    user_discount.save()
