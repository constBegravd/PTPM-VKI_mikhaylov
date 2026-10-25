class Converter:
    @staticmethod
    def do(x: float) -> int:
        if x >= 100.7:
            return 1000
        
        if 0.0 < x < 100.7:
            return int(x)
        
        if x == 0:
            raise ValueError("x == 0")
            
        if -30.4 <= x < 0.0:
            return int(x) - 5
        
        return -2000
