def solution(answers):
#     answer = []
#     correct = [len([0 for i in range(len(answers)) if i%5+1 == answers[i]]),len([0 for i in range(len(answers)) if (2, 1, 2, 3, 2, 4, 2, 5)[i%8] == answers[i]]),len([0 for i in range(len(answers)) if (3, 3, 1, 1, 2, 2, 4, 4, 5, 5)[i%10] == answers[i]])]
    
#     print(correct)
        
    return [index + 1 for index, val in enumerate([len([0 for i in range(len(answers)) if i%5+1 == answers[i]]),len([0 for i in range(len(answers)) if (2, 1, 2, 3, 2, 4, 2, 5)[i%8] == answers[i]]),len([0 for i in range(len(answers)) if (3, 3, 1, 1, 2, 2, 4, 4, 5, 5)[i%10] == answers[i]])]) if val == max([len([0 for i in range(len(answers)) if i%5+1 == answers[i]]),len([0 for i in range(len(answers)) if (2, 1, 2, 3, 2, 4, 2, 5)[i%8] == answers[i]]),len([0 for i in range(len(answers)) if (3, 3, 1, 1, 2, 2, 4, 4, 5, 5)[i%10] == answers[i]])])]