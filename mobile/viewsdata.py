import mimetypes
from wsgiref.util import FileWrapper

from appdirs import unicode
from django.views.generic import View
from django.http import FileResponse, HttpResponse, Http404
from zeppter import settings
from fpdf import FPDF
import os.path
import pathlib
from fpdf import FPDF,HTMLMixin
from admin_dashboard.models import Book
from django.utils.encoding import iri_to_uri, smart_str

from django.utils.html import strip_tags
class DownloadPDF(View):
    def get(self,request):
       # title = request.POST.get("title")[:20]
        book_id = request.GET.get("bookid")
        book = Book.objects.get(pk=book_id)
       # print(strip_tags(book.book_data))





        pdf_path = "testkese.pdf"
        server_webpath = "/var/www/zeppter/"

        pdf = PDF(orientation = 'P', unit = 'mm', format="A5")
        pdf.alias_nb_pages()
        pdf.add_page()
        pdf.add_font("HidiShow", "" ,server_webpath+"static/assets/font/gargi.ttf",uni=True)
        pdf.set_font("HidiShow", "",20)
        image_url = server_webpath+"media/"+str(book.book_image)
        pdf.write(6,book.book_title)
        pdf.ln(8)


        # pdf.cell(0,0,book.book_title)

       #  pdf.print_chapter(image_url,book.book_title,strip_tags(book.book_data))
     #   for titi in book.book_title.split('\n'):
     #       pdf.write(7,titi)
     #       pdf.ln(20)

      #  pdf.write(9,book.book_title)

       # pdf.set_left_margin(20)
        pdf.image(image_url,pdf.get_x(),pdf.get_y(),100)
        pdf.ln(70)
        textg = strip_tags(book.book_data)

        pdf.add_font("HidiSh", "",server_webpath+ "static/assets/font/gargi.ttf", uni=True)
        pdf.set_font("HidiSh" ,"" ,10)

        for tedt in textg.split('\n'):
           pdf.write(8,tedt)
           




        pdf.output(server_webpath+'media/downloadpdf/'+str(book.pk)+'.pdf', 'F')

        if pathlib.Path(pdf_path).exists() :
            print("no file data")

        return HttpResponse("upload complite")


# return FileResponse(pdf_path)



class PDF(FPDF,HTMLMixin):
    def header(self):
        # Logo
    #    self.image('logo_pb.png', 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
      #  self.cell(30, 10, 'Title', 1, 0, 'C')
        # Line break
        self.ln(20)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


    def my_title(self,title):
         self.set_text_color("#000000")
         self.set_font_size("30")

         self.cell(txt="hello",align="C")

    def getmyimage(self,myimage):
        self.c_margin()
        self.cell(0,0,)
       # self.image(settings.BASE_DIR+"/media/"+str(myimage),0, 0, 0)
    def maincontent(self,datashow):
        for txt in datashow.split('\n'):
            self.write(8,txt)
            self.ln(8)

    def print_chapter(self, image, title, data):
        self.add_page()
        self.my_title(title)

        self.getmyimage(image)
        self.maincontent(data)



