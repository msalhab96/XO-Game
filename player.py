class player():
    name = "Player"
    symbole =""
    turn = False
    enteries = []
    
    def checker(self):
        hor = [0, 0, 0]
        ver = [0, 0, 0]
        ltr = 0
        rtl = 0
        for i in range(0,3):
            for k in range(0,3):
                
                hor[i] = hor[i] + self.enteries[i][k]
                ver[i] = ver[i] + self.enteries[k][i]
        ltr = self.enteries[0][0] + self.enteries[1][1] + self.enteries[2][2]
        rtl = self.enteries[0][2] + self.enteries[1][1] + self.enteries[2][0]

        if (3 in hor) or (3 in ver) or ltr == 3 or rtl == 3:
            return True
        else:
            return False

