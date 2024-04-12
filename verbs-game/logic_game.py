def game_logic(answer, correct_answer):
  if answer == correct_answer:
    print("Correct!")
    cont = True
  else:
    print("Incorrect!")
    print("The correct answer is: "+correct_answer)
    cont = False
    
  return cont