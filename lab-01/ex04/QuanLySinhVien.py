from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []
    
    def generateId(self):
        maxId = 1
        if (self.soLuongSinhVien() > 0):
            maxId = self.listSinhVien[0]._id
            for sv in self.listSinhVien:
                if (maxId < sv._id):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId
    def soLuongSinhVien(self):
        return self.listSinhVien.__len__()
    
    