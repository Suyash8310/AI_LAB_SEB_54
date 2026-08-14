from experta import *
class StudentFacts(Fact):
    pass
class CareerExpertSystem(KnowledgeEngine):
    @Rule(StudentFacts(likes='Maths'), StudentFacts(likes='Physics'))
    def mechanical(self):
        print("Suggested Career Path: Mechanical Engineering")
    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Maths'))
    def computer(self):
        print("Suggested Career Path: Computer Engineering")
    @Rule(StudentFacts(likes='mechanic'), StudentFacts(likes='Physics'))
    def biotech(self):
        print("Suggested Career Path: civil")
    @Rule(StudentFacts(likes='Circuits'), StudentFacts(likes='Maths'))
    def electronics(self):
        print("Suggested Career Path: Electronics Engineering")

def main():
    engine = CareerExpertSystem()
    engine.reset()
    
    print("Welcome to the Career Path Expert System!")
   
    print(" | Maths                  ")
    print(" | Programming            ")
    print(" | information technology ")
    print(" | mechanic               ")
    print(" | Electronic               ")
    print(" | Physics")
    interests = input("Enter your interests separated by commas (e.g., Maths, Physics, Programming): ").split(',')
    for interest in interests:
        engine.declare(StudentFacts(likes=interest.strip()))
    engine.run()
if __name__ == "__main__":
    main()
