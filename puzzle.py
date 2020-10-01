from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # Information from structure of problem.
    Or(AKnight,AKnave),                           # Either a knight or Knave.
    Not(And(AKnight,AKnave)),                     # Not both knight and knave.
    
    # Information from statements.
    Biconditional(And(AKnight,AKnave), AKnight)   # A is knight if he said true
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # Information from structure of problems.
    Or(AKnight,AKnave),                        # Either a knight or knave.
    Not(And(AKnight,AKnave)),                  # Not both Knight and Knave.
    Or(BKnight,BKnave),                        # Either a knight or knave.
    Not(And(AKnight,AKnave)),                  # Not both knight and knave.
    
    # Information from statements.
    Biconditional(And(AKnave,BKnave), AKnight) # A is a knight if he said truth
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # Information from structure of problem.
    Or(AKnight,AKnave),                        # Either a knight or knave.
    Not(And(AKnight,AKnave)),                  # Not both knight and knave.
    Or(BKnight,BKnave),                        # Either a knight or knave.
    Not(And(BKnight,BKnave)),                  # Not both knight and knave.
    
    # Information from statements.
    Biconditional(Or(And(AKnave,BKnave), And(AKnight,BKnight)), AKnight),
                                               # A is a knight if he said truth
    Biconditional(Or(And(AKnave,BKnight), And(AKnight,BKnave)), BKnight),
                                               # B is a knight if he said truth
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Information from structure of problem.
    Or(AKnight,AKnave),                          # Either a knight or knave.
    Not(And(AKnight,AKnave)),                    # Not both knight and knave.
    Or(BKnight,BKnave),                          # Either a knight or knave.
    Not(And(BKnight,BKnave)),                    # Not both knight and knave.
    Or(CKnight,CKnave),                          # Either a knight or knave.
    Not(And(CKnight,CKnave)),                    # Not both knight and knave.
    
    # Information from statements.
    Biconditional(AKnight, Or(AKnight,AKnight)),
                                                 # A is knight if he said truth
    Biconditional(BKnight, Biconditional(AKnight,AKnave)),
                                                 # B is knight if he said truth
    Biconditional(BKnight, CKnave),              # B is knight if he said truth
    
    Biconditional(CKnight, AKnight)              # C is knight if he said truth                                             
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
