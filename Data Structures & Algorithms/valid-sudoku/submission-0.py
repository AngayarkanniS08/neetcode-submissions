class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        all_rows = {}
        for r_idx, row in enumerate(board):
             row_dict = {}
             for c_idx, val in enumerate(row):
                if val != ".":
                    row_dict[c_idx + 1] = int(val)
             if row_dict:
                 all_rows[r_idx + 1] = row_dict

        all_cols = {}
        for c_idx in range(9):
            col_dict = {}
            for r_idx in range(9):
                val = board[r_idx][c_idx]
                if val != ".":
                    col_dict[r_idx + 1] = int(val)
            if col_dict:
                all_cols[c_idx + 1] = col_dict

        sudoku_data = {
            "rows" : all_rows,
            "columns":all_cols
        }
        
        sub_boxes = {f"sub_box_{i}": {} for i in range(1, 10)}

        for row, cols in sudoku_data["rows"].items():
            for col, val in cols.items():
                box_num = ((row - 1) // 3) * 3 + ((col - 1) // 3) + 1
                box_key = f"sub_box_{box_num}"
                
                position_key = f"r{row}c{col}"
                
              
                sub_boxes[box_key][position_key] = val

        sudoku_data["sub_boxes"] = sub_boxes
        

        for row_num, inner_dict in sudoku_data["rows"].items():
            numbers = list(inner_dict.values())
            if len(numbers) != len(set(numbers)):
                return False  
            
      
        for col_num, inner_dict in sudoku_data["columns"].items():
            numbers = list(inner_dict.values())
            if len(numbers) != len(set(numbers)):
                return False  
                
       
        for box_name, inner_dict in sudoku_data["sub_boxes"].items():
            numbers = list(inner_dict.values())
            if len(numbers) != len(set(numbers)):
                return False  
                
        
        return True
