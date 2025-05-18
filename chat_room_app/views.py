from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth  import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Customers,User,Chat,Chatroom
from django.contrib import messages
from django.utils import timezone
from django.utils.timezone import localtime




# Create your views here.
def demo(request):
    return render(request,'dashboard.html')
    
def admin_login(request):
    return render(request,'login.html')

def dashboard(request):
    return render(request,'dashboard.html')


def logins(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        
        user=authenticate(request,username=username,password=password)
        print(username)
        print(password)
        if user!=None:
                customer_obj = Customers.objects.filter(user_id=user).first()
                print(customer_obj)
                if customer_obj:
                    if customer_obj.status!='active':
                        messages.warning(request, 'you are inactive as of now.')
                        return redirect('admin_login')
                    else:
                        request.session['is_customer'] = True
              
                else:
                    request.session['is_customer'] = False

                login(request, user)
                messages.success(request, 'You have successfully logged in!')
                print(messages)
                if request.session['is_customer']==True:
                    return redirect('chatroom')
                else:
                    request.session['is_customer']==False
                    return redirect('customer')
        else:
            request.session['is_customer'] = False
            messages.error(request, 'Invalid username or password.')
            print(messages)
            return redirect('admin_login')
            
    else:
            request.session['is_customer'] = False
            messages.error(request, 'Invalid username or password.')
            print(messages)
            return redirect('admin_login')
      
def admin_logout(request):
    logout(request)
    return redirect('admin_login')

@login_required(login_url='/login/')
def customer(request):
    customer_obj=Customers.objects.all()
    context={"customer_obj":customer_obj}
    print(customer_obj)
    print(type(customer_obj))
    return render(request,'customer.html',context)

@login_required(login_url='/login/')
def add_customer(request):
    if request.method=="POST":
        customer_obj=Customers()
        user_obj=User()
        user_obj.first_name=request.POST['firstname']
        user_obj.last_name=request.POST['lastname']
        user_obj.username=request.POST['username']
        user_obj.email=request.POST['email']
        user_obj.set_password(request.POST['password'])
        user_obj.save()
        customer_obj.user_id=user_obj
        customer_obj.mobile_no=request.POST['mobile no']
        customer_obj.status=request.POST['status']
        customer_obj.save()
        return redirect('customer')
    else:
        print("add_customer")
        return render(request,'add_customer.html')
    
@login_required(login_url='/login/')
def get_customer(request,id):
    ed1_customer=Customers.objects.get(id=id)
    context={"ed1_customer":ed1_customer}
    return render(request,'edit_customer.html',context)

@login_required(login_url='/login/')
def edit_customer(request):
    if request.method=='POST':
        id=request.POST['id']
        print(request.POST['status'],'status')
        ed1_customer=Customers.objects.get(id=id)
        user_obj=User(id=ed1_customer.user_id.id)
        user_obj.first_name=request.POST['firstname']
        user_obj.last_name=request.POST['lastname']
        user_obj.username=request.POST['username']
        user_obj.email=request.POST['email']
        if request.POST['password']!='':
            user_obj.set_password(request.POST['password'])
        user_obj.save()
        ed1_customer.mobile_no=request.POST['mobile no']
        ed1_customer.status=request.POST['status']
        ed1_customer.save()
        return redirect('customer')

@login_required(login_url='/login/')
def delete_customer(request,id):
    customer_obj=Customers.objects.get(id=id)
    customer_obj.delete()
    return redirect('customer')

@login_required(login_url='/login/')
def chatroom(request):
    chatroom_obj=Chatroom.objects.all()
    context={"chatroom_obj":chatroom_obj}
    print(chatroom_obj)
    print(type(chatroom_obj))
    return render(request,'chatroom.html',context)

@login_required(login_url='/login/')
def add_chatroom(request):
        if request.method=="POST":
            chatroom_obj=Chatroom()
            chatroom_obj.title=request.POST['title']
            chatroom_obj.description=request.POST['description']
            chatroom_obj.valid_till=request.POST['valid_till']
            chatroom_obj.save()
            return redirect('chatroom')
        else:
            print("add_chatroom")
            return render(request,'add_chatroom.html')

@login_required(login_url='/login/')
def get_chatroom(request,id):
    edchat1_obj=Chatroom.objects.get(id=id)
    context1={"edchat1_obj":edchat1_obj} 
    return render(request,'edit_chatroom.html',context1)


@login_required(login_url='/login/')
def edit_chatroom(request):
    if request.method=='POST':
        id = request.POST['id']
        edchat1_obj = Chatroom.objects.get(id=id)
        edchat1_obj.title=request.POST['title']
        edchat1_obj.description=request.POST['description']
        edchat1_obj.valid_till=request.POST['valid_till']
        edchat1_obj.save()
        return redirect('chatroom')
    
@login_required(login_url='/login/')
def delete_chatroom(request,id):
    chatroom_obj=Chatroom.objects.get(id=id)
    chatroom_obj.delete()
    return redirect('chatroom')
    
@login_required(login_url='/login/')
def view(request):
        return render(request,'chatroom_view.html')

@login_required(login_url='/login/')
def chat_view(reqest,id):
    chatroom_obj=Chatroom.objects.get(id=id)
    chatview_obj=Chat.objects.filter(chatroom_id=chatroom_obj)
    context2={"chatview_obj":chatview_obj,"chatroom_obj":chatroom_obj}
    print(chatview_obj,'chatview_obj')
    return render(reqest,'chatroom_view.html',context2)

@login_required(login_url='/login/')
def edit_profile(request):
    if request.method=='POST':
        id=request.POST['id']
        ed1_user_profile=User.objects.get(id=id)
        ed1_user_profile.first_name=request.POST['firstname']
        ed1_user_profile.last_name=request.POST['lastname']
        ed1_user_profile.username=request.POST['username']
        if request.POST['password']!='':
            ed1_user_profile.set_password(request.POST['password'])
            ed1_user_profile.email=request.POST['email']
            ed1_user_profile.save()
        return redirect('edit_profile')
    else:
        user_flag=request.session['is_customer']
        id=request.user.id
        if user_flag:
            ed1_user_profile=Customers.objects.get(id=id)
        else:
            ed1_user_profile=User.objects.get(id=id)
            context={"ed1_user_profile":ed1_user_profile}
            return render(request,'edit_profile.html',context)
        
@login_required(login_url='/login/')
def edit_customer_profile(request):
    if request.method=='POST':
        id=request.POST['id']
        ed1_customer_profile=Customers.objects.get(id=id)
        user_obj=User.objects.get(id=ed1_customer_profile.user_id.id)
        user_obj.firstname=request.POST['firstname']
        user_obj.last_name=request.POST['lastname']
        user_obj.username=request.POST['username']
        if request.POST['password']!='':
            user_obj.set_password(request.POST['password'])
        user_obj.email=request.POST['email']
        user_obj.save()
        ed1_customer_profile.user_id=user_obj
        ed1_customer_profile.mobile_no=request.POST['mobile_no']
        ed1_customer_profile.save()
        return redirect('edit_customer_profile')    
    else:
        user_flag=request.session['is_customer']
        id=request.user.id
        if user_flag:
             ed1_customer_profile=Customers.objects.get(user_id=request.user)
        context={"ed1_customer_profile":ed1_customer_profile}
        return render(request,'edit_customer_profile.html',context)


@login_required(login_url='/login/')
def chatroom_view(request, id):
    chatroom_obj = Chatroom.objects.get(id=id)
    chat_obj = Chat.objects.filter(chatroom_id=chatroom_obj)

    for chat in chat_obj:
        chat.create_Date = localtime(chat.create_Date)  

    context = {"chat_obj": chat_obj, "chatroom_obj": chatroom_obj}
    return render(request, 'chat.html', context)


@login_required(login_url='/login/')
def add_new_chat(request):
    if request.method == 'POST':
        chatroom_obj = Chatroom.objects.get(id=request.POST['chatroom_id'])
        client_obj = Customers.objects.get(user_id=request.user)
        chat_obj = Chat()
        chat_obj.chatroom_id = chatroom_obj
        chat_obj.client_id = client_obj
        chat_obj.message = request.POST['message']
        
        
        if 'doc' in request.FILES:
            chat_obj.attechment = request.FILES['doc']
        
        chat_obj.save()
        return redirect('chatroom_view', id=chatroom_obj.id)



 
        















    









         
        
    