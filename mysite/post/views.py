from django.shortcuts import render

def index(request):

    if request.method == 'POST':
        content = request.POST.get('content', '')

        if content:
            print('content:', content)

            return redirect('index')

    return render( request ,'/post/index.html')