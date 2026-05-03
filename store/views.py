from django.shortcuts import render

def home(request):
    """
    Renders the homepage of the store application.

    Args:
        request: HTTP request object

    Returns:
        Rendered HTML page
    """
    return render(request, "home.html")
