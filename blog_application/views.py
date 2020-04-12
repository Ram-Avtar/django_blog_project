from django.shortcuts import render
from .models import Post

# posts = [
#         {
#             'auther':'Ram',
#             'title':'post number one',
#             'content':'this is a first post',
#             'date_p':'nov 29 ,2019', 
#             },


#         {
#             'auther':'shyam',
#             'title':'post number two',
#             'content':'this is second post',
#             'date_p':'jan 01 ,2020', 
#             },

#         {
#             'auther':'sita',
#             'title':'post number tree',
#             'content':'this is third post',
#             'date_p':'jan 02 ,2020', 
#             },
#         ]



def home(request):
    contexts = {
            'post':Post.objects.all() ,
            }
    return render(request,'blog_application/home.html',contexts)

def about(request):
     return render(request,'blog_application/about.html',{'title':'about'})

