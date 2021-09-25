from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from blog.models import Post

posts = [
    {
        'author':'Edil',
        'title':'Omur bayan',
        'content':'lerning pubg soo easy Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda commodi culpa distinctio fugit hic itaque nobis perferendis similique totam vitae. Amet consequatur debitis, deserunt ea est facere iste laboriosam, magni mollitia nihil nisi officiis praesentium sit! Aut dolor iusto laborum maxime perspiciatis praesentium quia rerum vero vitae voluptatibus? Ea, quo!',
        'post_date':'21.09.2021'
    },

    {
        'author': 'Islam',
        'title': 'love story',
        'content': 'jealous to Edil Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda commodi culpa distinctio fugit hic itaque nobis perferendis similique totam vitae. Amet consequatur debitis, deserunt ea est facere iste laboriosam, magni mollitia nihil nisi officiis praesentium sit! Aut dolor iusto laborum maxime perspiciatis praesentium quia rerum vero vitae voluptatibus? Ea, quo!',
        'post_date': '18.08.2021'
    }
]


def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'about'})
