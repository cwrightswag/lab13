#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.



from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='black')
player = drawpad.create_oval(390,580,410,600, fill="red")

# Create your "enemies" here, before the class
circle = drawpad.create_oval(20, 20, 100, 100, fill='blue')
hi = drawpad.create_oval(300, 400, 100, 100, fill='hot pink')
yolo = drawpad.create_rectangle(390,580,350,500, fill='grey')
class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "green")
       	    self.up.grid(row=0,column=1)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="right", background = "hot pink")
       	    self.right.grid(row=1,column=2)
       	    self.right.bind("<Button-1>", self.rightClicked)
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="left", background = "yellow")
       	    self.left.grid(row=1,column=0)
       	    self.left.bind("<Button-1>", self.leftClicked)
       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="down", background = "light blue")
       	    self.down.grid(row=2,column=1)
       	    self.down.bind("<Button-1>", self.downClicked)
       	    
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=BOTTOM)
            self.animate()
	
	def animate(self):
	    global drawpad
	    global player
	    global circle
	    drawpad.move(circle,10,0)
            # Wait for 1 millisecond, then recursively call our animate function
            x1, y1, x2, y2 = drawpad.coords(circle)
            if x1 > 800: 
                drawpad.move(circle,-800,0)
            global hi
            drawpad.move(hi,-10,0)
            x1, y1, x2, y2 = drawpad.coords(hi)
            if x2 < 0: 
                drawpad.move(hi,800,0)
            global yolo
            drawpad.move(yolo,10,0)
            x1, y1, x2, y2 = drawpad.coords(yolo)
            if x1 > 800:
                drawpad.move(yolo,-800,0)
            drawpad.after(20, self.animate)
            
            
	    
	
	
	    # Remember to include your "enemies" with "global"
	    	
		
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
        def rightClicked(self, event):
           global oval
           global player
           drawpad.move(player,20,0)
        def leftClicked(self,event):
           global oval
           global player
           drawpad.move(player,-20,0)
        def downClicked(self, event):
           global oval
           global player
           drawpad.move(player,0,20)
		
		




















app = MyApp(root)
root.mainloop()