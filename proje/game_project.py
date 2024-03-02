from graphics import Canvas
import time
import random

zombi_list = []
can_list = []
zombi_time = []
bullet_list=[]

def main():    
    canvas=Canvas(1000,1000)
    w = canvas.get_canvas_width()
    h = canvas.get_canvas_height()
    game_time = 120
    heart = 1
    time_piece = 0
    delay = 0.2
    canvas.set_canvas_title('Survival game')
    start_screen = canvas.create_image_with_size(0, 0, 1000, 1000, 'start_screen.jpg')
    x0 =canvas.get_canvas_width()/2 - 20
    x1 = x0 + 40
    y0 =canvas.get_canvas_height()/2 +40
    y1 = y0 + 40
    button = canvas.create_rectangle(x0,y0,x1,y1)
    canvas.set_color(button, 'white')
    text =canvas.create_text(x0+20, y0+20 , 'START')
    button2 = canvas.create_rectangle(x0,y0 +50,x1,y1 +50)
    canvas.set_color(button2, 'white')
    text2 =canvas.create_text(x0+20, y0+70 , 'OPTİON')
    dx = random.randint(1,4)
    dy = random.randint(3,5)
    
    n = 1
    while n>0 :
       clicks = canvas.get_new_mouse_clicks()
       for click in clicks:
            click_on_the_object=canvas.find_element_at(click.x, click.y)
            if click_on_the_object and click_on_the_object!=start_screen and click_on_the_object!=button2 and click_on_the_object!=text2:
                canvas.delete_all()
                n =0
            if click_on_the_object and click_on_the_object!=start_screen and click_on_the_object!=button and click_on_the_object!=text:
                option(canvas)
                n =0
 
       canvas.update()
    
    backround = canvas.create_image_with_size(0, 0, w, h,'city.png')
    silah = canvas.create_image_with_size(20, 30, 70, 80,'silah2.png')
    nisangah = canvas.create_image_with_size(0, 0, 40, 40, 'nişsangah.jpg')
    can1 = canvas.create_image_with_size(0, 0, 20, 20, 'can.png')
    can2 = canvas.create_image_with_size(20, 0, 20, 20, 'can.png')
    can3 = canvas.create_image_with_size(40, 0, 20, 20, 'can.png')
    can_list.append(can1)
    can_list.append(can2)
    can_list.append(can3)
    time_sign = canvas.create_text(0, 0, '')
    add_time_sign(canvas, game_time)
    #kare oluştur arkasına time sign
    while game_time>0 and heart > 0:
        silah_hareketi(canvas,  silah , nisangah , backround , time_sign, can1, can2, can3 , h , zombi_list)
        if time_piece !=5:
            time_piece +=1
        elif time_piece ==5:
            time_piece = 0
            game_time = game_time -1
        zombi_time.append(game_time)
        if zombi_time[-1]%5==0 :
              rastgele_zombi(canvas)
        zombi_hareketi(canvas, h , w , zombi_list, dx , dy)
        can_gitmesi(canvas, can_list , h , w , zombi_list )
        if len(can_list) == 0:
            heart = 0
        update_time_sign(canvas, time_sign, game_time)
        canvas.update()
        time.sleep(delay)
    if heart == 0 :
        canvas.create_image_with_size(0, 0, 1000, 1000, 'game_over.png')
    if game_time == 0:
        canvas.create_image_with_size(0, 0, 1000, 1000, 'win_page.jpeg')
    canvas.mainloop()


def add_time_sign(canvas, game_time):
    time_sign = canvas.create_text(850,0, "")
    canvas.set_font(time_sign, "Courier", 20)
    return time_sign


def update_time_sign(canvas, time_sign, game_time):
    
    canvas.set_text(time_sign, "Time: " + str(game_time))
    canvas.set_font(time_sign, "Courier", 20)
    canvas.moveto(time_sign, 850, 0)

def rastgele_zombi(canvas):
     x_size = 100     # random.randint(80,120)
     y_size = 100    # random.randint(80,120)
     number = random.randint(1, 4)
     if number == 1:
         x1 = random.randint(170, 350)
         y1 = random.randint(350, 550)
         zombi1 = canvas.create_image_with_size(x1, y1, x_size, y_size,'zombi6.jpeg' )
         zombi_list.append(zombi1)
     elif number == 2: 
         x2 = random.randint(750, 820)
         y2 = random.randint(440,640)
         zombi2 = canvas.create_image_with_size(x2, y2 , x_size , y_size,'zombi5.jpeg')
         zombi_list.append(zombi2)
     elif number == 3:
        x3 = random.randint(350, 500)
        y3 = random.randint(350,650)
        zombi3 = canvas.create_image_with_size(x3, y3, x_size, y_size,'zombi3.jpeg' )
        zombi_list.append(zombi3)
     else :
        x4 = random.randint(500,750)
        y4 = random.randint(300,650)
        zombi4 = canvas.create_image_with_size(x4, y4, x_size, y_size,'zombi4.jpeg')
        zombi_list.append(zombi4)
def silah_hareketi(canvas,  silah , nisangah , backround , time_sign, can1, can2, can3 , h , zombi_list):
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        clicks = canvas.get_new_mouse_clicks()
        canvas.moveto(silah, mouse_x - 35,700)
        canvas.moveto(nisangah, mouse_x - 35,mouse_y - 35)
        for click in clicks:
            bullet = canvas.create_oval(mouse_x -3 , 700, mouse_x  +3, 713)
            canvas.set_fill_color(bullet, 'yellow')
            bullet_list.append(bullet)
        for ammo in bullet_list:
           canvas.move(ammo, 0 , -50)
           for i in zombi_list:
               vurdu = False
               for k in bullet_list:
                   if (canvas.get_left_x(k)>canvas.get_left_x(i) and canvas.get_left_x(k)<canvas.get_left_x(i) +100 
                       and canvas.get_top_y(k)<canvas.get_top_y(i)+100 and canvas.get_top_y(k)>canvas.get_top_y(i)-100) :
                       zombi_list.remove(i)
                       bullet_list.remove(k)
                       canvas.delete(k)
                       canvas.delete(i)
                       vurdu = True
                       break
               if vurdu:
                    break

def zombi_hareketi(canvas , h , w , zombi_list , dx , dy):
    for zombi in zombi_list:
        if canvas.get_left_x(zombi) > w/2:
            canvas.move(zombi, -dx, dy)
        else:
            canvas.move(zombi, dx, dy)

def can_gitmesi(canvas, can_list , h , w , zombi_list):
    for i in zombi_list:
        if canvas.get_top_y(i) + 100 >= h:
                zombi_list.remove(i)
                canvas.delete(i)
                can = can_list[-1]
                canvas.delete(can)
                can_list.remove(can)
def option(canvas):
    canvas.delete_all()
    canvas.set_canvas_background_color('white')
    easy = canvas.create_rectangle(450, 300, 550, 380)
    easy_text = canvas.create_text(480, 340, 'EASY')
    medium = canvas.create_rectangle(450, 400, 550, 480)
    medium_text = canvas.create_text(480, 440, 'MEDİUM')
    hard = canvas.create_rectangle(450, 500, 550, 580)
    hard_text = canvas.create_text(480, 540, 'HARD')
    m=1
    while m>0 :
        clicks = canvas.get_new_mouse_clicks()
        for click in clicks:
            click_on_the_object=canvas.find_element_at(click.x, click.y)
            if (click_on_the_object  and click_on_the_object!=medium
                and click_on_the_object!=medium_text and click_on_the_object!=hard and click_on_the_object!=hard_text):
                dy = random.randint(1,2)
                canvas.delete_all()
                m = 0
            if (click_on_the_object  and click_on_the_object!=easy
                and click_on_the_object!=easy_text and click_on_the_object!=hard and click_on_the_object!=hard_text):
                dy = random.randint(3,5)
                canvas.delete_all()
                m = 0
               
            if (click_on_the_object  and click_on_the_object!=easy
                and click_on_the_object!=easy_text and click_on_the_object!=medium and click_on_the_object!=medium_text):
                dy = random.randint(5,8)
                canvas.delete_all()
                m = 0
        canvas.update()

 
if __name__ == "__main__":
    main()
    
