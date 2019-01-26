from django.shortcuts import render
from .models import URLPattern

#View function of homepage (accessed when no further pattern is provided after the main website URL)
def URL(request):
    searched = None   #initialized to none (no input in input bar) 

    if(request.GET.get('searchBtn')):  #checks if value is entered into input bar and submitted
        URL_Map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        searched = request.GET['searchBox']   #retrieve long URL value from search bar

        #check duplicate
        selectedURL = URLPattern.objects.filter(longURL=searched)
        if (len(selectedURL)!=0):       #catches duplicate and displays message
            context = {
                'selectedURL': selectedURL,
                'searched': searched,
                'URLTyped': True,
                'duplicate': True,
            }
            return render(request, 'homePage.html', context)

        #create database entry if no duplicate found
        selectedURL = URLPattern.objects.create(longURL=searched)
        selectedID = selectedURL.id
        #need to convert long URL through the use of the database ID to a order of 62 number such that URL_Map can be used to map correspond values

        #find numerical value of entered input
        accum = 0
        for i in searched:
            accum = accum + ord(i)
        int(accum)

        #find shortened mapped value
        shortURL = ''
        while (accum !=0):
            remainder = accum % 62
            shortURL = shortURL + URL_Map[int(remainder)]
            accum = (accum - remainder)/62

        #shortURL now stores the value of the converted short URL
        #Queryset for newly created URL pattern and send data to template for display
        URLPattern.objects.filter(id=selectedID).update(shortURL=shortURL)
        selectedURL = URLPattern.objects.get(id=selectedID)
        context = {
            'selectedURL': selectedURL,
            'searched': searched,
            'URLTyped': True,
            'shortenedURL': shortURL,
            'duplicate': False,
        }
        return render(request, 'homePage.html', context)

    #if no URL is typed into search bar (ie. homepage reached by just www.example.com)
    context = {
        'searched': searched,
        'URLTyped': False,
        'duplicate': False,
    }

    return render(request, 'homePage.html', context)


#View function to arrive to a given URL given the long or short URL pattern
def URLstr(request, URLstr):
    notFound = False

    #try to find short URL submitted
    selectedURL = URLPattern.objects.filter(longURL=URLstr).order_by().distinct()
    if len(selectedURL) == 0: #if short URL not found, check whether long URL inputted instead
        selectedURL = URLPattern.objects.filter(shortURL=URLstr).order_by().distinct()
        if (len(selectedURL)==0):  #if an invalid URL is inputted
            notFound = True
    
    if len(selectedURL) != 0: #increments the number of visits to the URL by 1 if valid URL is inputted
        selectedURL[0].visits = selectedURL[0].visits + 1
        selectedURL[0].save()

    context = {
        'URLstr': URLstr,
        'notFound': notFound,
        'selectedURL': selectedURL,       
    }

    return render(request, 'longURL.html', context)


