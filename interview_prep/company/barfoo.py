from enum import Enum
from collections import defaultdict


class EventMessageType(Enum):
    NEW = "NEW"
    ORDER_ACK = "ORDER_ACK"
    ORDER_REJECT = "ORDER_REJECT"
    CANCEL = "CANCEL"
    CANCEL_ACK = "CANCEL_ACK "
    CANCEL_REJECT = "CANCEL_REJECT"
    FILL = "FILL"


class Order(object):
    TYPE = "type"
    ORDER_ID = "order_id"
    TIME = "time"
    SIDE = "side"
    QUANTITY = "quantity"
    SYMBOL = "symbol"
    REASON = "reason"

    def __init__(self, order_id, *args, **kwargs):
        """
        Order constructor. All orders must have id, symbol, and amount
        Otherwise, add it as kwarg
        :param order_id:
        :param symbol:
        :param quantity:
        """
        self._order_id = order_id
        for k, v in kwargs.items():
            setattr(self, k, v)

class Event(object):
    def __init__(self):
        pass


class MarkingPositionMonitor:
    """
    NEW or "short" orders   => count immediately against marking position

    ORDER_ACK               => no effect on position

    ORDER_REJECT            => exchange rejected order, decrement order by amount fulfilled

    CANCEL                  => we requested, no change to marking position

    CANCEL_ACK              => order removed, decrement marking position

    CANCEL_REJECT           => order not changed, keep marking position

    FILL                    => order is partially or entirely filled. parse event and update marking position as follows,
                                marking_position = filled_orders - open_orders
    """
    def __init__(self):
        """

        """
        self._position = defaultdict(int)
        self._filled_orders = {}
        self._open_orders = {}
        pass

    @property
    def position(self):
        """
        :return:
        """
        return self._position

    def set_position(self, symbol, position):
        """
        :param symbol:
        return self._position

        :param position:
        :return:
        """
        pass

    @property
    def filled_orders(self):
        """
        :return:
        """
        return self._filled_orders

    @property
    def open_orders(self):
        """
        :return:
        """
        return self._open_orders

    def insert_order(self, order_id, data):
        """
        :param order_id:
        :param data:
        :return:
        """
        self._open_orders[order_id] = data

    def cancel_open_order(self, order_id):
        """
        :param order_id:
        :return:
        """
        if order_id not in self._open_orders:
            pass

    def on_event(self, message):
        message_type = message.get("type", None)
        order_id = message.get("order_id", None)

        args = {}
        for key, value in message.items():
            if Order.ORDER_ID != key:
                args.update({key: value})

        order = Order(order_id, args)

        if EventMessageType.NEW == message_type:
            self.create_new_order(order)

        elif EventMessageType.ORDER_ACK == message_type:
            # self.order_ack_handler(order)
            return self._position[order["symbol"]]

        elif EventMessageType.ORDER_REJECT == message_type:
            self.order_reject_handler(order)

        elif EventMessageType.CANCEL == message_type:
            #self.cancel_handler(order)
            return self._position[order["symbol"]]

        elif EventMessageType.CANCEL_ACK == message_type:
            # self.cancel_ack_handler(order)
            self._position[order["symbol"]] = 0
            return 0
        elif EventMessageType.CANCEL_REJECT == message_type:
            # self.cancel_reject_handler(order)
            pass
        elif EventMessageType.FILL == message_type:
            self.fill_order(order)
        else:
            pass

        symbol = message.get("symbol", self._open_orders["symbol"])

        return self._position[symbol]

    def create_new_order(self, order):
        """
        New order marked short.
            1. Add it to open orders,
            2. Decrement Marking Position
        :param message:
        :return:
        """
        symbol = order.symbol
        self._position["symbol"] = order["quantity"]
        pass

    def order_ack_handler(self, order):
        pass

    def order_reject_handler(self, order):
        pass

    def cancel_handler(self, order):
        pass

    def cancel_ack_handler(self, order):
        pass

    def cancel_reject_handler(self, order):
        pass

    def fill_order(self, order):
        pass


print(EventMessageType.FILL == "FILL")
"""
monitor = MarkingPositionMonitor()
event = {
    "type": "NEW",
    "symbol": "MSFT",
    "side": "SELL",
    "order_id": 5,
    "quantity": 1100,
    "time": "2016-12-22T12:07:04.521073"
}

monitor.on_event(event)
"""
