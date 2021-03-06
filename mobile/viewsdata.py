import mimetypes
import numbers
from typing import Text
from wsgiref.util import FileWrapper
import operator
import json

from appdirs import unicode
from django.views.generic import View
from django.http import FileResponse, HttpResponse, Http404
from reportlab.lib.colors import Color
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import BaseDocTemplate, PageTemplate, Image, Paragraph, Frame
from reportlab.platypus.paragraph import stringWidth

from zeppter import settings
from fpdf import FPDF
import os.path

from django.shortcuts import render
import pathlib
from fpdf import FPDF,HTMLMixin
from admin_dashboard.models import Book
from django.utils.encoding import iri_to_uri, smart_str
from bs4 import BeautifulSoup


from django.utils.decorators import method_decorator
from mobile.middleware.login import LOGIN_MOBILE

from django.utils.html import strip_tags

mobile_size = (120 * mm, 297 * mm)


class DownloadPDF(View):
    def post(self,request):
        book_id = request.POST.get("bookid")

        book = Book.objects.get(pk=book_id)
        file_path = os.path.join(settings.MEDIA_ROOT+'/downloadpdf', str(book.pk)+'.pdf')
        if os.path.isfile(file_path):
            return HttpResponse("no file")


        else:
            return self.pdfreader(book)



    def pdfreader(self,book):


        style = getSampleStyleSheet()['Normal']
        style.fontName = 'Montserratd'
        #style.spaceBefore = 20
        style.leading=24
        style.spaceBefore = 25


        elements = []

        doc = BaseDocTemplate(settings.BASE_DIR+'/media/downloadpdf/'+str(book.pk)+'.pdf', showBoundary=1, pagesize=mobile_size)
        pdfmetrics.registerFont(TTFont('Montserrat',settings.BASE_DIR+ '/fonts/Hind-SemiBold.ttf'))
        pdfmetrics.registerFont(TTFont('Montserratd',settings.BASE_DIR+ '/fonts/Martel-ExtraLight.ttf'))


        frameT = Frame(5 * mm,5*mm,110*mm,287 *mm,showBoundary=2)
       # TopCenter = Frame(1.2 * inch, height - 1.2 * inch, width - 2.4 * inch, 1 * inch, showBoundary=1, id='normal')

        frame1 = Frame(0,0, doc.width / 2 - 3, doc.height, id='col1')
        frame2 = Frame(doc.leftMargin + doc.width , doc.bottomMargin, doc.width , doc.height, id='col2')

        doc.addPageTemplates([
            PageTemplate(id='basedoc', frames=frameT),
       #     PageTemplate(id='TwoCol', frames=[frame1, frame2]),
        ])
        im = Image(settings.BASE_DIR+'/media/'+str(book.book_image),80* mm,200)
        styles = getSampleStyleSheet()
        yourStyle = ParagraphStyle('yourtitle',
                                   fontName="Montserrat",
                                   fontSize=16,
                                   #       parent=style['Heading2'],
                                   alignment=1,
                                   leading = 20,

                                   spaceAfter=30)
        # styletitle.alignment = TA_CENTER

        elements.append(Paragraph(book.book_title, yourStyle))
        elements.append(im)
        for txtd in strip_tags(book.book_data).split('\n'):
            elements.append(Paragraph(txtd ,style))

        # start the construction of the pdf
        doc.build(elements, canvasmaker=NumberedCanvas)
        return HttpResponse("writer is susesss")

# return FileResponse(pdf_path)



class NumberedCanvas(canvas.Canvas):
            def __init__(self, *args, **kwargs):
                canvas.Canvas.__init__(self, *args, **kwargs)
                self._saved_page_states = []

            def showPage(self):
                self._saved_page_states.append(dict(self.__dict__))
                self._startPage()

            def save(self):
                """add page info to each page (page x of y)"""
                num_pages = len(self._saved_page_states)
                for state in self._saved_page_states:
                    self.__dict__.update(state)
                    self.draw_page_number(num_pages)
                    canvas.Canvas.showPage(self)
                canvas.Canvas.save(self)

            def draw_page_number(self, page_count):
                self.setFont('Montserrat', 9)
                self.setLineWidth(0.1)
                self.setStrokeColor(Color(0, 0, 0, alpha=0.2))
                self.setFillColor(Color(0, 0, 0, alpha=0.4))
                #self.line(cm, 1.5 * cm, A4[0] - cm, 1.5 * cm)
                self.drawRightString(mobile_size[0] -cm,3, "Page %d of %d" % (self._pageNumber, page_count))


@method_decorator(LOGIN_MOBILE,name="dispatch")
class CreateBook(View):
    def post(self,request):
       if  "book_title" in request.POST:


           book_title = request.POST["book_title"]
           if book_title != "":
               return None

       else:
               return render(request,"mobile/dashboard/load/create_post.html")




class Books(View):
    def post(self,req):
        if 'id' in  req.POST and 'books' in req.POST :
            id = json.loads(req.POST['id'])
            b_json =req.POST['books']
           # print(id)

            mybooks = []
            books = json.loads(b_json)[:5]

        #    print(books)

            for book in books:
                bd = Book.objects.get(id=book)

                mybooks.append(bd)
              #  mybooks += bd
            for fg in id:
                c_book = Book.objects.filter(pk=fg)[:2]
                if mybooks.count(c_book) is not 1:
                    for gf in  c_book:
                        mybooks.append(gf)





            return render(req,'mobile/dashboard/load/book.html',{'mybook':mybooks[:12]})

        elif 'books' in req.POST and req.POST['books'] is not 'not':
           # id = json.loads(req.POST['id'])
            b_json = req.POST['books']
            # print(id)

            mybooks = []
            books = json.loads(b_json)

            #    print(books)

            for book in books:
                bd = Book.objects.get(id=book)

                mybooks.append(bd)
            return render(req, 'mobile/dashboard/load/book.html', {'mybook': mybooks[:5]})
        else:
          books =   Book.objects.all()[:5]
          return render(req, 'mobile/dashboard/load/book.html', {'mybook': books})




