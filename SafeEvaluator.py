class SafeEvaluator:
    def __init__(self):
        pass
    def isSafe(self,i_A1,i_A2,i_A3,i_A4):

        s_Safe = False
        T = 40 #Threshold
        A1 = 0 #URL_Length
        A2 = 0 #FavIcon
        A3 = 0 #Security protocol
        A4 = 0 #Site Age

        if i_A1 != 0: #URL_Length
            A1 = 1
        if (i_A2 == False): #FavIcon
            A2 = 1
        if (i_A3 == False): #Security protocol
            A3 = 1
        if (i_A4 == False or i_A4 == None): #Site Age + check if no age is available
            A4 = 1

        if T - (A1 * 20) - (A2 * 15) - (A3 * 25) - (A4 * 20) > 0 :      #CHANGE VALUES
            s_Safe = True
        
        return s_Safe
