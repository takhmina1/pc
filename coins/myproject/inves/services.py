from .models import Investment, TradingStrategy, Trade

class InvestmentService:
    @staticmethod
    def get_investment_by_id(investment_id):
        try:
            return Investment.objects.get(id=investment_id)
        except Investment.DoesNotExist:
            return None

    @staticmethod
    def perform_some_action():
        pass

class TradingStrategyService:
    @staticmethod
    def get_all_strategies():
        return TradingStrategy.objects.all()

    @staticmethod
    def perform_some_action():
        pass

class TradeService:
    @staticmethod
    def create_trade(user, investment_id, amount):
        investment = InvestmentService.get_investment_by_id(investment_id)
        if investment:
            trade = Trade.objects.create(user=user, investment=investment, amount=amount)
            return trade
        return None

    @staticmethod
    def perform_some_action():
        pass

    @staticmethod
    def get_trades_by_user(user):
        # ваш код для получения сделок пользователя
        return Trade.objects.filter(user=user)