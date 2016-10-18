import sys
from pico2d import *
import random
sys.path.append('../LabsAll/Labs')
TileSize = 20
width=40
height=30
from random import randint
housenum=2
grassnum=0
temphouse=0
castleSize=100
matrix=[]








class node:
    GRASS, CASTLE, E_CASTLE, BLOCK,TREE, TREE2, TILE, E_TILE = 0,1,2,3,4,5,6,7

    def __init__(self):
        self.H = None
        self.G = 0
        self.F = None
        self.parent = None
        self.is_blocked = False
        self.is_target = False
        self.is_start = False
        self.walked_on = False
        self.state=None



    def __str__(self):
        if self.is_blocked:
            return "B"
        elif self.is_target:
            return "X"
        elif self.is_start:
            return "O"
        elif self.walked_on:
            return "*"
        else:
            return " "





def create_base(): #맵초기화해주기
    for x in range(width):
        matrix.append([])
        for y in range(height):
            matrix[x].append(node())
            matrix[x][y].state=node.GRASS
            coin = randint(1, 15)
            if coin >13:
                if coin ==14:
                    matrix[x][y].state=node.TREE
                else:
                    matrix[x][y].state = node.TREE2
                matrix[x][y].is_blocked = True
            if x == 0 or x == width-2 or y == 0 or y == height-2:
                matrix[x][y].is_blocked = True
                matrix[x][y].state=node.BLOCK

    matrix[3][14].state = node.CASTLE
    matrix[35][14].state = node.E_CASTLE
    matrix[3][14].is_blocked = False
    matrix[25][14].is_blocked = False


def create_map():
    from random import randint
    #matrix = []
    #for x in range(40):
    #    matrix.append([])
    #    for y in range(30):
    #        matrix[x].append(node())
    #        if x==0  or x==38  or y==0  or y==28:
    #            matrix[x][y].is_blocked=True
    #for x in range(3,10,1):
    #    matrix[x][25].is_blocked=True#
    #matrix[3][14].is_castle=True
    #matrix[35][25].is_blocked=True
    finish = (35,15)
    #finish = (randint(0, 9), randint(0, 29))#
    start =  (house[temphouse].x, house[temphouse].y)
    print(house[temphouse].x,house[temphouse].y)
    while start == finish:
       finish = (randint(0, width-1), randint(0, height-1))
    #matrix[start[0]][start[1]].is_start = True
    #matrix[start[0]][start[1]].is_blocked = False
    #matrix[finish[0]][finish[1]].is_target = True
    #matrix[finish[0]][finish[1]].is_blocked = False
    return matrix, finish, start


#def print_map(matrix):
#    temp=[]
#    x=0
#    y=0
#    image = load_image('grass.png')
#    for row in matrix:
#        row_copy=row[:]
#        y+=1
#        for i in row_copy:
#            x+=1
#            if show(i)==1:
#                image.draw(y*TileSize, x*TileSize)


#
#   for row in matrix:

#       row_copy = row[:]

#       row_copy.insert(0, "|")

#       row_copy.append("|")

#       temp.append(" ".join(str(i) for i in row_copy))

#   temp.append(" " + "=" * 61)

#   info_bar = "| Start: (%d,%d)  Target: (%d,%d)  |" % (start_node[0], start_node[1], target_node[0], target_node[1])
#   temp.append(info_bar)
#   temp.append(" " + "=" * 61)
#   return "\n".join(temp)


#def print_map(matrix):
#   temp = [" " + "=" * 61]

#   for row in matrix:
#       row_copy = row[:]

#       row_copy.insert(0, "|")
#
#       row_copy.append("|")

#       temp.append(" ".join(str(i) for i in row_copy))

#   temp.append(" " + "=" * 61)

#   info_bar = "| Start: (%d,%d)  Target: (%d,%d)  |" % (start_node[0], start_node[1], target_node[0], target_node[1])
#   temp.append(info_bar)
#   temp.append(" " + "=" * 61)
#   return "\n".join(temp)


def get_neighbors(cur_node):
    x, y = cur_node

    for neighbor in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]:
        nx, ny = neighbor

        yield (nx + x, ny + y)


def check_node(chk_node, matrix):
    x, y = chk_node

    if y < 0:
        return False

    if x < 0:
        return False

    if x > len(matrix) - 1:
        return False

    if y > len(matrix[x]) - 1:
        return False

    if matrix[x][y].is_blocked:
        return False

    return True


def get_G(next_node, cur_node):
    cx, cy = cur_node

    nx, ny = next_node

    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        if cx + dx == nx and cy + dy == ny:
            return 10
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        if cx + dx == nx and cy + dy == ny:
            return 14


def get_H(node, target_node):
    cx, cy = node

    tx, ty = target_node

    if tx > cx:

        x_diff = tx - cx

    else:

        x_diff = cx - tx

    if ty > cy:

        y_diff = ty - cy

    else:

        y_diff = cy - ty

    return (abs(x_diff) + abs(y_diff)) * 10


def get_parent_G(parent):
    px, py = parent

    return new_map[px][py].G


def get_parent(parent):
    return parent


#def sho#w_parent(parent):
#    py,px=parent
#    info_bar = "|  (%d,%d)  |" % (py,px)
#    temp.append(info_bar)
#    return "\n".join(temp)


def blocked_corner(neighbor, cur_node):
    x, y = cur_node

    if get_G(neighbor, cur_node) == 14:

        if (x - 1, y - 1) == neighbor:

            if new_map[x - 1][y].is_blocked and new_map[x][y - 1].is_blocked:
                return True

        if (x + 1, y - 1) == neighbor:

            if new_map[x + 1][y].is_blocked and new_map[x][y - 1].is_blocked:
                return True

        if (x - 1, y + 1) == neighbor:

            if new_map[x - 1][y].is_blocked and new_map[x][y + 1].is_blocked:
                return True

        if (x + 1, y + 1) == neighbor:

            if new_map[x + 1][y].is_blocked and new_map[x][y + 1].is_blocked:
                return True

    return False


def astar(matrix):
    sx, sy = start_node

    open_list = {start_node: matrix[sx][sy].G}

    closed_list = []

    while True:

        if len(open_list) == 0:
            return False

        cur_node = min(open_list, key=open_list.get)

        del open_list[cur_node]

        closed_list.append(cur_node)

        if target_node in closed_list:
            return True

        for neighbor in get_neighbors(cur_node):

            if check_node(neighbor, matrix) and neighbor not in closed_list:

                x, y = neighbor

                if neighbor in open_list:

                    if get_G(neighbor, cur_node) + get_parent_G(cur_node) < new_map[x][y].G:

                        new_map[x][y].parent = cur_node

                        new_map[x][y].G = get_G(neighbor, cur_node) + get_parent_G(cur_node)

                        new_map[x][y].H = get_H(neighbor, target_node)

                        new_map[x][y].F = new_map[x][y].G + new_map[x][y].H

                    else:

                        pass

                else:

                    new_map[x][y].G = get_G(neighbor, cur_node) + get_parent_G(cur_node)

                    new_map[x][y].H = get_H(neighbor, target_node)

                    new_map[x][y].F = new_map[x][y].G + new_map[x][y].H

                    new_map[x][y].parent = cur_node

                if blocked_corner(neighbor, cur_node):

                    if neighbor == target_node:

                        pass

                    else:

                        closed_list.append(neighbor)

                else:

                    open_list[neighbor] = new_map[x][y].F


def setup_failed(matrix):
    for x in range(len(matrix) - 1):
        for y in range(len(matrix[x]) - 1):
            if matrix[x][y].parent != None:
                matrix[x][y].walked_on = True




def show_print(matrix):
    image1 = None
    image2 = None
    image3 = None
    image4 = None
    image5 = None
    image6 = None
    image7 = None
    image8 = None
    image9=None
    if image1 == None:
        image1 = load_image('ice.png')
    if image2 == None:
        image2 = load_image('castle.png')
    if image3 == None:
        image3 = load_image('e_castle.png')
    if image4 == None:
        image4 = load_image('block.png')
    if image5 == None:
        image5 = load_image('tree1.png')
    if image6 == None:
        image6 = load_image('tree2.png')
    if image7 == None:
        image7 = load_image('tile.png')
    if image8 == None:
        image8 = load_image('e_tile.png')
    for x in range(len(matrix) - 1):
        for y in range(len(matrix[x]) - 1):
            if matrix[x][y].state==node.GRASS:
                image1.clip_draw(0, 0, TileSize, TileSize, x * TileSize, y * TileSize)
            elif matrix[x][y].is_blocked == True:
                if matrix[x][y].state==node.TREE:
                    image5.clip_draw(0, 0, 30,30, x * TileSize, y * TileSize)
                elif matrix[x][y].state==node.TREE2:
                    image6.clip_draw(0, 0, 30, 30, x * TileSize, y * TileSize)
                elif matrix[x][y].state==node.BLOCK:
                    image4.clip_draw(0, 0, TileSize, TileSize, x * TileSize, y * TileSize)
            elif matrix[x][y].state==node.CASTLE:
                image2.clip_draw(0, 0, castleSize, castleSize, x * TileSize, y * TileSize)
            elif matrix[x][y].state==node.E_CASTLE:
                image3.clip_draw(0, 0, castleSize, castleSize, x * TileSize, y * TileSize)
            elif matrix[x][y].state==node.TILE:
                image7.clip_draw(0, 0,TileSize, TileSize, x * TileSize, y * TileSize)
            elif matrix[x][y].state==node.E_TILE:
                image8.clip_draw(0, 0, castleSize, castleSize, x * TileSize, y * TileSize)




class e_House:
    image=None
    num=2
    def __init__(self):
        self.x,self.y=3,20
        self.timer=0
        self.hp=300
        self.frame=0
        self.size=30
        self.onoff=False
        self.list=None
        if House.image == None:
            House.image = load_image('house.png')

        def draw(self):
            self.image.clip_draw(self.frame * 50, 0, self.size, self.size, self.x * TileSize, self.y * TileSize)
class House:
    image=None
    num=2
    def __init__(self):
        self.x,self.y=3,20
        self.timer=0
        self.hp=300
        self.frame=0
        self.size=30
        self.onoff=False
        self.list=None

        if House.image == None:
            House.image = load_image('house.png')

    def draw(self):
        self.image.clip_draw(self.frame * 50, 0, self.size, self.size, self.x*TileSize, self.y*TileSize)

    def update(self):
        if(self.timer % 10)==0:
            self.onoff=True
        else:
            self.onoff=False
        self.timer+=1

    def set_all(self,matrix):
        matrix[self.x][self.y].is_house=True



class Grass:
    WALK, DIE, RUN, ATTACK = 0, 1, 2, 3
    num=0
    image=None
    def __init__(self):
        self.x, self.y= house[temphouse].x,house[temphouse].y
        self.frame=0
        self.imageframe=random.randint(0, 9)
        self.drawx, self.drawy=self.x*TileSize, self.y*TileSize
        self.parnum = 0
        self.parlist=[]
        self.speed=5
        self.state = self.RUN
        if Grass.image == None:
            Grass.image = load_image('Knight.png')

    def draw(self):
        self.image.clip_draw(self.imageframe*TileSize, self.state*TileSize, TileSize, TileSize, self.drawx, self.drawy)

    def handle_walk(self):
        pass

    def handle_die(self):
        pass

    def handle_run(self):
        if self.frame==4:
            self.x = self.parlist[self.parnum][0]
            self.y = self.parlist[self.parnum][1]
            if len(self.parlist) - 1 > self.parnum:
                self.parnum += 1
            else:
                self.parnum -= 1
            self.frame=0
        self.drawx += (self.parlist[self.parnum][0] - self.x) * 5
        self.drawy += (self.parlist[self.parnum][1] - self.y) * 5
        self.frame += 1

    def handle_attack(self):
        pass

    handle_state={
        WALK: handle_walk,
        DIE: handle_die,
        RUN: handle_run,
        ATTACK: handle_attack
    }

    def get_xy(self):
        return self.x, self.y

    def get_parlist(self):
        if astar(new_map):
            cur_node = target_node  # 출발점좌표 저장
            while cur_node != start_node:  # 목표지점이 아닐때까지 반복
                cx, cy = cur_node
                cur_node = new_map[cx][cy].parent
                cx, cy = cur_node
                self.parlist.append([cx,cy])
                new_map[cx][cy].walked_on = True

    def update(self):
        self.imageframe = (self.frame + 1) % 10
        self.handle_state[self.state](self)


def handle_events():
    events=get_events()
    for event in events:
        if event.type==SDL_MOUSEBUTTONDOWN and event.button==SDL_BUTTON_LEFT:
            if matrix[event.x // TileSize][(599-event.y) // TileSize].is_blocked != True:
                temp = House()
                house.append(temp)
                house[0].num += 1
                house[house[0].num - 1].x = event.x // TileSize
                house[house[0].num - 1].y = (599 - event.y) // TileSize
                print(house[house[0].num - 1].x)


if __name__ == "__main__":

    import sys
    import time
    open_canvas()
    create_base()


    grass = []
    house=[]
    for i in range(2):
        temp=House()
        house.append(temp)
    new_map, start_node, target_node = create_map()
    show_print(new_map)
    house[1].x=3
    house[1].y=7




    while 1:
       clear_canvas()
       handle_events()
       show_print(new_map)
       #print(grass[grassnum].parlist)
       for i in range(house[0].num):
          if house[i].onoff==True:
               temphouse = i
               new_map, start_node, target_node = create_map()
               temp = Grass()
               grass.append(temp)
               grass[grassnum].get_parlist()
              # print(grass[grassnum].parlist)
               grassnum += 1
       for i in range(house[0].num):
          house[i].draw()
          house[i].update()

       for i in range(grassnum):
          grass[i].draw()
          grass[i].update()

       update_canvas()
       time.sleep(.3)


    #close_canvas()


   # show_print(new_map)

   #if astar(new_map):

   #   # sys.stdout.write("\n" * 20 + print_map(new_map))  ##맵과맵사이 공백
   #   # print_map(new_map)
   #   # sys.stdout.flush()
   #    cur_node = target_node #출발점좌표 저장
   #    while cur_node != start_node: #목표지점이 아닐때까지 반복
   #        clear_canvas()
   #        x,y = cur_node
   #        show_print(new_map)
   #        grass.draw()
   #        grass.update()
   #        cur_node = new_map[x][y].parent
   #        print("(%d %d )" % (cur_node))
   #        x, y = cur_node

   #        new_map[x][y].walked_on = True
   #        update_canvas()
   #        #sys.stdout.write("\n" * 17 + print_map(new_map))
   #        #print_map(new_map)
   #       # sys.stdout.flush()

   #        time.sleep(.3)#

    #    print
    #    ""


#   else:
#
#       setup_failed(new_map)

#       print
#       print_map(new_map)

#       print
#       "No dice, better luck next time."