def hanoiTower(n, fromTower, toTower, tempTower):
    if n == 0:
        return
    else:
        hanoiTower(n-1, fromTower, tempTower, toTower)
        move(fromTower, toTower)
        hanoiTower(n-1, fromTower, tempTower, toTower)
        
