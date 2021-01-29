from django.shortcuts import render  , redirect  ,HttpResponse , get_object_or_404
from .forms import SignUpForm , edit_info , postt , comment_form
from .models import photo , more_user_info  , follow , comments
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    x = []
    following = follow.objects.filter(followers=request.user)
    if not following:
        return render(request,"not_follow.html")

    for f in following:
        x.append(f.followed_user)
    photoes = photo.objects.filter(created_by__in=x).order_by("-created_dt")
    return render(request,"home.html",{"photoes":photoes})



def search(request):
    return redirect("account:other_user_profile",user_name=request.POST["user"])


def main(request):
    return render(request,"main_page.html")



# SIGN UP VIEW
def signup(request):
    # MAKE SURE THAT LOGED IN USERS CANNOT SIGN UP AGAIN
    if  request.user.is_authenticated:
        return redirect("account:profile")
    # IF USER NOT authenticated
    else :
        form = SignUpForm()
        if request.method =='POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                auth_login(request,user)
                more_user_info.objects.create(
                    user=request.user
                )

                return redirect('account:profile')

        return render(request,'signup.html',{'form':form})


# PROFILE PAGE VIEW
@login_required
def profile(request):

    # DELET USER POST
    if request.method =='POST':
        post = photo.objects.get(pk=request.POST["pk"])

        if request.user  == post.created_by:
            post.delete()
    
    # TRY GET USER POSTS IF EXSIST
    try:
        posts = photo.objects.filter(created_by=request.user)
        posts_count = photo.objects.filter(created_by=request.user).count()
    except:
        posts = None


    user_info = more_user_info.objects.get(user=request.user)
    follows_count = follow.objects.filter(followed_user=request.user).count()
    following_count = follow.objects.filter(followers=request.user).count()
    posts_count = photo.objects.filter(created_by=request.user).count()
    context={"posts":posts,'user_info':user_info,"posts_count":posts_count,"follows_count":follows_count , "following_count":following_count}
    return render(request,"profile.html" ,context)


# EDIT USER INFO (BIO - PROFILE PIC - PHONE NUMBER)
@login_required
def profile_edit(request):
    
    user_info = more_user_info.objects.get(user=request.user)
    if request.method =='POST':
        form = edit_info(request.POST , request.FILES ,instance=user_info)
        if form.is_valid():
            form.save()
            return redirect("account:profile")
            
    form = edit_info(instance=user_info)
    return render(request,"edit.html" ,{'user_info':user_info,'form':form})



#  ADD PHOTO
@login_required
def add_post(request):
    if request.method =='POST':
        form = postt(request.POST , request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.created_by = request.user
            photo.post_more_user_info = more_user_info.objects.get(user=request.user)
            photo.save()
        return redirect("account:profile")


    form = postt()
    return render(request,"add_post.html" ,{"form":form})

@login_required
def other_user_profile(request , user_name):
    try :
        user_id = get_object_or_404(User,username=user_name)
    except:
        users = more_user_info.objects.filter(user__username__contains =user_name)
        return render(request,"user_notfound.html",{"users":users})
    try:
        other_user_photos = photo.objects.filter(created_by=user_id.pk)
        posts_count = photo.objects.filter(created_by=user_id.pk).count()
    except:
        other_user_photos = None

    other_user_info = more_user_info.objects.get(user=user_id.pk)

    try:
        follows_count = follow.objects.filter(followed_user=user_id.pk).count()
        is_follower = follow.objects.filter(followed_user=user_id.pk,followers=request.user)
    except :
        followes_count = "0"

    
    if request.method =='POST':
    
        if  str(request.user) == user_name :
            pass # not gone follow your self
        else:
            if is_follower :
                is_follower.delete()
            else:
                follow.objects.create(
                    followed_user= other_user_info.user,
                    followers= request.user ,
                    more_follower_info = more_user_info.objects.get(user=request.user) ,
                    more_followed_user_info =  other_user_info ,
                )

            return redirect("account:other_user_profile",user_name=user_name)
             
            
    context = {"other_user_photos":other_user_photos,"other_user_info":other_user_info,"posts_count":posts_count,"follows_count":follows_count,"is_follower":  is_follower}
    return render(request,"other_user_profile.html" ,context)


@login_required
def profile_follower(request):
    followers = follow.objects.filter(followed_user=request.user)
    return render(request,"profile_follower.html",{"followers":followers})

@login_required
def profile_following(request):
    following = follow.objects.filter(followers=request.user)
    return render(request,"profile_following.html",{"following":following})


@login_required
def post(request , id):
    post = get_object_or_404(photo,pk=id)
    photo_of_comment = more_user_info.objects.get(user=request.user)
    if request.method =='POST':
        form=comment_form(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) 
            comment.created_by = request.user
            comment.post = post
            comment.created_by_photo = photo_of_comment
            comment.save()

    comment = comments.objects.filter(post=post)

    form = comment_form()
    context={"form":form,"post":post,"comment":comment}
    return render(request,"post.html",context)