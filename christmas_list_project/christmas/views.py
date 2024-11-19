from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ChristmasList, GiftItem
from .forms import ChristmasListForm, GiftItemForm

@login_required
def my_lists(request):
    lists = ChristmasList.objects.filter(user=request.user)
    return render(request, 'christmas/my_lists.html', {'lists': lists})

@login_required
def create_list(request):
    if request.method == "POST":
        form = ChristmasListForm(request.POST)
        if form.is_valid():
            new_list = form.save(commit=False)
            new_list.user = request.user
            new_list.save()
            return redirect('my_lists')
    else:
        form = ChristmasListForm()
    return render(request, 'christmas/create_list.html', {'form': form})

def view_list(request, list_id):
    gift_list = get_object_or_404(ChristmasList, id=list_id)
    if gift_list.visibility == 'private' and gift_list.user != request.user:
        return redirect('login')  # Redirect unauthorized users
    return render(request, 'christmas/view_list.html', {'gift_list': gift_list})