class player:
    #class variabel
    jumlah_player = 0
    #konstruktor
    def __init__(self, nickname, guild, region, point):
        self.nickname = nickname
        self.guild = guild
        self.region = region
        self.point = point
        player.jumlah =+ 1
    #methode
    def viewPlayer(self):
        print("---------------------")
        print("Data Player")
        print("Nickname : ", self.nickname)
        print("Guild : ", self.guild)
        print("Region : ", self.region)
        print("---------------------")
    
    def viewPoint(self):
        print("Data Point")
        print("Nickname : ", self.nickname)
        for point in self.point:
            print("Point : ", point)
        print("---------------------")

    def viewKeterangan(self):
        print("Keterangan")
        print("Nickname : ", self.nickname)
        print("Guild : ", self.guild)
        rata = sum(self.point)/len(self.point)
        print("Rata2 : ", rata)
        if rata >= 75:
            keterangan = "Upper Bracket"
        else:
            keterangan = "Lower Bracket"
        print("Keterangan : ", keterangan)
        print("---------------------")

#instansiasi objek
player1 = player("Udin", "Bren Legend", "Kanada", [72,74,70])
player2 = player("Budi", "C9 Esport", "USA", [89,100,78])
#pemanggilan objek player 1
player1.viewPlayer()
player1.viewPoint()
player1.viewKeterangan()
print("Jumlah player : ", player.jumlah_player)
#pemanggilan objek player 2
player2.viewPlayer()
player2.viewPoint()
player2.viewKeterangan()
print("Jumlah player : ", player.jumlah_player)