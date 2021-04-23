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
    def post(self,request):
        book_id = request.POST.get("bookid")

        book = Book.objects.get(pk=book_id)
        file_path = os.path.join(settings.MEDIA_ROOT+'/downloadpdf', str(book.pk)+'.pdf')
        if os.path.isfile(file_path):
            return HttpResponse("no file")


        else:
            return self.pdfreader(book)



    def pdfreader(self,book):
       # title = request.POST.get("title")[:20]

       # print(strip_tags(book.book_data))





        pdf_path = "testkese.pdf"
        server_webpath = "/var/www/zeppter/"

        pdf = PDF('P','mm',(200,500))
        pdf.alias_nb_pages()
        pdf.add_page()
        pdf.add_font("HidiShow", "" ,settings.BASE_DIR+"/static/assets/font/gargi.ttf",uni=True)
        pdf.set_font("HidiShow", "",25)
        
        image_url = settings.MEDIA_ROOT+'/'+str(book.book_image)
        pdf.write(15,book.book_title)
        pdf.ln(30)


        # pdf.cell(0,0,book.book_title)

       #  pdf.print_chapter(image_url,book.book_title,strip_tags(book.book_data))
     #   for titi in book.book_title.split('\n'):
     #       pdf.write(7,titi)
     #       pdf.ln(20)

      #  pdf.write(9,book.book_title)

       # pdf.set_left_margin(20)
        if os.path.isfile(image_url):
             pdf.image(image_url,pdf.get_x(),pdf.get_y(),100)
        print(book.book_image)
        pdf.ln(70)
        textg = strip_tags(book.book_data)

        pdf.add_font("HidiSh", "",settings.BASE_DIR+"/static/assets/font/gargi.ttf", uni=True)
        pdf.set_font("HidiSh" ,"" ,18)

        for tedt in textg.split('\n'):
           pdf.write(12,tedt)
           




        pdf.output(settings.BASE_DIR+'/media/downloadpdf/'+str(book.pk)+'.pdf', 'F')

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



