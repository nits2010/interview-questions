from service.ratingService import RatingService


def main():
    service = RatingService()
    print("creating survey")
    # sruvey
    survey_id = service.create_survey("TEST")

    # create questions and keep their ids
    question1_id = service.add_questions(survey_id, "Q1")
    question2_id = service.add_questions(survey_id, "Q2")

    # add options for each question; keep option ids
    o1_id = service.add_option(survey_id, question1_id, "op1", 1)
    o2_id = service.add_option(survey_id, question1_id, "op2", 2)

    o3_id = service.add_option(survey_id, question2_id, "op3", 10)
    o4_id = service.add_option(survey_id, question2_id, "op4", 20)

    #share
    service.share_survey(survey_id, "user_id_1")
    service.share_survey(survey_id, "user_id_2")

    # submit
    user_id_1_answers = {
        question1_id: o1_id,
        question2_id: o4_id,
    }

    ## o1 = 1
    ## o4 = 20
    ## total = 21
    ## rating = 21 / 2 = 10.5
    user_id_2_answers = {
        question1_id: o2_id,
        question2_id: o3_id,
    }
    
    ## o2 = 2
    ## o3 = 10
    ## total = 12
    ## rating = 12 / 2 = 6
    
    # total rating = (10.5 + 6) / 2 = 8.25
    
    # submit
    print("submitting survey for user_id_1")
    service.submit_survey(survey_id, user_id_1_answers, "user_id_1")
    print("submitting survey for user_id_2")
    service.submit_survey(survey_id, user_id_2_answers, "user_id_2")



    overall_rating = service.get_survey_rating(survey_id)
    q1_rating = service.get_question_average_rating(survey_id, question1_id)

    print(f"overall rating = {overall_rating}")
    print(f"question 1 rating = {q1_rating}")

if __name__=="__main__":
    main()
