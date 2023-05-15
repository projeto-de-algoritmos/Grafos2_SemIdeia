def grafos_basico(grafo):
    grafo.adicionar_predio("S1", (0,0.1)) #c/l - <- -> + 
    grafo.adicionar_predio("S2", (1,0.1))
    grafo.adicionar_predio("S3", (1,1.2))
    grafo.adicionar_predio("37", (1.02,1.32))


    grafo.adicionar_predio("S4", (3.7,1.1))
    grafo.adicionar_predio("S5", (4.7,1))
    grafo.adicionar_predio("S6", (5.75,0.8))
    grafo.adicionar_predio("S7", (5.75,0.9))
    grafo.adicionar_predio("S8", (6.3,0.8))
    grafo.adicionar_predio("S9", (7,0.65))


    grafo.adicionar_predio("42", (7.57,0.55))
    grafo.adicionar_predio("43", (9.6,0.15))
    grafo.adicionar_predio("44", (9.6,0.29))
    grafo.adicionar_predio("45", (8.8,0.8))
    grafo.adicionar_predio("46", (0,0))
    

    grafo.adicionar_predio("S10", (7.05,1.1))
    grafo.adicionar_predio("I1", (1,1.9))
    grafo.adicionar_predio("I2", (2,2.1))
    grafo.adicionar_predio("I3", (2.3,1.6))
    grafo.adicionar_predio("46", (2.05,1.3))

    grafo.adicionar_predio("I4", (2.6, 1.9))
    grafo.adicionar_predio("I5", (3,2.3))
    grafo.adicionar_predio("I6", (3.88,3.2))
    grafo.adicionar_predio("11", (4.35,2.89))

    grafo.adicionar_predio("21", (3.91,2.44))
    grafo.adicionar_predio("22", (3.58,2.1))
    grafo.adicionar_predio("23", (3.38,1.86))
    grafo.adicionar_predio("24", (2.8,1.3))



    grafo.adicionar_predio("12", (4.85,2.6))
    grafo.adicionar_predio("25", (4.78,2.48))    
    grafo.adicionar_predio("26", (4.69,2.3))    
    grafo.adicionar_predio("27", (4.63,2.1))
    grafo.adicionar_predio("28", (4.58,1.99))
    grafo.adicionar_predio("29", (4.54,1.91))
    grafo.adicionar_predio("30", (4.38,1.58))
    grafo.adicionar_predio("31", (4.25,1.38))    
    grafo.adicionar_predio("32", (4.15,1.18))    


    grafo.adicionar_predio("13", (5.32,2.3))


    grafo.adicionar_predio("14", (5.68,2.05))
    grafo.adicionar_predio("15", (5.79,2))
    grafo.adicionar_predio("33", (5.66,1.75))
    grafo.adicionar_predio("34", (5.49,1.45))
    grafo.adicionar_predio("35", (5.4,1.25))
    grafo.adicionar_predio("36", (5.31,1))





    grafo.adicionar_predio("16", (6.65,1.58))

    grafo.adicionar_predio("I7", (4.58,3.9))
    grafo.adicionar_predio("2", (5.66,5))
    grafo.adicionar_predio("20", (5.55,5.89))


    grafo.adicionar_predio("47", (5.59,6.05))
    grafo.adicionar_predio("53", (6.1,5.96))
    grafo.adicionar_predio("54", (6.1,5.75))


    grafo.adicionar_predio("48", (5.6,6.6))
    grafo.adicionar_predio("49", (5.25,6.9))
    grafo.adicionar_predio("50", (5.02,7.1))
    grafo.adicionar_predio("51", (4.55,7.55))
    grafo.adicionar_predio("52", (4.15,7.95))




    grafo.adicionar_predio("10", (5.9,4.85))
    grafo.adicionar_predio("9", (6.6,4.42))
    grafo.adicionar_predio("8", (7.2,4.07))
    grafo.adicionar_predio("7", (7.5,3.85))

    grafo.adicionar_predio("6", (8.25,3.2))
    grafo.adicionar_predio("38", (8.28,2.9))
    grafo.adicionar_predio("39", (8.22,2.28))
    grafo.adicionar_predio("40", (8.15,1.55))
    grafo.adicionar_predio("41", (9,1.25))
    




    grafo.adicionar_predio("5", (8.95,2.63))
    grafo.adicionar_predio("55", (9.3,2.3))
    grafo.adicionar_predio("56", (9.6,2.8))
    grafo.adicionar_predio("57", (8.4,3.85))
    grafo.adicionar_predio("58", (7.48,4.68))                

    grafo.adicionar_predio("59", (7.59,4.85))
    grafo.adicionar_predio("60", (6.55,5.76))


    grafo.adicionar_predio("I8", (3.5,4.35))
    grafo.adicionar_predio("I9", (7.1,1.7))



    grafo.adicionar_predio("17", (7.19,2.2))
    grafo.adicionar_predio("18", (7.23,2.58))
    grafo.adicionar_predio("19", (7.28,2.68))


    grafo.adicionar_predio("I10", (7.1,1.5))

    grafo.adicionar_predio("Mocap", (1.1,3.7))
    grafo.adicionar_predio("Lab SS", (1.4,3.78))
    grafo.adicionar_predio("Lab NEI", (2.2,3.9))
    grafo.adicionar_predio("Lab Fisica", (2.7,3.9))
    grafo.adicionar_predio("Lab Quimica", (4.1,4.1))

    grafo.adicionar_predio("Direção", (2.5,5))
    grafo.adicionar_predio("Salas dos professores", (4.1,5.5))
    grafo.adicionar_predio("61", (4.35,5.75))
    grafo.adicionar_predio("62", (4.35,5.58))
    
    grafo.adicionar_predio("1", (0,0)) #c/l - <- -> + 
    
    grafo.adicionar_predio("3", (0,0))
    grafo.adicionar_predio("4", (0,0))



    grafo.adicionar_conexao("S1", "S2", 1)
    grafo.adicionar_conexao("S2", "S3", 1)
    grafo.adicionar_conexao("S3", "S4", 1)
    grafo.adicionar_conexao("S4", "S5", 1)
    grafo.adicionar_conexao("S5", "S6", 1)
    grafo.adicionar_conexao("S6", "S7", 1)
    grafo.adicionar_conexao("S7", "S8", 1)
    grafo.adicionar_conexao("S8", "S9", 1)
    grafo.adicionar_conexao("S9", "S10", 1)

    grafo.adicionar_conexao("I1", "I2", 1)
    grafo.adicionar_conexao("I2", "I3", 1)
    grafo.adicionar_conexao("I3", "I4", 1)
    grafo.adicionar_conexao("I4", "I5", 1)
    grafo.adicionar_conexao("I5", "I6", 1)
    grafo.adicionar_conexao("I6", "I7", 1)




    
    grafo.adicionar_conexao("I7", "2", 1)
    grafo.adicionar_conexao("10", "2", 1)
    grafo.adicionar_conexao("10", "9", 1)
    grafo.adicionar_conexao("8", "9", 1)
    grafo.adicionar_conexao("8", "7", 1)
    grafo.adicionar_conexao("6", "7", 1)
    grafo.adicionar_conexao("6", "5", 1)    
    grafo.adicionar_conexao("I6", "11", 1)
    grafo.adicionar_conexao("12", "11", 1)
    grafo.adicionar_conexao("I9", "I10", 1)
    grafo.adicionar_conexao("13", "14", 1)
    grafo.adicionar_conexao("14", "15", 1)
    grafo.adicionar_conexao("15", "16", 1)
    grafo.adicionar_conexao("6", "5", 1)    
    grafo.adicionar_conexao("12", "13", 1)    

    grafo.adicionar_conexao("I9", "17", 1)
    grafo.adicionar_conexao("17", "18", 1)    
    grafo.adicionar_conexao("19", "18", 1)    
    grafo.adicionar_conexao("19", "7", 1)    


    grafo.adicionar_conexao("I1", "S3", 5)
    grafo.adicionar_conexao("I10", "S10", 5)

    grafo.adicionar_conexao("16", "I10", 5)
    grafo.adicionar_conexao("I1", "Mocap",10)



    grafo.adicionar_conexao("Lab SS", "Mocap",1)
    grafo.adicionar_conexao("Lab NEI", "Lab SS",1)
    grafo.adicionar_conexao("Lab Fisica", "Lab NEI",1)
    grafo.adicionar_conexao("Lab Fisica", "I6",1)
    grafo.adicionar_conexao("Lab Quimica", "I7",1)
    grafo.adicionar_conexao("Lab Quimica", "I8",1)

    grafo.adicionar_conexao("Direção", "Lab Fisica",5)
    grafo.adicionar_conexao("Direção", "Salas dos professores",5)

    grafo.adicionar_conexao("20", "62",5)
    grafo.adicionar_conexao("20", "2",5)

    grafo.adicionar_conexao("11", "21",5)
    grafo.adicionar_conexao("22", "21",5)
    grafo.adicionar_conexao("22", "23",5)
    grafo.adicionar_conexao("24", "23",5)

    grafo.adicionar_conexao("12", "25",5)
    grafo.adicionar_conexao("26", "25",5)
    grafo.adicionar_conexao("26", "27",5)
    grafo.adicionar_conexao("28", "27",5)

    grafo.adicionar_conexao("28", "29",5)
    grafo.adicionar_conexao("30", "29",5)
    grafo.adicionar_conexao("30", "31",5)
    grafo.adicionar_conexao("32", "31",5)

    grafo.adicionar_conexao("15", "33",5)    
    grafo.adicionar_conexao("34", "33",5)        
    grafo.adicionar_conexao("34", "35",5)    
    grafo.adicionar_conexao("36", "35",5)    

    grafo.adicionar_conexao("36", "S7",5)    
    grafo.adicionar_conexao("36", "32",5)    
    grafo.adicionar_conexao("24", "32",5)    
    grafo.adicionar_conexao("46", "37",5) 
    grafo.adicionar_conexao("46", "24",5) 
    grafo.adicionar_conexao("S3", "37",5) 

    grafo.adicionar_conexao("6", "38",5) 
    grafo.adicionar_conexao("38", "39",5) 
    grafo.adicionar_conexao("40", "39",5) 
    grafo.adicionar_conexao("40", "41",5) 
    grafo.adicionar_conexao("40", "I10",5) 
    grafo.adicionar_conexao("23", "31",5) 
    grafo.adicionar_conexao("22", "30",5) 
    grafo.adicionar_conexao("21", "28",5)     
    grafo.adicionar_conexao("34", "28",5)  

    grafo.adicionar_conexao("42", "S9",5)  
    grafo.adicionar_conexao("42", "43",5)  
    grafo.adicionar_conexao("44", "43",5)  
    grafo.adicionar_conexao("44", "45",5)  
    grafo.adicionar_conexao("41", "45",5)  
    grafo.adicionar_conexao("I3", "46",5)  

    grafo.adicionar_conexao("47", "48",5)  
    grafo.adicionar_conexao("49", "48",5)  
    grafo.adicionar_conexao("49", "50",5)      
    grafo.adicionar_conexao("51", "50",5)      
    grafo.adicionar_conexao("51", "52",5)      


    grafo.adicionar_conexao("47", "53",5)      
    grafo.adicionar_conexao("54", "53",5)      
    grafo.adicionar_conexao("54", "20",5)          


    grafo.adicionar_conexao("5", "55",5)      
    grafo.adicionar_conexao("56", "55",5)      
    grafo.adicionar_conexao("56", "57",5)          

    grafo.adicionar_conexao("57", "58",5)      
    grafo.adicionar_conexao("54", "58",5)      

    grafo.adicionar_conexao("59", "58",5)      
    grafo.adicionar_conexao("59", "60",5)      
    grafo.adicionar_conexao("53", "60",5)   
    grafo.adicionar_conexao("48", "60",5)   

    grafo.adicionar_conexao("Salas dos professores", "62",5)
    grafo.adicionar_conexao("62", "61",5)
    grafo.adicionar_conexao("47", "61",5)