from DepartmentPackage.InstructorModule import Instructor

class Department:
    def __init__(self, name):
        self.name=name
        self.faculty=dict()        
    
    def __str__(self):
        return f"{self.name}"
    
    
    def __contains__(self, faculty):
        if isinstance(faculty, Instructor):
            if faculty.id in self.faculty:
                return True
        return False
        
    def addFaculty(self, faculty):
        if isinstance(faculty, Instructor):
            self.faculty.setdefault(faculty.id,faculty)
            
    def delFaculty(self, IDdata):
        if IDdata in self.faculty:
            self.faculty.pop(IDdata)
            
    def getFaculty(self, IDdata):
        return self.faculty[IDdata]
    
    
    def printFaculty(self):
        for i in self.faculty.values():
            i.greeting()
            
    def sortFaculty(self):
        return sorted(self.faculty.items(), key=lambda item:item[1])