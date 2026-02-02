x = []

for y in ['2024', '2023', '2022', '2021', '2020']:
    all_scores = [[] for x in range(9)]
    with open(f'var/raw_results/results{y}.txt', 'r') as f:
        for l in list(f.readlines()):
            # Gets the list of scores of the current student
            # Desconsiders students with null overall score
            scores = l.split()[-17:]
            if float(scores[0]) == 0: continue

            # Scores are listed in the following format:
            # scores = [
            #   Overall Score,
            #   Portuguese Language Objective Exam,
            #   Mathematics Objective Exam,
            #   Literature Objective Exam,
            #   History Objective Exam,
            #   Geography Objective Exam,
            #   Physics Objective Exam,
            #   Chemistry Objective Exam,
            #   Biology Objective Exam,
            #   Portuguese Language Discursive Exam,
            #   Mathematics Discursive Exam,
            #   Literature Discursive Exam,
            #   History Discursive Exam,
            #   Geography Discursive Exam,
            #   Physics Discursive Exam,
            #   Chemistry Discursive Exam,
            #   Biology Discursive Exam,
            # ]
            general_score = float(scores[0])

            # Adds the score per subject (given by 2 * (Objective score + Discursive score))
            # to the all_scores list
            for j in range(1, 9):
                obj_score = 0 if scores[j] == '**' else float(scores[j])
                dis_score = 0 if scores[j + 8] == '**' else float(scores[j + 8])
                all_scores[j].append(2 * (obj_score + dis_score))

            all_scores[0].append(general_score)


    # Dumps the scores of each student in a file in the following format:
    #
    # Line 1 --> Overall
    # Line 2 --> Portuguese Language
    # Line 3 --> Mathematics 
    # Line 4 --> Literature 
    # Line 5 --> History 
    # Line 6 --> Geography 
    # Line 7 --> Physics
    # Line 8 --> Chemistry 
    # Line 9 --> Biology

    with open(f'var/operated_results/segmented_scores/segmented_scores{y}.txt', 'w+') as wf:
        for segment_scores in all_scores:
            wf.write(f'{segment_scores}\n')
        wf.close()
    
    with open(f'var/operated_results/average_scores/average_scores{y}.txt', 'w+') as wf:
        for segment_scores in all_scores:
            wf.write(f'{sum(segment_scores)/len(segment_scores):.2f}\n')
        wf.close()
