class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        total_rows = len(matrix)
        total_cols = len(matrix[0])

        left = 0
        right = (total_cols*total_rows) -1 

        while left <= right:
            mid =  (left+right) //2 
            
            row_index = mid // total_cols
            col_index = mid % total_cols

            value = matrix [row_index][col_index]

            if value > target:
                right = mid -1
            elif value < target:
                left = mid + 1
            else:
                return True
        
        return False


        

        


      


                    


                
        




        
        
        
        
            
            
        
