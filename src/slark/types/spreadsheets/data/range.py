from typing import Tuple

from slark.types._common import BaseModel


def row_column_to_excel(row: int, column: int) -> str:
    """Convert row and column to excel format.
    For example, 0,0 => A1, 1,0 => A2, 0,26 => AA1"""
    excel = ""
    while column >= 0:
        excel = chr(65 + column % 26) + excel
        column = column // 26 - 1
    return excel + str(row + 1)


def excel_to_row_column(excel: str) -> Tuple[int, int]:
    """Convert excel to row and column.
    For example, A1 => 0,0, A2 => 1,0, AA1 => 0,26"""
    column = 0
    for c in excel:
        if c.isalpha():
            column = column * 26 + ord(c) - 65
        else:
            row = int(excel[len(str(column)) :]) - 1
            return row, column
    return row, column


class Range(BaseModel):
    start_row: int = 0
    start_col: int = 0
    rows: int
    cols: int
    sheet_id: str

    @property
    def excel(self) -> str:
        start_pos = row_column_to_excel(self.start_row, self.start_col)
        end_pos = row_column_to_excel(
            self.start_row + self.rows - 1, self.start_col + self.cols - 1
        )
        return f"{self.sheet_id}!{start_pos}:{end_pos}"

    def intersect(self, other: "Range") -> "Range":
        if self.sheet_id != other.sheet_id:
            raise ValueError("Cannot intersect ranges from different sheets")
        if (
            self.start_row > other.start_row + other.rows - 1
            or other.start_row > self.start_row + self.rows - 1
        ):
            raise ValueError("Ranges do not intersect")
        if (
            self.start_col > other.start_col + other.cols - 1
            or other.start_col > self.start_col + self.cols - 1
        ):
            raise ValueError("Ranges do not intersect")
        start_row = max(self.start_row, other.start_row)
        start_col = max(self.start_col, other.start_col)
        end_row = min(self.start_row + self.rows - 1, other.start_row + other.rows - 1)
        end_col = min(self.start_col + self.cols - 1, other.start_col + other.cols - 1)
        return Range(
            start_row=start_row,
            start_col=start_col,
            rows=end_row - start_row + 1,
            cols=end_col - start_col + 1,
            sheet_id=self.sheet_id,
        )
