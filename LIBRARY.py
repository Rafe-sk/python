# wap design a library catalogue system using inheritance take base class
# library item and derived classes book dvd and journal each derived class should have unique attributes
#  and methods and ssystem should support checking in and checkout
class Library:
    def __init__(self,title,author,publisher):
        self.title=title
        self.author=author
        self.publisher=publisher

    def info(self):
        print(self.title)
        print(self.author)
        print(self.publisher)

print("""chode duniya ko rakh banake
      aise launde kabhi dil na jalaate 
      jaha jaani kabhi uth ti ungliya 
      aaj wahi se h uthne janaaze""")
tit=input("Enter the title:-")
aut=input("Enter author name:-")
pub=input("Enter publisher")

obj=Library()
obj(tit,aut,pub)