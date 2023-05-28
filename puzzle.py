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
    Or(AKnight,AKnave),                     # A can be either a Knight or a Knave
    Not(And(AKnight,AKnave)),               # But cannot be both at the same time

    Or(BKnight,BKnave),                     # A can be either a Knight or a Knave
    Not(And(BKnight,BKnave)),               # But cannot be both at the same time

    Or(CKnight,CKnave),                     # A can be either a Knight or a Knave
    Not(And(CKnight,CKnave)),               # But cannot be both at the same time

    Implication(AKnight,And(AKnight,AKnave)),       # If A is a Knight, then it must be both Knight and Knave
    Implication(AKnave,Not(And(AKnight,AKnave))),   # If A is a Knave, then it is not true that it is both Knight and Knave


    #And(AKnight,AKnave),                    # According to A, A is both Knight and Knave
    #Implication(AKnave,Not(AKnight)),       # If A is a knave, cannot be a kinght
    #Implication(AKnight,Not(AKnave))        # If A is a knight, cannot be a knave
    # -- And(AKnight,AKnave)
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight,AKnave),                     # A can be either a Knight or a Knave
    Not(And(AKnight,AKnave)),               # But cannot be both at the same time

    Or(BKnight,BKnave),                     # B can be either a Knight or a Knave
    Not(And(BKnight,BKnave)),               # But cannot be both at the same time

    Or(CKnight,CKnave),                     # C can be either a Knight or a Knave
    Not(And(CKnight,CKnave)),               # But cannot be both at the same time

    Implication(AKnight,And(AKnave,BKnave)),    # If it is a knight, both A and B are knaves (I know it is impossible), because he always say the truth
    Implication(AKnave,Not(And(AKnave,BKnave))) # If it is a knave, it is not true that both A and B are Knaves because he always lies

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # TODO
    Or(AKnight,AKnave),                     # A can be either a Knight or a Knave
    Not(And(AKnight,AKnave)),               # But cannot be both at the same time

    Or(BKnight,BKnave),                     # B can be either a Knight or a Knave
    Not(And(BKnight,BKnave)),               # But cannot be both at the same time

    Or(CKnight,CKnave),                     # C can be either a Knight or a Knave
    Not(And(CKnight,CKnave)),               # But cannot be both at the same time

    Implication(AKnight,Or(And(AKnight,BKnight),And(AKnave,BKnave))),       # If A is a knight, both are the same kind
    Implication (AKnave,Not(Or(And(AKnight,BKnight),And(AKnave,BKnave)))),   # If A is knave, both are different

    Implication(BKnight,Or(And(AKnight,BKnave),And(AKnave,BKnight))),       # If B is a knight, both are different
    Implication (AKnave,Not(Or(And(AKnight,BKnave),And(AKnave,BKnight))))   # If B is a knave, both are the same (negation)


)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
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
