from django.shortcuts import render
def menuitems(request):
    menuitems = [
        {'name':'idli_sambar_combo','description':'This is dish from Tamilnadu and most parts of kerala','price':'280.00'},
        {'name':'rajmah_chawal','description':'This is dish from northinda which is kideneybeans and rice','price':'150.00'}
    ]
    context = {
        'menuitems':menuitems
    }
    return render(request, 'here will be requried app /menuitem.html', context )

