from . import util
from. import models
from django.http import HttpResponse
from django import forms
from django.shortcuts import render ,redirect
import random
import markdown2
from django.utils.safestring import mark_safe



# Définir un formulaire pour la création d'une nouvelle entrée
class EntryForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100)
    content = forms.CharField(label="Content", widget=forms.Textarea)

# Vue pour ajouter une nouvelle entrée
def add(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            entries=util.list_entries()
            if title not in entries:
                util.save_entry(title, content)
                return redirect('index')
            return HttpResponse("file exists")

        else:
            # Si le formulaire n'est pas valide, renvoyer le formulaire avec les erreurs
            return render(request, "encyclopedia/add.html", {
                "form": form
            })

    # Si la méthode est GET, afficher un formulaire vide
    return render(request, "encyclopedia/add.html", {
        "form": EntryForm()
    })



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
       
    })

def search(request):
    if request.method == 'POST':
        query = request.POST.get('q')
        matching_entries = [title for title in util.list_entries()
                            if title.lower() == query.lower() or query.lower() in title.lower()]
        return render(request, "encyclopedia/search.html", {
            "entries": matching_entries})
    return render(request, "encyclopedia/search.html")


def title(request ,title):
    return render(request, "encyclopedia/title.html",{
            "title": title,
            "entries": util.list_entries(),
            "contenu" : util.get_entry(title),})



def edit(request,title):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            
            new_content = form.cleaned_data['content']
            util.save_entry(title, new_content)
            return redirect('title',title)
    else:
        initial_data = {'title': title, 'content': util.get_entry(title)}
        form = EntryForm(initial=initial_data)    
    return render(request, "encyclopedia/edit.html", {
                "form": form , 'title':title })

def random_entr(request):
    entries= util.list_entries()
    random_entry = random.choice(entries)
    return render(request, "encyclopedia/random.html",{
        "title": random_entry,
        "contenu" : util.get_entry(random_entry)

    })
def convertir(request,title):
    with open(f"entries/{title}.md","r") as f_md:
        content_md = f_md.read()
    html_content=markdown2.markdown(content_md)
    contenu = mark_safe(html_content)
    with open(f"entries/{title}.html","w") as f_html:
        f_html.write(contenu)
    return render(request,"encyclopedia/convertir.html",{
        "title":title,
        "contenu":contenu})
    


