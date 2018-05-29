mouseMove("1527583681435.png")
click()
wait(1)
click("1527583681435.png")
if exists("1527580485956.png").similar(0.85):
    wait(0.5)
    mouseMove(Location(1214, 43))
    
m = find(Pattern("1527580485956.png").similar(0.5).targetOffset(100,0))
print m # message area: Match[10,0 30x22] score=1.00, target=(105,11)
elif exists("1527580458486.png").similar(0.85):
    
    mouseMove(Location(51, 48))