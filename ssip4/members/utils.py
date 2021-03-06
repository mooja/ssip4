from io import BytesIO

from django.template import Context, Template


from reportlab.pdfgen.canvas import Canvas

from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter, landscape

from reportlab.platypus import Spacer
from reportlab.platypus import Frame
from reportlab.platypus import Paragraph
from reportlab.platypus import PageTemplate
from reportlab.platypus import BaseDocTemplate


from .models import Member


def build_frames(pwidth, pheight, ncols):
    frames = []
    for i in range(ncols):
        f = Frame(x1=(i*((pwidth-30) / ncols)+15),
                  y1=0,
                  width=((pwidth-30) / ncols),
                  height=pheight+2,
                  leftPadding=15,
                  rightPadding=15,
                  topPadding=15,
                  bottomPadding=15,
                  showBoundary=True)
        frames.append(f)
    frames[0].showBoundary=False
    frames[3].showBoundary=False
    return frames


def make_pdf(ncolumns=4):
    NCOLUMNS = ncolumns
    PAGE_WIDTH, PAGE_HEIGHT = landscape(letter)

    styles = getSampleStyleSheet()

    buffer = BytesIO()
    ptemplate = PageTemplate(frames=build_frames(PAGE_WIDTH, PAGE_HEIGHT, NCOLUMNS))
    doc = BaseDocTemplate(
        filename=buffer,
        pagesize=landscape(letter),
        pageTemplates=[ptemplate],
        showBoundary=0,
        leftMargin=inch,
        rightMargin=inch,
        topMargin=inch,
        bottomMargin=inch,
        allowSplitting=0,
        title='SSIP209 Members Listing',
        author='Max Shkurygin',
        _pageBreakQuick=1,
        encrypt=None)

    template = Template(PDF_TEMPLATE)
    content = []
    for member in Member.objects.filter(is_active=True):
        context = Context({"member": member})
        p = Paragraph(template.render(context), styles["Normal"])
        content.append(p)
        content.append(Spacer(1, 0.3*inch))

    doc.build(content)
    pdf = buffer.getvalue()
    buffer.close()
    return pdf


PDF_TEMPLATE = """
<font size="14"><strong>{{ member.last_name }}, {{ member.first_name }}</strong></font>
<br/>

{% if member.address or member.town %}
    {{ member.address }}<br/>
    {% if member.town %} {{ member.town }} NY <br/>{% endif %}
{% endif %}

{% if member.homephone %}
(Home) {{ member.homephone }}
<br/>
{% endif %}

{% if member.cellphone %}
(Cell) {{ member.cellphone }}
<br/>
{% endif %}

{% if member.email %}
Email: {{ member.email }}
<br/>
{% endif %}

{% if member.hobbies %}
<strong>My Hobbies</strong>: {{ member.hobbies }}
<br/>
{% endif %}

{% if member.canhelp %}
<strong>I can help with</strong>: {{ member.canhelp }}
<br/>
{% endif %}

{% if member.needhelp %}
<strong>I could use help with</strong>: {{ member.needhelp }}
<br/>
{% endif %}


{% if member.emergency_first_name %}
    <strong>Emergency Contact</strong>: {{ member.emergency_first_name }}, {{ member.emergency_last_name }} <br/>
    {% if member.emergency_homephone %}
        (Home) {{ member.emergency_homephone }} <br/>
    {% endif %}
    {% if member.emergency_cellphone %}
        (Cell) {{ member.emergency_cellphone }} <br/>
    {% endif %}
    {% if member.emergency_comment  %}
        {{ member.emergency_comment }} <br/>
    {% endif %}
{% endif %}
"""