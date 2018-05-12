from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .numbersinword import NumberInWords


class FrontendView(View):
    template_name = "index.html"

    def get(self, request):
        number = request.GET.get('n', '')

        if number:
            number = request.GET.get('n', '')
            n = NumberInWords()
            number = n.toString(int(number))
            return JsonResponse({"success": "true", "number": number})

        return render(request, self.template_name)

    def contact(request):
        """
        Contact page
        :request: GET
        :returns: string
        """
        return render(request, 'contact.html')
