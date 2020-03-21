import braintree
from django.shortcuts import render, redirect, get_object_or_404
from orders.models import Order


# 支付流程
def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        # retrieve nonce检索支付令牌nonce
        nonce = request.POST.get('payment_method_nonce', None)
        # create and submit transaction创建并提交事务
        result = braintree.Transaction.sale({
            'amount': '{:.2f}'.format(order.get_total_cost()),
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True
            }
        })
        if result.is_success:
            # mark the order as paid将订单标记为已付款
            order.paid = True
            # store the unique transaction id存储唯一的事务id
            order.braintree_id = result.transaction.id
            order.save()
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')
    else:
        # generate token生成令牌
        client_token = braintree.ClientToken.generate()
        return render(request, 'payment/process.html', {'order': order, 'client_token': client_token})


# 付款完成
def payment_done(request):
    return render(request, 'payment/done.html')


# 付款取消
def payment_canceled(request):
    return render(request, 'payment/canceled.html')
