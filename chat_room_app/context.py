from .models import Customers

def user_context(request):
    try:
        customer_obj=Customers.objects.filter(user_id=request.user).first()
        if customer_obj:
            is_customer=True
        else:
            is_customer=False
        return {"is_customer":is_customer,"user":request.user}

    except:
        return {"is_customer":False}