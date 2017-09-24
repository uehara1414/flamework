from django.shortcuts import render, redirect
from flamework_app.models import DesignerIdea, EngineerIdea, IdeaImage, UserInfo
from .forms import DesignerIdeaForm, UserInfoForm


def index(request):
    return render(request, 'flamework_app/index.html')


def register(request):
    if request.method == 'POST':
        f = DesignerIdeaForm(request.POST)
        design_idea = f.save(commit=False)
        design_idea.user = request.user
        design_idea.save()

        f = UserInfoForm(request.POST)
        user_info = f.save(commit=False)
        user_info.user = request.user
        user_info.digest_address(request.POST['address'])

        for img in request.FILES.getlist('image', []):
            IdeaImage.objects.create(idea=design_idea, image=img)
        return redirect('/mypage/')

    elif request.method == 'GET':
        form = UserInfoForm()
        return render(request, 'flamework_app/register.html', {'form': form})


def register_idea(request):
    if request.method == 'POST':
        f = DesignerIdeaForm(request.POST)
        design_idea = f.save(commit=False)
        design_idea.user = request.user
        design_idea.save()

        for img in request.FILES.getlist('image', []):
            IdeaImage.objects.create(idea=design_idea, image=img)
        return redirect('/mypage/')

    elif request.method == 'GET':
        form = UserInfoForm()
        return render(request, 'flamework_app/register.html', {'form': form})


def mypage(request):
    return render(request, 'flamework_app/mypage.html')


def search(request):

    def distance(idea: DesignerIdea):
        return idea.user.userinfo.get_zip_distance(request.user.userinfo.zipcode)

    target = request.GET.get('target', 'designer')

    if target == 'designer':
        ideas = list(sorted(DesignerIdea.objects.all(), key=lambda x: x.image_num, reverse=True))
        ideas = list(sorted(ideas, key=lambda i: distance(i)))
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
