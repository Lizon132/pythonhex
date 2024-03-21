# profile.py
class ProfileRow:
    def __init__(self, byte_range, parameter, units, data_type):
        self.byte_range = byte_range
        self.parameter = parameter
        self.units = units
        self.data_type = data_type

class Profile:
    def __init__(self):
        self.rows = []

    def add_row(self, byte_range, parameter, units, data_type):
        row = ProfileRow(byte_range, parameter, units, data_type)
        self.rows.append(row)

    def delete_row(self, index):
        if 0 <= index < len(self.rows):
            del self.rows[index]

    # Method to move rows, modify rows, etc., can be added here
