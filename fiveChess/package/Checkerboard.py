#检查输赢
offset = [(1, 0), (0, 1), (1, 1), (1, -1)] # - | / \
class Checkerboard:
    """
    __init__第一参数永远是self,表示创建的类
    实例本身
    """
    def __init__(self, line_points):
        self._line_points = line_points
        # _ 仅仅是一个循环标志，相当i,j
        # _checkerboard 19*19的二维数组
        self._checkerboard = [[0] * line_points for _ in range(line_points)]
        self.ls = []  #划线标记
        """
        和普通数相比，在类中定义函数只有一点不同，就是第一参数永远是类的本身实例变量self，
        并且调用时，不用传递该参数。
        除此之外，类的方法(函数）和普通函数没啥区别，
        你既可以用默认参数、可变参数或者关键字参数
        （*args是可变参数，args接收的是一个tuple，**kw是关键字参数，kw接收的是一个dict）
        """
    def _get_checkerboard(self):    #私有
        return self._checkerboard
    # property() 函数的作用是在新式类中返回属性值。
    checkerboard = property(_get_checkerboard)
    def can_drop(self, point):# 判断是否可落子,看这个地方有没有被标记过
        return self._checkerboard[point.Y][point.X] == 0
    def drop(self, chessman, point): #落子
        #print(f'{chessman.Name} ({point.X}, {point.Y})') # 把黑棋/白棋落子的坐标打印出来
        self._checkerboard[point.Y][point.X] = chessman.Value   #point:落子位置  相当于标记
        # 打印获胜方出来
        ls = self._win(point)
        if ls:
            self.ls = self._tans(ls)
            # print("hhh",self.ls)
            return chessman #return:若该子落下之后即可获胜，则返回获胜方，否则返回 None
    def _tans(self,a): #逻辑->物理   # a [(11, 8), (11, 9), (11, 10), (11, 11), (11, 12)]
        return [(26+30*a[0][0],26+30*a[0][1]),(26+30*a[-1][0],26+30*a[-1][1])]

    # 判断是否赢了
    def _win(self, point): #私有方法
        cur_value = self._checkerboard[point.Y][point.X]
        for os in offset:
            ls = self._get_count_on_direction(point, cur_value, os[0], os[1])  #获取到五颗棋子的位置，如果赢
            if ls:
                return ls

    # 数步数
    def _get_count_on_direction(self, point, value, x_offset, y_offset):   #数步数
        count = 1
        ls = []
        for step in range(1, 5):#前进数
            x = point.X + step * x_offset
            y = point.Y + step * y_offset
            if 0 <= x < self._line_points and 0 <= y < self._line_points and self._checkerboard[y][x] == value:
                ls.append((x,y))
                count += 1
            else:
                break
        for step in range(1, 5):#后退数
            x = point.X - step * x_offset
            y = point.Y - step * y_offset
            if 0 <= x < self._line_points and 0 <= y < self._line_points and self._checkerboard[y][x] == value:
                ls.append((x, y))
                count += 1
            else:
                break
        if count==5:
            ls.append((point.X,point.Y))
            # print(ls)
            a =sorted(ls)
            return a  #好像放这里有点多余，但是只是想得到划线的xy
        return count >= 5 #0,1
