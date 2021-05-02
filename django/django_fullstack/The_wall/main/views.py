from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
from datetime import datetime
# Create your views here.


def index(request):
    if 'uid' in request.session:
        context = {
            "this_user": User.objects.get(id=request.session['uid']),
            "all_msgs": Message.objects.all(),
        }
        return render(request, "wall.html", context)

    else:
        return render(request, "login_reg.html")


def process_user(request):
    if request.method == 'POST':
        is_reg = request.POST.get('type')
        if is_reg == 'reg':  # registration
            errors = User.objects.reg_validator(request.POST)
            if len(errors) > 0:
                for key, val in errors.items():
                    messages.error(request, val)
                request.session['is_reg'] = "true"
                return redirect('/')
            else:
                fname = request.POST['fname']
                lname = request.POST['lname']
                email = request.POST['email']
                new_pass = bcrypt.hashpw(
                    request.POST['pass'].encode(), bcrypt.gensalt()).decode()
                bday = request.POST['bdate']
                new_user = User.objects.create(
                    first_name=fname, last_name=lname, email=email, password=new_pass, birthday=bday)
                request.session['uid'] = new_user.id
                request.session['is_reg'] = "true"
                return redirect('/wall')
        else:  # log in
            errors = User.objects.login_validator(request.POST)
            if len(errors) > 0:
                for key, val in errors.items():
                    messages.error(request, val)
                request.session['is_reg'] = "false"
                return redirect('/')
            else:
                # made sure email is unique upon registration
                logged_user = User.objects.get(email=request.POST['email'])
                if bcrypt.checkpw(request.POST['pass'].encode(), logged_user.password.encode()):
                    request.session['uid'] = logged_user.id
                    request.session['is_reg'] = "false"
                    return redirect('/wall')
                else:
                    messages.error(request, "invalid Log in")
                    return redirect('/')


def wall(request):
    if 'uid' in request.session:
        context = {
            "this_user": User.objects.get(id=request.session['uid']),
            "all_msgs": Message.objects.all(),
        }
        return render(request, "wall.html", context)
        
    else:
        return redirect("/")


def logout(request):
    request.session.flush()
    return redirect('/')


def msg_post(request):
    if request.method == 'POST':
        poster = User.objects.get(id=request.session['uid'])
        Message.objects.create(user=poster, msg_txt=request.POST['post_msg'])
        return redirect('/wall')


def msg_comment(request):
    if request.method == 'POST':
        commenter = User.objects.get(id=request.session['uid'])
        msg_to_comment_on = Message.objects.get(id=request.POST['msg_id'])
        Comment.objects.create(
            user = commenter, message=msg_to_comment_on, comment=request.POST['msg_cmnt'])
        return redirect('/wall')


def del_msg(request, id):
    msg_to_delete = Message.objects.get(id=id)
    created_on = msg_to_delete.created_at.date()
    today = datetime.today().date()
    if created_on == today:
        t1 = datetime.today().timestamp()
        t2 = msg_to_delete.created_at.timestamp()
        diff = (t1 - t2) / 60 # in minutes
        if diff <= 30:
            msg_to_delete.delete()
    return redirect('/wall')
