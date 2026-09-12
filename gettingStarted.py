### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    match question:
        case "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
            answer = "pcap"
        case "Are encoding and encryption the same? - Yes/No":
            answer = "No"
        case "Is it possible to decrypt a message without a key? - Yes/No":
            answer = "No"
        case "Is it possible to decode a message without a key? - Yes/No":
            answer = "Yes"
        case "Is a hashed message supposed to be un-hashed? - Yes/No":
            answer = "No"
        case "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
            answer = "817cbceb6ca79341e1117e49dd49264aa2a2e19a2049105d59d0567eba06f4a3"
        case "Is MD5 a secured hashing algorithm? - Yes/No":
            answer = "No"
        case "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
            answer = "4"
        case "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
            answer = "2"
        case _:
            # Catch unrecognized questions, including typos.
            answer = "This is not my beautiful wife! This is not my beautiful car! How did I get here?"
    return(answer)
# Complete all the questions.


if __name__ == "__main__":
    #use this space to debug and verify that the program works
    debug_question = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question))

#Questions:
#"In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
#"Are encoding and encryption the same? - Yes/No":
#"Is it possible to decrypt a message without a key? - Yes/No":
#"Is it possible to decode a message without a key? - Yes/No":
#"Is a hashed message supposed to be un-hashed? - Yes/No":
#"What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
#"Is MD5 a secured hashing algorithm? - Yes/No":
#"What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
#"What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
