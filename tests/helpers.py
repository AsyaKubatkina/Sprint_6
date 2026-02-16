def get_click_method(order, entry_point):
    actions = {
        "top": order.click_order_top,
        "bottom": order.click_order_bottom,
    }
    return actions[entry_point]