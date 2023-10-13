from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle 
from reportlab.lib import colors 
from reportlab.lib.pagesizes import A4 
from reportlab.lib.styles import getSampleStyleSheet 
  
DATA = [ 
    [ "Date" , "Name", "Subscription", "Price (Rs.)" ], 
    [ 
        "16/03/2023", 
        "Maths by Gagan pratap", 
        "20-feb- 2025", 
        "2000.00/-", 
    ], 
    [ "10/03/2023", "English by Reetu Singh,Vol-1", "15-feb-2025", "1000.00/-"], 
    [ "Sub Total", "", "", "3000.00/-"], 
    [ "Discount", "", "", "-100.00/-"], 
    [ "Total", "", "", "2,900.00/-"], 
] 
  
pdf = SimpleDocTemplate( "receipt.pdf" , pagesize = A4 ) 
  
styles = getSampleStyleSheet() 
  
title_style = styles[ "Heading1" ] 
  
title_style.alignment = 1
  
title = Paragraph( "Payment Receipt" , title_style ) 
  
style = TableStyle( 
    [ 
        ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ), 
        ( "GRID" , ( 0, 0 ), ( 4 , 4 ), 1 , colors.black ), 
        ( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.gray ), 
        ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ), 
        ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ), 
        ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ), 
    ] 
) 


table = Table( DATA , style = style ) 
  
pdf.build([ title , table ]) 