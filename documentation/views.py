from django.shortcuts import render
from django.http import HttpResponse
from .models import Department
from .models import Project
from .models import Document,Tags
from django.core.exceptions import ObjectDoesNotExist


def index(request):
	prod = Department.objects.all()
	pro = Project.objects.all()
	doc = Document.objects.filter(publish_mode=True)
	tag= Tags.objects.all()
	return render(request, 'documentation/index.html', {'products' : prod, 'projects':pro ,'docs':doc,'tags':tag} )

def detailproject(request,product_id,project_id,version_no):
	tag = Tags.objects.all()
	doc_page = Document.objects.filter(project__id = project_id,project__department=product_id,version=version_no,publish_mode=True)
	return render(request, 'documentation/document_page.html',{'doc_pages': doc_page,'tags': tag ,})

def detailproduct(request,product_id):
	try:
		prod = Department.objects.get(id=product_id)
	except ObjectDoesNotExist:
		prod='Product not exist'
	pro = Project.objects.filter(product=product_id)
	tag = Tags.objects.all()
	doc=Document.objects.filter(project__department=product_id,publish_mode=True)
	return render(request, 'documentation/projectlist_page.html',{'product' : prod, 'projects':pro ,'docs':doc,'tags': tag} )

def page(request,tag_id):
	prod = Department.objects.all()
	pro = Project.objects.all()
	doc = Document.objects.all()
	tag = Tags.objects.all()
	doc_page = Document.objects.filter(tags__in=tag_id,publish_mode=True)
	return render(request, 'documentation/tagpage.html', {'products' : prod, 'projects':pro ,'doc_pages': doc_page,'docs':doc,'tags':tag} )


# Create your views here.

