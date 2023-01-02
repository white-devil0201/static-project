from django.shortcuts import render

# Create your views here.
def my_view(request):
    myName = "GoluMolu"
    favActor = "Kartik Aryan"
    favAnimal = "Lion"
    favSub = "HTML/CSS"
    p = {"name" : myName, "actor" : favActor, "animal" : favAnimal, "subject" : favSub}
    return render(request, "myApp/1.html", p)