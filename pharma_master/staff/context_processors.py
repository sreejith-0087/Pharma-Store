from staff.models import Categories

def Medicine_Category(request):
    cat=Categories.objects.all()
    return dict(cat=cat)