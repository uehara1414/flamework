from django.shortcuts import render
from flamework_app.models import DesignerIdea, EngineerIdea, IdeaImage
from .forms import DesignerIdeaForm


def index(request):
    return render(request, 'flamework_app/index.html')


def register(request):
    if request.method == 'POST':
        f = DesignerIdeaForm(request.POST)
        design_idea = f.save(commit=False)
        design_idea.user = request.user
        design_idea.save()
        for img in request.FILES.getlist('image', []):
            IdeaImage.objects.create(idea=design_idea, image=img)
    return render(request, 'flamework_app/register.html')


def mypage(request):
    return render(request, 'flamework_app/mypage.html')


def search(request):

    target = request.GET.get('target', 'designer')

    if target == 'designer':
        ideas = DesignerIdea.objects.all()
        context = {
            'ideas': ideas
        }
        return render(request, 'flamework_app/search_designers.html', context)
    else:
        ideas = EngineerIdea.objects.all()
        context = {
            'ideas': ideas
        }
        return render(request, 'flamework_app/search_engineers.html', context)


def engineer_idea_detail(request, pk):
    idea = EngineerIdea.objects.get(id=pk)
    context = {'idea': idea}
    return render(request, 'flamework_app/engineer_idea_detail.html', context)


def designer_idea_detail(request, pk):
    idea = DesignerIdea.objects.get(id=pk)
    images = IdeaImage.objects.filter(idea=idea)
    context = {'idea': idea, 'images': images}
    return render(request, 'flamework_app/designer_idea_detail.html', context)


def signup(request):
    return render(request, 'flamework_app/signup.html')


def signin(request):
    return render(request, 'flamework_app/signin.html')


def wish(request):
    return render(request, 'flamework_app/wish.html')


def onsale(request):
    return render(request, 'flamework_app/onsale.html')


def confirming(request):
    return render(request, 'flamework_app/confirming.html')


def sale_request(request):
    return render(request, 'flamework_app/sale_request.html')


def sale_request_submitted(request):
    return render(request, 'flamework_app/sale_request_submitted.html')


def buy_request(request):
    return render(request, 'flamework_app/buy_request.html')


def buy_request_submitted(request):
    return render(request, 'flamework_app/buy_request_submitted.html')


def onsale_list(request):
    return render(request, 'flamework_app/onsale_list.html')


def submitted_buy_request_list(request):
    return render(request, 'flamework_app/submitted_buy_request_list.html')


def edit_onsale(request):
    return render(request, 'flamework_app/edit_onsale.html')


def wish_list(request):
    return render(request, 'flamework_app/wish_list.html')


def edit_wish(request):
    return render(request, 'flamework_app/edit_wish.html')


def submitted_sale_request_list(request):
    return render(request, 'flamework_app/submitted_sale_request_list.html')


def sell(request):
    return render(request, 'flamework_app/sell.html')


def sell_confirm(request):
    return render(request, 'flamework_app/sell_confirm.html')


def sell_completed(request):
    return render(request, 'flamework_app/sell_completed.html')
